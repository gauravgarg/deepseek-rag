import requests
import pandas as pd


# # Store feedback analysis in a DataFrame
# feedback_data = 
pd.DataFrame(columns=["Feedback", "Sentiment", "Key Issues", "Suggested Action"])


# DeepSeek API URL
OLLAMA_URL = "http://localhost:11434/api/generate"

def analyze_feedback(feedback_text):
    """
    Uses DeepSeek AI to analyze customer feedback and extract insights.
    """
    prompt = f"Analyze the following customer feedback:\n\n{feedback_text}\n\n" \
             "Provide sentiment analysis (positive, neutral, negative), key themes, and actionable insights."

    # prompt = f"Analyze the customer feedback and classify it into categories like Product, Service, Price, Delivery:\n\n{feedback_text}"

    payload = {
        "model": "deepseek-r1",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code == 200:
        return response.json().get("response", "No insights generated.")
    else:
        return f"Error: {response.text}"


# # Test AI Feedback Analyzer
if __name__ == "__main__":
    test_feedback = "I love the laptop's performance, but the keyboard feels cheap."
    print("### AI Feedback Analysis ###")
    print(analyze_feedback(test_feedback))
