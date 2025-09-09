# DeepSeek RAG: AI-Powered Tools

This repository contains multiple AI-powered projects for text summarization, text generation, and grammar/spell checking. Each project is self-contained and can be run independently.

## Repository Structure

- `project-1`: Text Summarizer
- `project-2`: Text Generator
- `project-3`: Grammar & Spell Checker


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
