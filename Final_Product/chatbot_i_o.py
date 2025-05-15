from neo4j import GraphDatabase
import requests
import re

# Neo4j Connection Configuration
URI = "neo4j://localhost:7687"  # Neo4j server URI
USERNAME = "neo4j"  # Neo4j username
PASSWORD = "jaajijaaji"  # Neo4j password (replace with your actual password)

# Initialize Neo4j driver
try:
    driver = GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD))
except Exception as e:
    print(f"Failed to initialize Neo4j driver: {e}")
    driver = None

# DeepSeek R1 API Configuration
DEEPSEEK_R1_API = "http://localhost:1234/v1/chat/completions"  # DeepSeek R1 API endpoint

# Full-Text Search in Neo4j
def search_full_text(tx, user_query):
    """
    Perform a full-text search in Neo4j using the specified query.

    Args:
        tx: Neo4j transaction object.
        user_query (str): The search query provided by the user.

    Returns:
        list: A list of dictionaries containing filename and content of the matched nodes.
    """
    try:
        result = tx.run("""
            CALL db.index.fulltext.queryNodes('chunkIndex', $query) 
            YIELD node, score 
            RETURN node.filename AS filename, node.content AS content, score 
            ORDER BY score DESC LIMIT 5
        """, {"query": user_query})

        return [{"filename": record["filename"], "content": record["content"]} for record in result]
    except Exception as e:
        print(f"Error executing Neo4j query: {e}")
        return []

# Query LLM (Large Language Model)
def query_llm(context, question):
    """
    Query the DeepSeek R1 API with the provided context and question.

    Args:
        context (str): The context retrieved from Neo4j.
        question (str): The user's question.

    Returns:
        str: The response from the LLM.
    """
    payload = {
        "model": "deepseek-r1-distill-qwen-7b",
        "messages": [
            {"role": "system", "content": "Answer based on the provided documentation."},
            {"role": "user", "content": f"{question}\n\nContext:\n{context}"}
        ],
        "temperature": 0.2,
        "max_tokens": 1024,
        "stream": False
    }

    try:
        response = requests.post(DEEPSEEK_R1_API, json=payload)
        response.raise_for_status()  # Raise an error for bad status codes
        raw_response = response.json()["choices"][0]["message"]["content"]
        # Remove <think> tags if they exist
        cleaned_response = re.sub(r"<think>.*?</think>", "", raw_response, flags=re.DOTALL).strip()
        return cleaned_response
    except requests.exceptions.RequestException as e:
        print(f"Error querying LLM: {e}")
        return f"Error: Failed to query LLM. Details: {e}"

# Chatbot Function
def chatbot(question):
    """
    Handle the chatbot logic: retrieve relevant context from Neo4j and query the LLM.

    Args:
        question (str): The user's question.

    Returns:
        str: The chatbot's response.
    """
    if not driver:
        return "Error: Neo4j driver is not initialized."

    try:
        with driver.session() as session:
            retrieved_chunks = session.execute_read(search_full_text, question)

        if not retrieved_chunks:
            return "Sorry, I couldn't find relevant information."

        # Combine retrieved content into a single context string
        context = "\n".join([chunk["content"] for chunk in retrieved_chunks])

        # Get response from LLM
        response = query_llm(context, question)
        return response
    except Exception as e:
        print(f"Error in chatbot function: {e}")
        return "Sorry, an error occurred while processing your request."

# Dynamic User Input
if __name__ == "__main__":
    try:
        while True:
            user_question = input("Ask a question (or type 'exit' to quit): ")
            if user_question.lower() == "exit":
                print("Response: Thank You!")
                break
            print("\nResponse:")
            print(chatbot(user_question))
    except KeyboardInterrupt:
        print("\nExiting...")
    finally:
        # Close Neo4j driver when done
        if driver:
            driver.close()