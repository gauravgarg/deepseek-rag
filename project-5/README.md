## 😊 Why Use AI for Sentiment Analysis?

- 💬 **Understands Customer Feedback** – Captures emotions and opinions from text.  
- 🌍 **Tracks Public Opinion** – Monitors how people feel about topics, brands, or events.  
- 📊 **Enhances Decision Making** – Provides data-driven insights for strategy.  
- ⚡ **Automates Analysis** – Quickly processes large volumes of text data.  

---

## 📌 Common Use Cases of AI-Powered Sentiment Analysis

- 📱 **Social Media Monitoring** – Analyze comments and posts for brand sentiment.  
- ⭐ **Customer Reviews** – Extract emotions from reviews on platforms like Amazon or Yelp.  
- 📰 **Financial Markets** – Assess sentiment in news articles that may impact stocks.  
- 👩‍💼 **HR Feedback** – Monitor employee satisfaction from surveys and feedback forms.  

## ⚙️ How Sentiment Analysis Works

**Example: Sentiment Classification**  

- 📝 **Input Text:**  
  *I love this product! It works perfectly and exceeded my expectations.*  

- 🤖 **AI-Detected Sentiment:**  
  ✅ **Positive**

---

## How to Run the Project Files

### 1. Run the FastAPI Server (API)
From the `project-5` directory, run:
```sh
uvicorn sentiment-analysis-api:app --reload
```
- The API will be available at: http://127.0.0.1:8000
- The `/analyze/` endpoint accepts POST requests with a `text` string.

### 2. Run the CLI Script
Run:
```sh
python sentiment-analysis-cli.py
```
- This will analyze sentiment in the terminal using your input text.

### 3. Run the Web App
Run:
```sh
python sentiment-analysis-web.py
```
- This will launch the Gradio web interface in your browser for interactive sentiment analysis.

---

Refer to the Project 1 README for environment setup and dependency installation.
