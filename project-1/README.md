## 📌 Use Cases of AI-Powered Text Summarization

- 📰 **News Summarization** – Quickly extract key highlights from lengthy news articles.  
- ⚖️ **Legal Document Summarization** – Simplify complex legal texts into concise summaries.  
- 🏥 **Medical Report Summarization** – Help doctors and patients understand critical details faster.  
- 📊 **Business Reports & Research Papers** – Condense data-heavy documents into actionable insights.  
- ✍️ **Content Summarization** – Summarize blogs, articles, or any long-form content for easy consumption.  


# Project 1: Text Summarizer

## Setup Instructions

Follow these steps to set up your Python environment and install dependencies for this project:

### 1. Create a Virtual Environment

Open your terminal and run:

```sh
python3 -m venv prj1-venv
```

This will create a virtual environment named `prj1-venv` inside the `project-1` folder.

### 2. Activate the Virtual Environment

On macOS/Linux:

```sh
source prj1-venv/bin/activate
```

On Windows:

```sh
prj1-venv\Scripts\activate
```

### 3. Install Dependencies

With the virtual environment activated, run:

```sh
pip3 install -r requirement.txt
```

This will install all required packages listed in `requirement.txt`.

### 4. Deactivate the Virtual Environment

When you are done working, you can deactivate the environment by running:

```sh
deactivate
```

---

**Note:** Always activate the virtual environment before running any Python scripts for this project.

## How to Run Each File

### 1. Run the FastAPI Server (API)
From the `project-1` directory, activate your virtual environment and run:
```sh
source prj1-venv/bin/activate
uvicorn text-summarizer-api:app --reload
```
- The API will be available at: http://127.0.0.1:8000
- The `/summarize/` endpoint accepts POST requests with a text string.

### 2. Run the CLI Script
Activate your virtual environment and run:
```sh
python text-summarizer-cli.py
```

### 3. Run the Web App
Activate your virtual environment and run:
```sh
python text-summarizer-web.py
```
- This will launch the Gradio web interface in your browser.
