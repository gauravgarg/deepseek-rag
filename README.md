# DeepSeek RAG: AI-Powered Tools

This repository contains multiple AI-powered projects for text summarization, text generation, and grammar/spell checking. Each project is self-contained and can be run independently.


## Repository Structure

- `project-1`: Text Summarizer
- `project-2`: Text Generator
- `project-3`: Grammar & Spell Checker
- `project-4`: NER Extractor
- `project-5`: Sentiment Analysis
- `project-6`: Customer Support Bot
- `project-7`: AI Assistant
- `project-8`: Legal Assistant
- `project-9`: Symptom Checker
- `project-10`: Product Recommender
- `project-11`: Email Responder
- `project-12`: Resume Generator
- `project-13`: Meeting Minutes Generator
- `project-14`: PDF Text Extractor
- `project-15`: Content Writer
- `project-16`: Code Autocompleter
- `project-17`: SQL Query Generator
- `project-18`: Code Debugger
- `project-19`: Code Documenter
- `project-20`: API Tester
- `project-21`: Feedback Analyzer
- `project-22`: News Summarizer
- `project-23`: Financial Analyzer
- `project-24`: Job Screener
- `project-25`: Paper Summarizer

## Installation Steps


### 1. Python Setup

Make sure you have Python 3.8+ installed. You can check your version with:
```sh
python3 --version
```

#### Install Python

