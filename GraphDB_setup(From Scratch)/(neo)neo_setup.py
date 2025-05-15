import os
from neo4j import GraphDatabase

# Neo4j Connection
URI = "neo4j://localhost:7687"
USERNAME = "neo4j"
PASSWORD = "jaajijaaji"  # Replace with actual credentials

driver = GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD))

# Folder containing all text chunks
DATA_FOLDER = "chunked_text"

# Function to read all text files
def read_all_chunks(folder_path):
    chunk_data = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            with open(os.path.join(folder_path, filename), "r", encoding="utf-8") as file:
                content = file.read().strip()
                chunk_data.append({"filename": filename, "content": content})
    return chunk_data

# Function to store chunks in Neo4j
def store_chunk(tx, filename, content):
    tx.run("""
        CREATE (c:DocumentChunk {filename: $filename, content: $content})
    """, filename=filename, content=content)

# Insert chunks into Neo4j
def insert_chunks_into_graph(chunks):
    with driver.session() as session:
        for chunk in chunks:
            session.execute_write(store_chunk, chunk["filename"], chunk["content"])

# Read and insert data
chunks = read_all_chunks(DATA_FOLDER)
insert_chunks_into_graph(chunks)

print("✅ All chunks stored successfully in Neo4j!")

driver.close()
