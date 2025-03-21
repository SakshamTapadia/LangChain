from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA

# Load the Document
loader = TextLoader("data.txt")
documents  = loader.load()

# Split the text into smaller chunks
test_splitter = RecursiveCharacterTextSplitter(chunk_size=500 , chunk_overlap=50)
docs = test_splitter.split_documents(documents)

# Convert text into embeddings and store in FAISS
vectorstore = FAISS.from_documents(docs, OpenAIEmbeddings())

# Create a retriever(fetches relevant documents)
retriever = vectorstore.as_retriever()

# Initialize the LLM
llm = OpenAI(model_name = "gpt-3.5-turbo", temperature = 0.7)

# Create a retrievalQA chain

qa_chain = RetrievalQA.from_chain_type(retriever=retriever, llm = llm)

# Ask a question
query = "What are the key take aways from the document?"
answer = qa_chain.run(query)

print("Answer: ", answer)