import os

TRANSCRIPT_FOLDER = "transcripts"
CHUNK_FOLDER = "chunks"

os.makedirs(CHUNK_FOLDER, exist_ok=True)

CHUNK_SIZE = 500
CHUNK_OVERLAP = 100

for file in os.listdir(TRANSCRIPT_FOLDER):

    if file.endswith(".txt"):

        path = os.path.join(TRANSCRIPT_FOLDER, file)

        with open(path, "r", encoding="utf-8") as f:
            text = f.read()

        chunks = []

        start = 0

        while start < len(text):

            end = start + CHUNK_SIZE

            chunk = text[start:end]

            chunks.append(chunk)

            start = end - CHUNK_OVERLAP

        folder_name = os.path.splitext(file)[0]

        output_folder = os.path.join(
            CHUNK_FOLDER,
            folder_name
        )

        os.makedirs(output_folder, exist_ok=True)

        for i, chunk in enumerate(chunks):

            output_file = os.path.join(
                output_folder,
                f"chunk_{i+1}.txt"
            )

            with open(output_file, "w", encoding="utf-8") as f:
                f.write(chunk)

        print(f"{file}: {len(chunks)} chunks created")

print("Chunking completed!")