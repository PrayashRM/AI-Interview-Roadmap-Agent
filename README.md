<html lang="en">
<body>

<h1 align="center">AI-Powered Interview Preparation Research Agent</h1>

<p align="center">
  <b>GenAI | Multi-Agent System | Web Scraping | NLP</b><br>
  An intelligent multi-agent system that generates <b>personalized interview preparation roadmaps</b> by analyzing job descriptions and company interview processes 🎯
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue?logo=python&style=for-the-badge" alt="Python">
  <img src="https://img.shields.io/badge/Gemini-2.5_Flash-orange?logo=google&style=for-the-badge" alt="Gemini">
  <img src="https://img.shields.io/badge/Playwright-Async-green?style=for-the-badge" alt="Playwright">
  <img src="https://img.shields.io/badge/SerpAPI-Integrated-red?style=for-the-badge" alt="SerpAPI">
  <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge" alt="Status">
</p>

<hr>

<h2>🚀 Overview</h2>

<p>
This project implements an <b>intelligent multi-agent AI system</b> that automates interview preparation research. Given a company name, role, and job description, the system:
</p>

<ul>
  <li>📝 <b>Parses job descriptions</b> to extract key skills, tools, and responsibilities</li>
  <li>🌐 <b>Scrapes real interview experiences</b> from platforms like Glassdoor, LeetCode, GeeksforGeeks, and more</li>
  <li>🧭 <b>Generates structured roadmaps</b> with interview rounds, topics, difficulty levels, and preparation order</li>
</ul>

<p>
The system uses <b>Google's Gemini 2.5 Flash</b> for intelligent parsing and roadmap generation, <b>SerpAPI</b> for targeted web searches, and <b>Playwright</b> for efficient web scraping.
</p>

<hr>

<h2>🎯 Key Features</h2>

<ul>
  <li>🤖 <b>Multi-Agent Architecture:</b> Three specialized agents working in orchestrated harmony
    <ul>
      <li><b>Agent 1:</b> Job Description Parser - Extracts structured information from JDs</li>
      <li><b>Agent 2:</b> Information Scraper - Gathers real interview experiences from web</li>
      <li><b>Agent 3:</b> Roadmap Builder - Generates personalized preparation plans</li>
    </ul>
  </li>
  <li>🌐 <b>Intelligent Web Scraping:</b> Targets 11+ trusted platforms (Glassdoor, LeetCode, GeeksforGeeks, etc.)</li>
  <li>🧠 <b>Gemini 2.5 Flash Integration:</b> Advanced LLM for intelligent content analysis</li>
  <li>📊 <b>Structured JSON Output:</b> Clean, parseable roadmaps ready for integration</li>
  <li>⚡ <b>Async Processing:</b> High-performance concurrent web scraping</li>
  <li>🎨 <b>Automatic Categorization:</b> Skills mapped to relevant interview topics</li>
  <li>💾 <b>Persistent Storage:</b> Input/output JSON files for easy tracking</li>
</ul>

<hr>

<h2>🏗️ System Architecture</h2>

<p>The system follows a <b>multi-agent orchestration pattern</b> with three specialized agents:</p>

<pre><code>
                                                                ┌─────────────────┐
                                                                │  User Input     │
                                                                │  (JSON file)    │
                                                                └────────┬────────┘
                                                                         │
                                                                         ▼
                                                        ┌─────────────────────────────────┐
                                                        │          Orchestrator           │
                                                        │  (Coordinates agent workflow)   │
                                                        └────────────────┬────────────────┘
                                                                         │
                                                                         ▼
                                                        ┌─────────────────────────────────┐
                                                        │  Agent 1: JD Parser             │
                                                        │  • Extracts technical skills    │
                                                        │  • Identifies tools/tech        │
                                                        │  • Maps responsibilities        │
                                                        └────────────────┬────────────────┘
                                                                         │
                                                                         ▼
                                                        ┌─────────────────────────────────┐
                                                        │  Agent 2: Info Scraper          │
                                                        │  • SerpAPI Google Search        │
                                                        │  • Playwright Web Scraping      │
                                                        │  • Content Extraction           │
                                                        └────────────────┬────────────────┘
                                                                         │
                                                                         ▼
                                                        ┌─────────────────────────────────┐
                                                        │  Agent 3: Roadmap Builder       │
                                                        │  • Analyzes interview patterns  │
                                                        │  • Structures preparation plan  │
                                                        │  • Generates difficulty rating  │
                                                        └────────────────┬────────────────┘
                                                                         │
                                                                         ▼
                                                        ┌─────────────────────────────────┐
                                                        │  JSON Output                    │
                                                        │  (Structured Roadmap)           │
                                                        └─────────────────────────────────┘