- **macOS:**
  - Recommended: Install Homebrew from [https://brew.sh/](https://brew.sh/)
  - Then run:
    ```sh
    brew install python
    ```
  - Or download the official installer from [https://www.python.org/downloads/](https://www.python.org/downloads/)

- **Windows:**
  - Download the installer from [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)
  - Run the installer and check "Add Python to PATH" during installation.

- **Linux (Debian/Ubuntu):**
  - Run:
    ```sh
    sudo apt update
    sudo apt install python3 python3-venv python3-pip
    ```

#### Create a Virtual Environment
It is recommended to use a virtual environment for each project:
```sh
python3 -m venv prj1-venv
source prj1-venv/bin/activate
```

#### Install Dependencies
```sh
pip install -r requirement.txt
```

### 2. Ollama Installation

Download and install Ollama from [https://ollama.com/](https://ollama.com/).
Start Ollama locally:
```sh
ollama serve
```
Ollama should be running at [http://localhost:11434/](http://localhost:11434/).

### 3. Model Setup

Pull the required model (e.g., DeepSeek) using Ollama:
```sh
ollama pull deepseek-r1
```
You can pull other models as needed. See Ollama documentation for more options.

---

## Quick Start

1. **Clone the repository:**
  ```sh
  git clone <your-repo-url>
  cd deepseek-rag
  ```
2. **Environment Setup:**
  - Each project has its own `README.md` with setup and run instructions.
  - Follow the environment setup steps in `project-1/README.md` (recommended for all projects).


## Project Overviews & Usage

### 1. Text Summarizer (`project-1`)
- **Purpose:** Summarize long-form content, news, legal, medical, and business documents.
- **How to Run:**
  - API: `uvicorn text-summarizer-api:app --reload`
  - CLI: `python text-summarizer-cli.py`
  - Web: `python text-summarizer-web.py`
- See [project-1/README.md](project-1/README.md) for details.

### 2. Text Generator (`project-2`)
- **Purpose:** Generate creative, professional, or SEO-friendly text for blogs, emails, product descriptions, stories, and chatbots.
- **How to Run:**
  - API: `uvicorn text-generator-api:app --reload`
  - CLI: `python text-generator-cli.py`
  - Web: `python text-generator-web.py`
- See [project-2/README.md](project-2/README.md) for details.

### 3. Grammar & Spell Checker (`project-3`)
- **Purpose:** Correct grammar and spelling in essays, emails, news articles, and official documents.
- **How to Run:**
  - API: `uvicorn grammer-checker-api:app --reload`
  - CLI: `python grammer-checker-cli.py`
  - Web: `python grammer-checker-web.py`
- See [project-3/README.md](project-3/README.md) for details.

### 4. NER Extractor (`project-4`)
- **Purpose:** Extract named entities (person, organization, location, etc.) from text for information retrieval, knowledge graphs, and data analysis.
- **How to Run:**
  - API: `uvicorn ner-extractor-api:app --reload`
  - CLI: `python ner-extractor-cli.py`
  - Web: `python ner-extractor-web.py`
- See [project-4/README.md](project-4/README.md) for details.

### 5. Sentiment Analysis (`project-5`)
- **Purpose:** Sentiment analysis captures customer emotions, tracks public opinion, supports better decisions, and automates large-scale text analysis.
- **How to Run:**
  - API: `uvicorn sentiment-analysis-api:app --reload`
  - CLI: `python sentiment-analysis-cli.py`
  - Web: `python sentiment-analysis-web.py`
- See [project-5/README.md](project-5/README.md) for details.

### 6. Customer Support Bot (`project-6`)
- **Purpose:** AI-powered customer support automation for chat, email, and web.
- **How to Run:**
  - API: `uvicorn customer-support-bot-api:app --reload`
  - CLI: `python customer-support-bot-cli.py`
  - Web: `python customer-support-bot-web.py`
- See [project-6/README.md](project-6/README.md) for details.

### 7. AI Assistant (`project-7`)
- **Purpose:** General-purpose AI assistant for productivity and automation.
- **How to Run:**
  - API: `uvicorn ai-assistant-api:app --reload`
  - CLI: `python ai-assistant-cli.py`
  - Web: `python ai-assistant-web.py`
- See [project-7/README.md](project-7/README.md) for details.

### 8. Legal Assistant (`project-8`)
- **Purpose:** Automate legal document review and legal queries.
- **How to Run:**
  - API: `uvicorn legal-assistant-api:app --reload`
  - CLI: `python legal-assistant-cli.py`
  - Web: `python legal-assistant-web.py`
- See [project-8/README.md](project-8/README.md) for details.

### 9. Symptom Checker (`project-9`)
- **Purpose:** AI-based health symptom checker and triage tool.
- **How to Run:**
  - API: `uvicorn symptom-checker-api:app --reload`
  - CLI: `python symptom-checker-cli.py`
  - Web: `python symptom-checker-web.py`
- See [project-9/README.md](project-9/README.md) for details.

### 10. Product Recommender (`project-10`)
- **Purpose:** Recommend products based on user preferences and history.
- **How to Run:**
  - API: `uvicorn product-recommender-api:app --reload`
  - CLI: `python product-recommender-cli.py`
  - Web: `python product-recommender-web.py`
- See [project-10/README.md](project-10/README.md) for details.

### 11. Email Responder (`project-11`)
- **Purpose:** Automate email replies and customer communication.
- **How to Run:**
  - API: `uvicorn email-responder-api:app --reload`
  - CLI: `python email-responder-cli.py`
  - Web: `python email-responder-web.py`
- See [project-11/README.md](project-11/README.md) for details.

### 12. Resume Generator (`project-12`)
- **Purpose:** Generate professional resumes from user input.
- **How to Run:**
  - API: `uvicorn resume-generator-api:app --reload`
  - CLI: `python resume-generator-cli.py`
  - Web: `python resume-generator-web.py`
- See [project-12/README.md](project-12/README.md) for details.

### 13. Meeting Minutes Generator (`project-13`)
- **Purpose:** Create meeting minutes from transcripts or notes.
- **How to Run:**
  - API: `uvicorn meeting-minutes-api:app --reload`
  - CLI: `python meeting-minutes-cli.py`
  - Web: `python meeting-minutes-web.py`
- See [project-13/README.md](project-13/README.md) for details.

### 14. PDF Text Extractor (`project-14`)
- **Purpose:** Extract text from PDF documents for analysis or search.
- **How to Run:**
  - API: `uvicorn pdf-text-extractor-api:app --reload`
  - CLI: `python pdf-text-extractor-cli.py`
  - Web: `python pdf-text-extractor-web.py`
- See [project-14/README.md](project-14/README.md) for details.

### 15. Content Writer (`project-15`)
- **Purpose:** Generate articles, blog posts, and marketing content.
- **How to Run:**
  - API: `uvicorn content-writer-api:app --reload`
  - CLI: `python content-writer-cli.py`
  - Web: `python content-writer-web.py`
- See [project-15/README.md](project-15/README.md) for details.

### 16. Code Autocompleter (`project-16`)
- **Purpose:** AI-powered code completion for developers.
- **How to Run:**
  - API: `uvicorn code-autocompleter-api:app --reload`
  - CLI: `python code-autocompleter-cli.py`
  - Web: `python code-autocompleter-web.py`
- See [project-16/README.md](project-16/README.md) for details.

### 17. SQL Query Generator (`project-17`)
- **Purpose:** Generate SQL queries from natural language prompts.
- **How to Run:**
  - API: `uvicorn sql-query-generator-api:app --reload`
  - CLI: `python sql-query-generator-cli.py`
  - Web: `python sql-query-generator-web.py`
- See [project-17/README.md](project-17/README.md) for details.

### 18. Code Debugger (`project-18`)
- **Purpose:** Assist with debugging code and finding errors.
- **How to Run:**
  - API: `uvicorn code-debugger-api:app --reload`
  - CLI: `python code-debugger-cli.py`
  - Web: `python code-debugger-web.py`
- See [project-18/README.md](project-18/README.md) for details.

### 19. Code Documenter (`project-19`)
- **Purpose:** Automatically generate documentation for codebases.
- **How to Run:**
  - API: `uvicorn code-documenter-api:app --reload`
  - CLI: `python code-documenter-cli.py`
  - Web: `python code-documenter-web.py`
- See [project-19/README.md](project-19/README.md) for details.

### 20. API Tester (`project-20`)
- **Purpose:** Test and validate APIs with automated tools.
- **How to Run:**
  - CLI: `python api-tester-cli.py`
  - Web: `python api-tester-web.py`
- See [project-20/README.md](project-20/README.md) for details.

### 21. Feedback Analyzer (`project-21`)
- **Purpose:** Analyze customer feedback for insights and trends.
- **How to Run:**
  - API: `uvicorn feedback-analyzer-api:app --reload`
  - CLI: `python feedback-analyzer-cli.py`
  - Web: `python feedback-analyzer-web.py`
- See [project-21/README.md](project-21/README.md) for details.

### 22. News Summarizer (`project-22`)
- **Purpose:** Summarize news articles and headlines using AI.
- **How to Run:**
  - CLI: `python news-summarizer-cli.py`
  - Web: `python news-summarizer-web.py`
- See [project-22/README.md](project-22/README.md) for details.

### 23. Financial Analyzer (`project-23`)
- **Purpose:** Analyze financial data and generate reports.
- **How to Run:**
  - API: `uvicorn financial-analyzer-api:app --reload`
  - CLI: `python financial-analyzer-cli.py`
  - Web: `python financial-analyzer-web.py`
- See [project-23/README.md](project-23/README.md) for details.

### 24. Job Screener (`project-24`)
- **Purpose:** Screen job applications and resumes using AI.
- **How to Run:**
  - API: `uvicorn job-screener-api:app --reload`
  - CLI: `python job-screener-cli.py`
  - Web: `python job-screener-web.py`
- See [project-24/README.md](project-24/README.md) for details.

### 25. Paper Summarizer (`project-25`)
- **Purpose:** Summarize academic papers and research articles.
- **How to Run:**
  - API: `uvicorn paper-summarizer-api:app --reload`
  - CLI: `python paper-summarizer-cli.py`
  - Web: `python paper-summarizer-web.py`
- See [project-25/README.md](project-25/README.md) for details.

## How to Navigate

- Each subproject folder contains its own code, requirements, and documentation.
- Start with the README in each project for specific instructions.
- Shared environment setup and dependency installation are described in `project-1/README.md`.

## Contributing

Feel free to open issues or pull requests for improvements, bug fixes, or new features.

## Acknowledgments

This repository is based on code and concepts from the Udemy course "DeepSeek R1: Real-World Projects" by Vivian Aranha.
