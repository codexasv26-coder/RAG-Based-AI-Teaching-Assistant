import chromadb
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to ChromaDB
client = chromadb.PersistentClient(path="chroma_db")

# Get collection
collection = client.get_collection("teaching_assistant")

print("RAG Retrieval System Ready!")

# Ask your question here
question = input("\nAsk your question: ")

# Convert question into embedding
question_embedding = model.encode(question).tolist()

# Search ChromaDB
results = collection.query(
    query_embeddings=[question_embedding],
    n_results=3
)

print("\n===== MOST RELEVANT CONTENT =====\n")

for i, document in enumerate(results["documents"][0]):

    print(f"Result {i + 1}:")
    print(document)
    print("\n-----------------------------\n")