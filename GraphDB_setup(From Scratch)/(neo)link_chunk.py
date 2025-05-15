from neo4j import GraphDatabase

# Neo4j Connection
URI = "neo4j://localhost:7687"
USERNAME = "neo4j"
PASSWORD = "jaajijaaji"  # Replace with actual credentials

driver = GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD))

# Link sequential chunks from the same file using :NEXT
def link_sequential_chunks(tx):
    tx.run("""
        MATCH (c1:DocumentChunk), (c2:DocumentChunk)
        WHERE c1.filename = c2.filename AND c1 <> c2
        MERGE (c1)-[:NEXT]->(c2)
    """)

# Link chunks with similar keywords using :RELATED_TO
def link_similar_chunks(tx):
    keywords = ["handover", "approval", "logsheet", "bulk", "solution", "filter", "update"]
    for keyword in keywords:
        tx.run("""
            MATCH (c1:DocumentChunk), (c2:DocumentChunk)
            WHERE c1 <> c2 AND c1.content CONTAINS $keyword AND c2.content CONTAINS $keyword
            MERGE (c1)-[:RELATED_TO]->(c2)
        """, keyword=keyword)

# Create relationships
with driver.session() as session:
    session.execute_write(link_sequential_chunks)
    session.execute_write(link_similar_chunks)

print("✅ Relationships created successfully in Neo4j!")

driver.close()

