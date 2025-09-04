# DeepSeek RAG: AI-Powered Tools

This repository contains multiple AI-powered projects for text summarization, text generation, and grammar/spell checking. Each project is self-contained and can be run independently.

## Repository Structure

- `project-1`: Text Summarizer
- `project-2`: Text Generator
- `project-3`: Grammar & Spell Checker

## Quick Start

1. **Clone the repository:**
   ```sh
git clone <your-repo-url>
cd deepseek-rag
```
2. **Environment Setup:**
   - Each project has its own `README.md` with setup and run instructions.
   - Follow the environment setup steps in `project-1/README.md` (recommended for all projects).

## Prerequisite

To run any project in this repository, you must have Ollama running locally. Download and start Ollama from [https://ollama.com/](https://ollama.com/) and ensure it is running at [http://localhost:11434/](http://localhost:11434/) before launching any API, CLI, or web app.

## Project Overviews & Usage

### 1. Text Summarizer (`project-1`)
- **Purpose:** Summarize long-form content, news, legal, medical, and business documents.
- **How to Run:**
  - API: `uvicorn text-summarizer-api:app --reload`
  - CLI: `python text-summarizer-cli.py`
  - Web: `python text-summarizer-web.py`
- See `project-1/README.md` for details.

### 2. Text Generator (`project-2`)
- **Purpose:** Generate creative, professional, or SEO-friendly text for blogs, emails, product descriptions, stories, and chatbots.
- **How to Run:**
  - API: `uvicorn text-generator-api:app --reload`
  - CLI: `python text-generator-cli.py`
  - Web: `python text-generator-web.py`
- See `project-2/README.md` for details.

### 3. Grammar & Spell Checker (`project-3`)
- **Purpose:** Correct grammar and spelling in essays, emails, news articles, and official documents.
- **How to Run:**
  - API: `uvicorn grammer-checker-api:app --reload`
  - CLI: `python grammer-checker-cli.py`
  - Web: `python grammer-checker-web.py`
- See `project-3/README.md` for details.

## How to Navigate

- Each subproject folder contains its own code, requirements, and documentation.
- Start with the README in each project for specific instructions.
- Shared environment setup and dependency installation are described in `project-1/README.md`.

## Contributing

Feel free to open issues or pull requests for improvements, bug fixes, or new features.

## Acknowledgments

This repository is based on code and concepts from the Udemy course "DeepSeek R1: Real-World Projects" by Vivian Aranha.
