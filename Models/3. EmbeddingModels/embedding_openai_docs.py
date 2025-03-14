from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding  = OpenAIEmbeddings(
    model="text-embedding-3-large",
    dimensions=32
)


documents = [
    "Delhi is Capital of India.",
    "Kolkata is Capital of West Bengal.",
    "Paris is Capital of France."
]

result = embedding.embed_documents(documents)

print(str(result))