import requests

# DeepSeek API URL
OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_sql_query(natural_query, database_type="MySQL", database_schema="employee(name, salary, department)"):
    """
    Uses DeepSeek AI to convert a natural language query into an SQL statement.
    """
    # prompt = f"Optimize the following SQL query for better performance:\n\n{sql_query}\n\n" \
             # f"Suggest indexing strategies if necessary."

    prompt = f"Convert this natural language query into {database_type}-compatible SQL:\n\nQuery: {natural_query}"


    prompt = f"Convert the following natural language query into an SQL query:\n\n" \
             f"Query: '{natural_query}'\n\n" \
             f"Assume the following database schema: {database_schema}.\n" \
             f"Return only the SQL query, without explanation."

    payload = {
        "model": "deepseek-r1",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code == 200:
        return response.json().get("response", "No SQL query generated.")
    else:
        return f"Error: {response.text}"

# # Test SQL Query Generator
if __name__ == "__main__":
    test_query = "List all employees in the Sales department."
    print("### AI-Generated SQL Query ###")
    print(generate_sql_query(test_query))