</code></pre>

<hr>

<h2>🔧 Agent Breakdown</h2>

<h3>Agent 1: Job Description Parser</h3>

<p>
<b>Purpose:</b> Extracts and categorizes key information from job descriptions using Gemini AI.
</p>

<p><b>Capabilities:</b></p>
<ul>
  <li>✓ Identifies technical skills (DSA, System Design, etc.)</li>
  <li>✓ Extracts tools and technologies (Python, REST APIs, databases)</li>
  <li>✓ Maps core responsibilities</li>
  <li>✓ Identifies required soft skills</li>
</ul>

<p><b>Output Format:</b></p>
<pre><code>{
  "company": "Google",
  "role": "SDE-1",
  "technical_skills": ["Data Structures", "Algorithms", "System Design"],
  "tools": ["Python", "REST APIs", "Databases"],
  "responsibilities": ["Build scalable systems", "Collaborate with teams"],
  "soft_skills": ["Problem solving", "Communication"]
}
</code></pre>

<h3>Agent 2: Information Scraper</h3>

<p>
<b>Purpose:</b> Gathers real interview experiences from trusted platforms using SerpAPI and Playwright.
</p>

<p><b>Target Platforms:</b></p>
<ul>
  <li>🔹 Glassdoor</li>
  <li>🔹 LeetCode</li>
  <li>🔹 GeeksforGeeks</li>
  <li>🔹 InterviewBit</li>
  <li>🔹 CareerCup</li>
  <li>🔹 Indeed</li>
  <li>🔹 Reddit</li>
  <li>🔹 Levels.fyi</li>
  <li>🔹 TeamBlind</li>
  <li>🔹 AmbitionBox</li>
  <li>🔹 LinkedIn</li>
</ul>

<p><b>Technology Stack:</b></p>
<ul>
  <li>📡 <b>SerpAPI:</b> Performs targeted Google searches</li>
  <li>🎭 <b>Playwright:</b> Async web scraping with JavaScript rendering support</li>
  <li>⚡ <b>Async/Await:</b> Concurrent scraping for faster results</li>
</ul>

<h3>Agent 3: Roadmap Builder</h3>

<p>
<b>Purpose:</b> Analyzes scraped content and generates structured interview preparation roadmaps.
</p>

<p><b>Features:</b></p>
<ul>
  <li>🎯 Identifies typical interview rounds (MCQ, Coding, System Design, HR)</li>
  <li>📚 Maps topics to each round</li>
  <li>⚖️ Assigns difficulty levels (Easy, Medium, Hard)</li>
  <li>🗺️ Creates recommended preparation order</li>
  <li>🧠 Fallback to general knowledge if web data unavailable</li>
</ul>

<hr>

<h2>📊 Input/Output Format</h2>

<h3>Input JSON Structure</h3>

<p>Place your input file in <code>input_json/</code> folder:</p>

<pre><code>{
  "company": "Google",
  "role": "SDE-1",
  "job_description": "We are looking for a Software Development Engineer with strong knowledge of Data Structures, Algorithms, and System Design. Experience with Python, REST APIs, and distributed systems is required..."
}
</code></pre>

<h3>Output JSON Structure</h3>

<p>Generated roadmap saved in <code>output_json/</code> folder:</p>

<pre><code>{
  "company": "Google",
  "role": "SDE-1",
  "jd_analysis": {
    "technical_skills": ["Data Structures", "Algorithms", "System Design"],
    "tools": ["Python", "REST APIs", "Databases"],
    "responsibilities": ["Build scalable systems"],
    "soft_skills": ["Problem solving", "Communication"]
  },
  "interview_sources": [
    "https://glassdoor.com/...",
    "https://leetcode.com/...",
    "https://geeksforgeeks.org/..."
  ],
  "roadmap": {
    "company": "Google",
    "role": "SDE-1",
    "rounds": [
      {
        "type": "MCQ",
        "topics": ["OS", "DBMS", "Networks"]
      },
      {
        "type": "Coding",
        "topics": ["Arrays", "DP", "Graphs", "Trees"]
      },
      {
        "type": "System Design",
        "topics": ["Scalability", "Load Balancing", "Caching"]
      },
      {
        "type": "HR",
        "topics": ["Behavioral", "Communication", "Leadership"]
      }
    ],
    "difficulty": "Hard",
    "recommended_order": ["DSA", "System Design", "Projects", "Behavioral"]
  },
  "timestamp": "2024-01-15 14:30:00"
}
</code></pre>

