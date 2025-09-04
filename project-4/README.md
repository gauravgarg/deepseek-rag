## 🏷️ Why Use AI for Named Entity Recognition (NER)?

- ⚙️ **Automates Data Extraction** – Identifies key information without manual effort.  
- 🔎 **Improves Searchability** – Makes documents easier to organize and retrieve.  
- 📊 **Enables Better Analysis** – Helps uncover patterns and insights from text data.  
- ⏱️ **Speeds Up Data Processing** – Processes large volumes of text quickly and efficiently.  

---

## 📌 Common Use Cases of AI-Powered NER

- 🏢 **Financial Reports** – Extract company names and financial entities.  
- 🏥 **Medical Records** – Identify diseases, treatments, and medications.  
- ⚖️ **Legal Contracts** – Find case laws, clauses, and legal references.  
- 📰 **News Articles** – Extract people, organizations, and locations automatically.  

## ⚙️ How Named Entity Recognition (NER) Works

**Example: Extracting Entities from Text**  

- 📝 **Input Text:**  
  *Elon Musk is the CEO of Tesla and SpaceX, headquartered in California. He was born in Pretoria, South Africa, in 1971.*  

- 🤖 **AI-Extracted Entities:**  
  - **Person:** Elon Musk  
  - **Organization:** Tesla, SpaceX  
  - **Location:** California, Pretoria, South Africa  
  - **Date:** 1971

---

## How to Run the Project Files

### 1. Run the FastAPI Server (API)
From the `project-4` directory, run:
```sh
uvicorn ner-extractor-api:app --reload
```
- The API will be available at: http://127.0.0.1:8000
- The `/extract/` endpoint accepts POST requests with a `text` string.

### 2. Run the CLI Script
Run:
```sh
python ner-extractor-cli.py
```
- This will extract named entities in the terminal using your input text.

### 3. Run the Web App
Run:
```sh
python ner-extractor-web.py
```
- This will launch the Gradio web interface in your browser for interactive entity extraction.

---

Refer to the Project 1 README for environment setup and dependency installation.
