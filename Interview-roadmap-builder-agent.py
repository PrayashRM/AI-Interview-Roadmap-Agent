import google.generativeai as genai
from datetime import datetime
import json
import os

from dotenv import load_dotenv
load_dotenv()

#Importing serpAPI for google search
from serpapi import GoogleSearch
# Configuring the SerpAPI
serp_api_key = os.getenv("SERP_API_KEY")

#Playwright web scrapper
import asyncio
asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
from playwright.async_api import async_playwright

# Configure the Gemini API key
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("models/gemini-2.5-flash")


#<--------------------------------------------------------------------------------------------------------------------------------------->


# Agent 1: User Input Parser
# Extracts the necessary parts from the user input into a json format file for the next agent

def jd_parser(company_name: str, role: str, job_description: str):
    
    prompt = f""" 
    
    You are a Job Description Parser Agent.

    Input:
    Company: {company_name}
    Role: {role}
    Job Description: {job_description}

    Task:
    1. Extract key information from the Job Description.
    2. Categorize them into the following:
      - Technical Skills
      - Tools/Technologies
      - Core Responsibilities
      - Soft Skills
    3. Return output in structured JSON format.
    Example Output:
    {{
      "company": "Google",
      "role": "SDE-1",
      "technical_skills": ["Data Structures", "Algorithms", "System Design"],
      "tools": ["Python", "REST APIs", "Databases"],
      "responsibilities": ["Build scalable systems", "Collaborate with teams"],
      "soft_skills": ["Problem solving", "Communication"]
    }}
    """

    response = model.generate_content(prompt)
    
    # Try parsing model output to JSON
    try:
        result = json.loads(response.text)
    except json.JSONDecodeError:
        result = {"raw_output": response.text}

    return result



#<--------------------------------------------------------------------------------------------------------------------------------------->


# Agent 2: Information scrapper agent
# Based on the json file info. from the earlier agent,
# SerpAPI - do a google search and returns the top websites
# while then , Playwriter - scrapes data from all of the websites and passes that data to the next agent 


async def interview_info_scraper(company_name, role):
    # Step 1 – Searching using SerpAPI
    params = {
        "engine": "google",
        "q": (
            f"{company_name} {role} interview process "
            "site:glassdoor.com OR "
            "site:leetcode.com OR "
            "site:geeksforgeeks.org OR "
            "site:interviewbit.com OR "
            "site:careercup.com OR "
            "site:indeed.com OR "
            "site:reddit.com OR "
            "site:levels.fyi OR "
            "site:teamblind.com OR "
            "site:ambitionbox.com OR "
            "site:linkedin.com"
        ),
        "api_key": serp_api_key
    }
    search = GoogleSearch(params)
    results = search.get_dict()

    # Step 2 – Extracting the top URLs
    links = []
    for res in results.get("organic_results", [])[:3]:
        link = res.get("link")
        if link:
            links.append(link)

    # Step 3 – Scraping pages using Playwright
    scraped_texts = []
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        for url in links:
            try:
                await page.goto(url, wait_until="networkidle", timeout=30000)
                content = await page.content()
                scraped_texts.append(content)
            except Exception as e:
                print(f"Error scraping {url}: {e}")
                continue
        await browser.close()

    return {
        "company": company_name,
        "sources": links,
        "raw_texts": scraped_texts
    }


#<--------------------------------------------------------------------------------------------------------------------------------------->


# Agent 3: Roadmap_builder
# Generates a structured interview roadmap based on scraped text from the earlier agent.

def interview_roadmap_agent(company_name: str, role: str, scraped_texts: list):

    combined_text = "\n\n".join(scraped_texts[:2])  # limit text length for token efficiency

    prompt = f"""
                You are an Interview Roadmap Generator AI.

                Input Context:
                Company: {company_name}
                Role: {role}
                Extracted interview details and experiences: {combined_text}

                Task:
                1. Analyze and summarize the company's interview process.
                2. Output only in this exact JSON structure:
                {{
                "company": "string",
                "role": "string",
                "rounds": [
                    {{
                    "type": "string",
                    "topics": ["topic1", "topic2", ...]
                    }}
                ],
                "difficulty": "Easy | Medium | Hard",
                "recommended_order": ["topic1", "topic2", ...]
                }}
                3. Keep it concise:
                - 3-5 rounds maximum.
                - Topics should be short and grouped logically.
                - One overall difficulty level for the entire process.
                - Recommended order should summarize ideal preparation flow.
                4. If web data is unavailable or blocked, infer typical interview patterns for the company and role based on general knowledge.
                """


    response = model.generate_content(prompt)

    # Try to convert to JSON
    try:
        result = json.loads(response.text)
    except json.JSONDecodeError:
        result = {"raw_output": response.text}

    return result


#<--------------------------------------------------------------------------------------------------------------------------------------->


# <-------------CONFIG------------->
INPUT_FOLDER = os.path.join(os.getcwd(), "Isaii_interview_project\input_json")
OUTPUT_FOLDER = os.path.join(os.getcwd(), "Isaii_interview_project\output_json")
os.makedirs(INPUT_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


# <----------Orchestrator---------->
def orchestrator(input_filename):
    input_path = os.path.join(INPUT_FOLDER, input_filename)

    if not os.path.exists(input_path):
        print(f"❌ Input file not found: {input_path}")
        return

    # Read input JSON
    with open(input_path, "r", encoding="utf-8") as f:
        input_data = json.load(f)

    company = input_data.get("company", "").strip()
    role = input_data.get("role", "").strip()
    job_description = input_data.get("job_description", "").strip()

    if not (company and role and job_description):
        print("❌ Missing required fields in input JSON (company, role, job_description).")
        return

    print(f"\n=== Processing {company} - {role} ===")

    # ----- Agent 1: JD Parser -----
    print("\n🔍 Running JD Parser Agent...")
    jd_info = jd_parser(company, role, job_description)

    # ----- Agent 2: Interview Info Scraper -----
    print("\n🌐 Running Interview Info Scraper Agent...")
    interview_info = asyncio.run(interview_info_scraper(company, role))

    # ----- Agent 3: Roadmap Agent -----
    print("\n🧭 Running Interview Roadmap Agent...")
    roadmap = interview_roadmap_agent(company, role, interview_info["raw_texts"])

    # Parse JSON safely
    raw_text = roadmap.get("raw_output", "")
    if "```json" in raw_text:
        raw_text = raw_text.replace("```json", "").replace("```", "").strip()

    try:
        parsed_roadmap = json.loads(raw_text)
    except json.JSONDecodeError:
        parsed_roadmap = {"raw_output": raw_text}

    # Combine results
    final_output = {
        "company": company,
        "role": role,
        "jd_analysis": jd_info,
        "interview_sources": interview_info.get("sources", []),
        "roadmap": parsed_roadmap,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

    # Save final JSON
    output_filename = f"{company}_{role}_interview_roadmap.json"
    output_path = os.path.join(OUTPUT_FOLDER, output_filename)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(final_output, f, indent=2, ensure_ascii=False)

    print(f"\n✅ Output saved to: {output_path}")



input_file = input("Enter input JSON filename (inside input_data folder): ").strip()
orchestrator(input_file)