<hr>

<h2>🛠️ Technologies & Dependencies</h2>

<h3>Core Technologies</h3>

<table align="center">
  <tr>
    <th>Technology</th>
    <th>Purpose</th>
    <th>Version</th>
  </tr>
  <tr>
    <td>🔥 Python</td>
    <td>Core programming language</td>
    <td>3.9+</td>
  </tr>
  <tr>
    <td>🤖 Google Gemini</td>
    <td>LLM for intelligent parsing</td>
    <td>2.5 Flash</td>
  </tr>
  <tr>
    <td>🔍 SerpAPI</td>
    <td>Google search integration</td>
    <td>Latest</td>
  </tr>
  <tr>
    <td>🎭 Playwright</td>
    <td>Web scraping framework</td>
    <td>Latest</td>
  </tr>
  <tr>
    <td>📦 asyncio</td>
    <td>Async processing</td>
    <td>Built-in</td>
  </tr>
</table>

<h3>Required Python Packages</h3>

<pre><code>google-generativeai
python-dotenv
serpapi
playwright
asyncio
</code></pre>

<hr>

<h2>📦 Installation & Setup</h2>

<h3>1. Clone the Repository</h3>

<pre><code>git clone https://github.com/PrayashRM/AI-Interview-Research-Agent.git
cd AI-Interview-Research-Agent
</code></pre>

<h3>2. Install Dependencies</h3>

<pre><code># Install Python packages
pip install google-generativeai python-dotenv serpapi playwright

# Install Playwright browsers
playwright install
</code></pre>

<h3>3. Configure API Keys</h3>

<p>Create a <code>.env</code> file in the project root:</p>

<pre><code>GEMINI_API_KEY=your_gemini_api_key_here
SERP_API_KEY=your_serpapi_key_here
</code></pre>

<p><b>Getting API Keys:</b></p>
<ul>
  <li>🔑 <b>Gemini API:</b> Get from <a href="https://makersuite.google.com/app/apikey">Google AI Studio</a></li>
  <li>🔑 <b>SerpAPI:</b> Sign up at <a href="https://serpapi.com/">SerpAPI.com</a></li>
</ul>

<h3>4. Create Required Folders</h3>

<pre><code>mkdir input_json
mkdir output_json
</code></pre>

<hr>

<h2>🚀 Usage</h2>

<h3>Step 1: Prepare Input JSON</h3>

<p>Create a JSON file in <code>input_json/</code> folder (e.g., <code>google_sde.json</code>):</p>

<pre><code>{
  "company": "Google",
  "role": "SDE-1",
  "job_description": "Your job description text here..."
}
</code></pre>

<h3>Step 2: Run the Agent</h3>

<pre><code>python main.py
</code></pre>

<h3>Step 3: Enter Filename</h3>

<pre><code>Enter input JSON filename (inside input_data folder): google_sde.json
</code></pre>

<h3>Step 4: Check Output</h3>

<p>The generated roadmap will be saved in <code>output_json/</code> as:</p>
<pre><code>Google_SDE-1_interview_roadmap.json
</code></pre>

<hr>

<h2>📁 Project Structure</h2>

<pre><code>AI-Interview-Research-Agent/
│
├── Interview-roadmap-builder-agent.py                        # Main orchestrator script
├── .env-sample                           # API keys (not committed)
├── README.md                      # Documentation
│
├── input_json/                    # Input JSON files
│   ├── Amazon.json
│   └── Isaii.json
│
└── output_json/                   # Generated roadmaps
    ├── Amazon_Software Development Engineer_interview_roadmap.json
    └── Isaii_Generative AI Internship – Agent Development & LLM Integration_interview_roadmap.json
</code></pre>

<hr>

<h2>🎯 How It Works</h2>

<h3>Workflow Execution</h3>

