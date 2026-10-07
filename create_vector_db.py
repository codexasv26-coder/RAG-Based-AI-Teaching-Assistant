import os
import json
import chromadb

EMBEDDING_FOLDER = "embeddings"
DB_FOLDER = "chroma_db"

# Create ChromaDB client
client = chromadb.PersistentClient(path=DB_FOLDER)

# Create collection
collection = client.get_or_create_collection(
    name="teaching_assistant"
)

print("ChromaDB initialized successfully!")

# Read all embedding files
for file in os.listdir(EMBEDDING_FOLDER):

    if file.endswith(".json"):

        file_path = os.path.join(EMBEDDING_FOLDER, file)

        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        topic = data["topic"]
        chunks = data["chunks"]
        embeddings = data["embeddings"]

        print(f"\nAdding: {topic}")

        ids = []
        documents = []
        metadatas = []

        for i, chunk in enumerate(chunks):

            chunk_id = f"{topic}_{i}"

            ids.append(chunk_id)
            documents.append(chunk["text"])

            metadatas.append({
                "topic": topic,
                "filename": chunk["filename"]
            })

        collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas
        )

        print(f"Added {len(chunks)} chunks.")

print("\nAll embeddings stored in ChromaDB!")

print("Total documents in database:", collection.count())