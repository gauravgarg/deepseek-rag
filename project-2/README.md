## 🤖 Why Use AI for Text Generation?

- ⏳ **Saves Time** – Automates repetitive writing tasks.  
- 🎨 **Boosts Creativity** – Generates fresh ideas and unique content styles.  
- 📈 **Improves Productivity** – Speeds up content creation for individuals and teams.  
- ⚙️ **Customizable Output** – Adjusts tone, style, and length as per requirements.  

---

## 📌 Common Use Cases of AI Text Generation

- ✍️ **Blog Writing** – Draft engaging blog posts and articles quickly.  
- 📧 **Email Writing** – Create professional, personalized emails in seconds.  
- 🛍️ **Product Descriptions** – Generate SEO-friendly and attractive product listings.  
- 📖 **AI Storytelling** – Build creative stories, dialogues, and narratives.  
- 💬 **Chatbot Conversations** – Power conversational AI with natural, human-like responses.

---

## How to Run the Project Files

### 1. Run the FastAPI Server (API)
From the `project-2` directory, run:
```sh
uvicorn text-generator-api:app --reload
```
- The API will be available at: http://127.0.0.1:8000
- The `/generate/` endpoint accepts POST requests with a `prompt` string and optional `word_limit`.

### 2. Run the CLI Script
Run:
```sh
python text-generator-cli.py
```
- This will generate text in the terminal using your prompt.

### 3. Run the Web App
Run:
```sh
python text-generator-web.py
```
- This will launch the Gradio web interface in your browser for interactive text generation.

---

Refer to the Project 1 README for environment setup and dependency installation.
