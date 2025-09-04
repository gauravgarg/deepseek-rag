## ✨ Why Use AI for Grammar and Spell Checking?

- 📝 **Fixes Spelling Mistakes** – Detects and corrects typos instantly.  
- 📚 **Improves Sentence Structure** – Suggests better phrasing and grammar.  
- 🔍 **Enhances Writing Clarity** – Makes text easier to read and understand.  
- ⏳ **Saves Time** – Automates proofreading to speed up the writing process.  

---

## 📌 Common Use Cases of AI Grammar & Spell Checking

- 📖 **Editing Essays, Reports, and Blogs** – Ensure content is polished and error-free.  
- 📧 **Proofreading Emails** – Check tone, grammar, and spelling before sending.  
- 📰 **News Articles** – Maintain accuracy and professionalism in published content.  
- 📑 **Official Documents** – Correct grammar and spelling in contracts, letters, and policies.  

## ⚙️ How AI-Based Grammar and Spell Checking Works

**Example: Basic Grammar Correction**  

- 📝 **Input Text:**  
  *The dog run fast to catch the frisbee, but he miss it.*  

- 🤖 **AI-Corrected Output:**  
  *The dog ran fast to catch the frisbee, but he missed it.*

---

## How to Run the Project Files

### 1. Run the FastAPI Server (API)
From the `project-3` directory, run:
```sh
uvicorn grammer-checker-api:app --reload
```
- The API will be available at: http://127.0.0.1:8000
- The `/correct/` endpoint accepts POST requests with a `text` string.

### 2. Run the CLI Script
Run:
```sh
python grammer-checker-cli.py
```
- This will correct grammar and spelling in the terminal using your input text.

### 3. Run the Web App
Run:
```sh
python grammer-checker-web.py
```
- This will launch the Gradio web interface in your browser for interactive grammar and spell checking.

---

Refer to the Project 1 README for environment setup and dependency installation.
