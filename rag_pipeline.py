import os
import chromadb
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from google import genai


# =========================================================
# LOAD ENVIRONMENT
# =========================================================

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env")


# =========================================================
# GEMINI
# =========================================================

client = genai.Client(
    api_key=api_key
)


# =========================================================
# EMBEDDING MODEL
# =========================================================

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


# =========================================================
# CHROMADB
# =========================================================

db = chromadb.PersistentClient(
    path="chroma_db"
)

collection = db.get_collection(
    "teaching_assistant"
)


# =========================================================
# RAG FUNCTION
# =========================================================

def generate_answer(question):

    question_embedding = model.encode(question).tolist()

    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=5
    )

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]

    context = "\n\n".join(documents)

    prompt = f"""
You are an AI Teaching Assistant.

Answer the student's question using the lecture
context provided below.

Rules:

1. Give a direct answer first.
2. If the question asks "What is", "What are",
   or "Define", start with a clear definition.
3. Explain the concept in simple student-friendly language.
4. Use only information supported by the lecture context.
5. Do not invent information.
6. If the lecture context does not contain enough information,
   say that the provided lecture material does not contain
   enough information to give a complete answer.

LECTURE CONTEXT:

{context}

STUDENT QUESTION:

{question}

ANSWER:
"""

    # Retry Gemini request if temporary 503 occurs
    for attempt in range(3):

        try:
            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=prompt
            )

            return {
                "answer": response.text,
                "metadatas": metadatas
            }

        except Exception as e:

            if "503" in str(e) or "UNAVAILABLE" in str(e):

                if attempt < 2:
                    import time

                    wait_time = 2 ** attempt

                    print(
                        f"Gemini temporarily unavailable. "
                        f"Retrying in {wait_time} seconds..."
                    )

                    time.sleep(wait_time)

                else:
                    raise Exception(
                        "Gemini is temporarily experiencing high demand. "
                        "Please try your question again in a few seconds."
                    )

            else:
                raise