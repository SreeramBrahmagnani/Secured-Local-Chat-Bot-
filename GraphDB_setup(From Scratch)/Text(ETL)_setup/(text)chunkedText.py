#!/usr/bin/env python
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Function to read text from a file
def read_text_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

# Function to chunk text
def chunk_text(text, chunk_size=1024, chunk_overlap=50):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return text_splitter.split_text(text)

# Folder where extracted text files are stored
text_folder = "extracted_text"
chunked_folder = "chunked_text"

# Create folder to store chunked text
if not os.path.exists(chunked_folder):
    os.makedirs(chunked_folder)

# Process each text file
for filename in os.listdir(text_folder):
    if filename.endswith(".txt"):
        file_path = os.path.join(text_folder, filename)
        text = read_text_file(file_path)

        # Chunk the text
        chunks = chunk_text(text)

        # Save chunks as separate files
        for i, chunk in enumerate(chunks):
            chunk_filename = f"{filename.replace('.txt', '')}_chunk_{i}.txt"
            chunk_path = os.path.join(chunked_folder, chunk_filename)
            with open(chunk_path, "w", encoding="utf-8") as f:
                f.write(chunk)

        print(f"Chunked {filename} into {len(chunks)} parts.")

print("Chunking complete.")
#source graph_rag_env/Scripts/activate
#python chunkedText.py
#deactivate
