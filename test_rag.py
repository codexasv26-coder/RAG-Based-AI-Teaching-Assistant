from rag_pipeline import generate_answer

print("Testing RAG system...")

question = "What is quantum computing?"

try:
    result = generate_answer(question)

    print("\n========== ANSWER ==========\n")
    print(result["answer"])

    print("\n========== SOURCES ==========\n")
    for metadata in result["metadatas"]:
        print(metadata)

    print("\nRAG TEST SUCCESSFUL!")

except Exception as e:
    print("\nRAG ERROR:")
    print(e)