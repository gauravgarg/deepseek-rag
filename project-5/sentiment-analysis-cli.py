import requests

# DeepSeek API URL
OLLAMA_URL = "http://localhost:11434/api/generate"

def analyze_sentiment(text, language="Engligh"):
    """
    Uses DeepSeek AI to classify sentiment as positive, negative, or neutral.
    """
    # prompt = f"Classify the sentiment of the following text as Positive, Negative, or Neutral:\n\n{text}"
    # prompt = f"Analyze the sentiment of this text. Provide a sentiment score from -1 (very negative) to +1 (very positive):\n\n{text}"
    # prompt = f"Classify the sentiment of this text (in {language}) as Positive, Negative, or Neutral:\n\n{text}"
    prompt = f"Identify sentiment in the following text and highlight words that contribute to it:\n\n{text}"

    payload = {
        "model": "deepseek-r1",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code == 200:
        return response.json().get("response", "No sentiment detected.")
    else:
        return f"Error: {response.text}"

# # Test Sentiment Analysis
if __name__ == "__main__":
    # sample_text = "The movie was absolutely fantastic! I enjoyed every minute of it."
    sample_text = "The service was terrible. I waited an hour, and my order was wrong."
    print("### Sentiment Analysis Result ###")
    print(analyze_sentiment(sample_text))
