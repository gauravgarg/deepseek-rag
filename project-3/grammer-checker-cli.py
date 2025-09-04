import requests

# DeepSeek API URL
OLLAMA_URL = "http://localhost:11434/api/generate"

def correct_grammar(text):
    """
    Uses DeepSeek AI to correct grammar and spelling errors in the given text.
    """
    prompt = f"Correct any spelling and grammar mistakes in the following text and provide explanations:\n\n{text}"

    payload = {
        "model": "deepseek-r1",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code == 200:
        return response.json().get("response", "No correction generated.")
    else:
        return f"Error: {response.text}"

# # Test Grammar Correction
if __name__ == "__main__":
    sample_text = "He dont like to eat apple because they taste sour."
    print("### Corrected Text ###")
    print(correct_grammar(sample_text))
