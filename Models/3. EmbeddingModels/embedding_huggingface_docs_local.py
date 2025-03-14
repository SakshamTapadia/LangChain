from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
)

documents = [
    "Delhi is Capital of India.",
    "Kolkata is Capital of West Bengal.",
    "Paris is Capital of France."
]

vector = embedding.embed_documents(documents)

print(str(vector))