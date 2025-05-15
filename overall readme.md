---

## **README.md**

# **Project Overview**

This repository contains the code and resources for a **Chatbot with Neo4j and DeepSeek R1 API**. The project is organized into several folders and files, each serving a specific purpose. Below is a detailed overview of the project structure.

---

## **Folder Structure**

### **1. `Final_Product`**
Contains the final versions of the chatbot scripts.

- `chatbot_i_o.py`: Command-line chatbot.

- `(chatbot)readme.md`: Documentation for the chatbot scripts.

### **2. `GraphDB_setup(From Scratch)`**
Scripts and documentation for setting up the Neo4j database from scratch.

- `(neo)neo_setup.py`: Script to set up the Neo4j database.
- `(neo)link_chunk.py`: Script to link chunks of text in the database.
- `Text(ETL)_setup/`: Folder for text extraction, transformation, and loading scripts.
  - `extractText.py`: Extracts text from PDF files.
  - `chunkedText.py`: Splits extracted text into chunks.
  - `(text)readme.md`: Documentation for text ETL scripts.

### **3. `GraphDB_setup(Import)`**
Resources for importing an existing Neo4j database.

- `neo4j.dump`: Database dump file.
- `readme.neo4j setup.txt`: Documentation for setting up Neo4j using the dump file.

---

## **How to Use**

### **1. Setting Up the Neo4j Database**
- For setup from scratch, see `GraphDB_setup(From Scratch)/(GraphDB)readme.text`.
- For importing a dump, see `GraphDB_setup(Import)/readme.neo4j setup.txt`.

### **2. Setting Up the LLM Local API**
- Ensure lmstudios is installed and running.
- Download `deepseek-r1-distill-qwen-7b`.
- Import and copy the port address.

### **3. Running the Chatbot**

**Command-Line Chatbot:**
- Use `Final_Product/chatbot_i_o.py` or `Final_Product/chatbot_i_o_with_loggings.py`.
- Run:
  ```bash
  python Final_Product/chatbot_i_o.py
  ```

**API Chatbot:**
- Use `Final_Product/chatbot_API.py` or `Final_Product/chatbot_API_with_Loggings.py`.
- Run:
  ```bash
  python Final_Product/chatbot_API.py
  ```
- Test the API using Postman (see `Prototypes/API_test_Postman.png`).

### **4. Virtual Environment**
- Create a virtual environment:
  ```bash
  python -m venv venv
  ```
- Activate it:
  ```bash
  venv\Scripts\activate  # On Windows
  source venv/bin/activate  # On macOS/Linux
  ```

---

## **Dependencies**
1. **Python 3.7+**:  
   Ensure Python is installed.

2. **Neo4j**:  
   Ensure Neo4j is installed and running.

3. **Python Packages**:  
   Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. **LLM setup**:  
   Ensure lmstudios is installed and running.  
   Download `deepseek-r1-distill-qwen-7b`.  
   Import and copy port address.

---
