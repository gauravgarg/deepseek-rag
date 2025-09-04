import requests

# DeepSeek API URL
OLLAMA_URL = "http://localhost:11434/api/generate"

def extract_named_entities(text):
    """
    Uses DeepSeek AI to identify named entities (people, organizations, locations, dates).
    """
    prompt = f"Extract all named entities (persons, organizations, locations, dates) from the following text:\n\n{text}"
    # prompt = f"Extract persons, organizations, locations, dates, and job titles from this French-language text:\n\n{text}"

    payload = {
        "model": "deepseek-r1",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code == 200:
        return response.json().get("response", "No entities detected.")
    else:
        return f"Error: {response.text}"

# # Test Named Entity Recognition
if __name__ == "__main__":
    sample_text = "Google was founded by Larry Page and Sergey Brin in September 1998 at Stanford University."
    print("### Extracted Entities ###")
    print(extract_named_entities(sample_text))
