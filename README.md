# 🔬 ResearchMind – Multi-Agent Research AI System

ResearchMind is an AI-powered multi-agent research assistant that automates the complete research workflow using multiple specialized AI agents. It searches the web, extracts relevant information, generates a structured research report, and critically evaluates the final output.

Built using **LangChain**, **LangGraph**, **Mistral AI**, **Streamlit**, and custom research tools.

---

## 🚀 Features

- 🔍 **Search Agent**
  - Searches the web for reliable and recent information.
  - Collects relevant URLs and summaries.

- 📄 **Reader Agent**
  - Scrapes the selected webpages.
  - Extracts detailed and meaningful content.

- ✍️ **Writer Chain**
  - Generates a well-structured research report.
  - Includes:
    - Introduction
    - Key Findings
    - Conclusion
    - Sources

- 🧐 **Critic Chain**
  - Reviews the generated report.
  - Assigns a score.
  - Highlights strengths and improvement areas.

- 🎨 Modern Streamlit dashboard
- 📊 Real-time pipeline progress
- 📝 Live execution logs
- 🌙 Responsive dark theme UI

---

## 🛠 Tech Stack

- Python
- Streamlit
- LangChain
- LangGraph
- Mistral AI
- BeautifulSoup4
- Requests
- Python Dotenv

---

## 📂 Project Structure

```
Multi-Agent Research AI System/
│
├── app.py                 # Streamlit UI
├── agents.py              # AI agents and chains
├── pipeline.py            # Research pipeline
├── tools.py               # Web search & scraping tools
├── requirements.txt
├── .env
├── README.md
└── assets/
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/multi-agent-research-ai.git
```

Move into the project

```bash
cd multi-agent-research-ai
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file.

```env
MISTRAL_API_KEY=your_mistral_api_key
```

---

## ▶️ Run the Project

```bash
streamlit run app.py
```

The application will open at

```
http://localhost:8501
```

---

## 🔄 Workflow

```
User Topic
      │
      ▼
Search Agent
      │
      ▼
Reader Agent
      │
      ▼
Writer Chain
      │
      ▼
Critic Chain
      │
      ▼
Final Research Report
```

---

## 📸 Application Preview

The application includes:

- Interactive research dashboard
- AI pipeline visualization
- Live execution logs
- Search results
- Scraped content
- Final research report
- Critic feedback panel

*(Add screenshots here)*

---

## 📈 Future Improvements

- PDF export
- Citation generation
- Multi-source comparison
- Research history
- Chat with generated report
- Parallel agent execution
- Vector database integration
- RAG support
- Streaming responses

---

## 👩‍💻 Author

**Saloni Kumari**

B.Tech CSE (AI & ML)

GitHub: https://github.com/Saloni468kumari

LinkedIn: https://linkedin.com/in/saloni-singh-8a1808253

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and feel free to contribute.