<ol>
  <li>
    <b>📥 Input Processing</b>
    <ul>
      <li>Orchestrator reads input JSON file</li>
      <li>Validates required fields (company, role, JD)</li>
    </ul>
  </li>
  <li>
    <b>🔍 JD Parsing (Agent 1)</b>
    <ul>
      <li>Gemini AI analyzes job description</li>
      <li>Extracts skills, tools, responsibilities</li>
      <li>Categorizes into structured format</li>
    </ul>
  </li>
  <li>
    <b>🌐 Web Scraping (Agent 2)</b>
    <ul>
      <li>SerpAPI searches for interview experiences</li>
      <li>Playwright scrapes top 3 relevant URLs</li>
      <li>Extracts text content asynchronously</li>
    </ul>
  </li>
  <li>
    <b>🧭 Roadmap Generation (Agent 3)</b>
    <ul>
      <li>Gemini analyzes scraped interview data</li>
      <li>Identifies common interview patterns</li>
      <li>Structures rounds, topics, difficulty</li>
      <li>Generates recommended preparation order</li>
    </ul>
  </li>
  <li>
    <b>💾 Output Generation</b>
    <ul>
      <li>Combines all agent outputs</li>
      <li>Adds timestamp and metadata</li>
      <li>Saves as structured JSON file</li>
    </ul>
  </li>
</ol>

<hr>

<h2>💡 Example Use Cases</h2>

<h3>Use Case 1: Tech Giant Preparation</h3>

<p><b>Input:</b> Google SDE-1 position</p>
<p><b>Output:</b> Roadmap covering DSA, System Design, behavioral rounds with Hard difficulty</p>

<h3>Use Case 2: Startup Role</h3>

<p><b>Input:</b> Early-stage startup Full Stack Developer</p>
<p><b>Output:</b> Roadmap focusing on practical coding, projects, and cultural fit</p>

<h3>Use Case 3: Product Management</h3>

<p><b>Input:</b> Microsoft Product Manager</p>
<p><b>Output:</b> Roadmap covering product sense, execution, leadership, and technical awareness</p>

<hr>

<h2>📈 Performance Metrics</h2>

<table align="center">
  <tr>
    <th>Metric</th>
    <th>Value</th>
  </tr>
  <tr>
    <td>Average Processing Time</td>
    <td>~30-45 seconds</td>
  </tr>
  <tr>
    <td>Web Pages Scraped</td>
    <td>3 per query</td>
  </tr>
  <tr>
    <td>Supported Platforms</td>
    <td>11+</td>
  </tr>
  <tr>
    <td>Output Format</td>
    <td>Structured JSON</td>
  </tr>
  <tr>
    <td>Concurrent Scraping</td>
    <td>Yes (Async)</td>
  </tr>
</table>

<hr>

<h2>⚠️ Important Notes</h2>

<ul>
  <li>🔑 <b>API Keys Required:</b> Both Gemini and SerpAPI keys must be configured</li>
  <li>🌐 <b>Internet Connection:</b> Required for web scraping and API calls</li>
  <li>⏱️ <b>Rate Limits:</b> Respect SerpAPI usage limits (free tier: 100 searches/month)</li>
  <li>🎭 <b>Playwright:</b> Requires browser installation via <code>playwright install</code></li>
  <li>💻 <b>Windows Users:</b> Uses WindowsProactorEventLoopPolicy for async support</li>
  <li>📝 <b>JSON Format:</b> Input files must follow exact structure</li>
</ul>

<hr>

<h2>🐛 Troubleshooting</h2>

<h3>Issue: "API Key not found"</h3>
<pre><code># Solution: Check .env file exists and contains:
GEMINI_API_KEY=your_key_here
SERP_API_KEY=your_key_here
</code></pre>

<h3>Issue: "Playwright browser not found"</h3>
<pre><code># Solution: Install Playwright browsers
playwright install
</code></pre>

<h3>Issue: "Scraping timeout"</h3>
<pre><code># Solution: Some websites may block scraping
# The system includes fallback logic to use general knowledge
# You can adjust timeout in the code (default: 30000ms)
</code></pre>

<h3>Issue: "JSON parsing error"</h3>
<pre><code># Solution: The system includes fallback to raw text
# Check output_json for "raw_output" field
# May indicate Gemini returned non-JSON response
</code></pre>

<hr>

<h2>🔮 Future Enhancements</h2>

