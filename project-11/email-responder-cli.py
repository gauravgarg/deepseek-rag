import requests

# DeepSeek API URL
OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_email_response(email_content, tone="Formal"):
    """
    Uses DeepSeek AI to generate an appropriate email response.
    """
    prompt = f"Generate an {tone} email as a response from the cutomer support team to the customer for the following email:\n\n{email_content}\n\n" \
             "Ensure the response is polite, clear, and professional."

    # prompt = f"Write an email response in {language}:\n\n{email_content}"

    payload = {
        "model": "deepseek-r1",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code == 200:
        return response.json().get("response", "No response generated.")
    else:
        return f"Error: {response.text}"

# # Test AI Email Responder
if __name__ == "__main__":
    test_email = "I need help with my order."
    print("### AI-Generated Email Response ###")
    print(generate_email_response(test_email))
