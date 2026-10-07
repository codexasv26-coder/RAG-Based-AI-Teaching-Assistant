import os
import json
from sentence_transformers import SentenceTransformer

CHUNK_FOLDER = "chunks"
EMBEDDING_FOLDER = "embeddings"

os.makedirs(EMBEDDING_FOLDER, exist_ok=True)

print("Loading embedding model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

print("Embedding model loaded successfully!")

for topic in os.listdir(CHUNK_FOLDER):

    topic_path = os.path.join(CHUNK_FOLDER, topic)

    if not os.path.isdir(topic_path):
        continue

    print(f"\nProcessing: {topic}")

    chunks = []
    embeddings = []

    for file in os.listdir(topic_path):

        if file.endswith(".txt"):

            file_path = os.path.join(topic_path, file)

            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()

            embedding = model.encode(text)

            chunks.append({
                "filename": file,
                "text": text
            })

            embeddings.append(embedding.tolist())

    output_file = os.path.join(
        EMBEDDING_FOLDER,
        topic.replace(" ", "_") + ".json"
    )

    data = {
        "topic": topic,
        "chunks": chunks,
        "embeddings": embeddings
    }

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f)

    print(f"Created embeddings for {len(chunks)} chunks.")

print("\nAll embeddings created successfully!")