<ul>
  <li>🎨 <b>Web UI:</b> Flask/Streamlit dashboard for easy interaction</li>
  <li>📊 <b>Analytics:</b> Track preparation progress and completion</li>
  <li>🔔 <b>Notifications:</b> Email/Slack alerts for roadmap generation</li>
  <li>💾 <b>Database Integration:</b> Store historical roadmaps in MongoDB/PostgreSQL</li>
  <li>🤝 <b>Collaborative Features:</b> Share roadmaps with peers</li>
  <li>📱 <b>Mobile App:</b> React Native app for on-the-go access</li>
  <li>🧠 <b>Advanced AI:</b> Fine-tune models on interview success patterns</li>
  <li>📈 <b>Progress Tracking:</b> Integrated study tracker with deadlines</li>
  <li>🔄 <b>Auto-Update:</b> Periodic re-scraping for latest interview trends</li>
</ul>

<hr>

<h2>🎓 Learning Outcomes</h2>

<p>This project demonstrates proficiency in:</p>

<ul>
  <li>🤖 <b>Multi-Agent AI Systems:</b> Orchestrated workflow with specialized agents</li>
  <li>🧠 <b>Large Language Models:</b> Prompt engineering and response parsing</li>
  <li>🌐 <b>Web Scraping:</b> Async scraping with Playwright</li>
  <li>🔍 <b>API Integration:</b> SerpAPI and Gemini API usage</li>
  <li>📊 <b>Data Structuring:</b> JSON schema design and validation</li>
  <li>⚡ <b>Async Programming:</b> Concurrent operations in Python</li>
  <li>🛡️ <b>Error Handling:</b> Robust exception management</li>
  <li>📁 <b>File I/O:</b> JSON reading, writing, and parsing</li>
</ul>

<hr>

<h2>📚 References & Resources</h2>

<ul>
  <li>🔗 <b>Google Gemini API:</b> <a href="https://ai.google.dev/">ai.google.dev</a></li>
  <li>🔗 <b>SerpAPI Documentation:</b> <a href="https://serpapi.com/search-api">serpapi.com/search-api</a></li>
  <li>🔗 <b>Playwright Python:</b> <a href="https://playwright.dev/python/">playwright.dev/python</a></li>
  <li>🔗 <b>Async Python:</b> <a href="https://docs.python.org/3/library/asyncio.html">docs.python.org/asyncio</a></li>
</ul>

<h2>⚖️ License</h2>

<p>
This project is open source and available for educational purposes. Please respect API rate limits and terms of service for all integrated platforms.
</p>

<hr>

<h2>👨‍💻 Author</h2>

<p align="center">
  <b>Prayash Ranjan Mohanty</b><br>
  AI/ML Enthusiast | Full Stack Developer<br>
  📧 <a href="mailto:prayashranjanmohanty11@gmail.com">prayashranjanmohanty11@gmail.com</a>
</p>

<p align="center">
  <a href="https://github.com/PrayashRM">
    <img src="https://img.shields.io/badge/GitHub-PrayashRM-black?logo=github&style=for-the-badge" alt="GitHub">
  </a>
  <a href="https://www.linkedin.com/in/prayash-mohanty-209303382">
    <img src="https://img.shields.io/badge/LinkedIn-Prayash_Mohanty-blue?logo=linkedin&style=for-the-badge" alt="LinkedIn">
  </a>
</p>

<hr>

<h2>🙏 Acknowledgments</h2>

<ul>
  <li>🤖 <b>Google:</b> For the powerful Gemini 2.5 Flash API</li>
  <li>🔍 <b>SerpAPI:</b> For reliable Google search integration</li>
  <li>🎭 <b>Playwright Team:</b> For the excellent web automation framework</li>
  <li>💡 <b>Interview Platforms:</b> Glassdoor, LeetCode, GeeksforGeeks, and others for hosting valuable interview insights</li>
  <li>🌟 <b>Open Source Community:</b> For inspiration and continuous learning</li>
</ul>

<hr>

<p align="center">
  <b>⭐ If you found this project helpful, please give it a star! ⭐</b><br>
  <i>"Preparation is the key to success." - Alexander Graham Bell</i><br><br>
  <i>Built with 🤖 using Python, Gemini AI, and Playwright | © 2024 Prayash Ranjan Mohanty</i>
</p>

</body>
</html>
