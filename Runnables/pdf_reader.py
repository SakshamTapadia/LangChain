from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import OpenAI

# Load the Document
loader = TextLoader('docs.txt') 
documents = loader.load()

# Split the text into smaller chunks
test_splitter = RecursiveCharacterTextSplitter(chunk_size=500 , chunk_overlap=50)
docs = test_splitter.split_documents(documents)

# Convert text into embeddings and store in FAISS
vectorstore = FAISS.from_documents(docs, OpenAIEmbeddings())

# Create a retriever(fetches relevant documents)
retriever = vectorstore.as_retriever()

# Manually retrieve relevant documents
query = "What are the key take aways from the document?"
retrieved_doc = retriever.get_relevant_documents(query)

# Combine retrieved text into a single prompt
retireved_text = "\n".join([doc.page_content for doc in retrieved_doc])

# Initialize the LLM
llm = OpenAI(model_name ="gpt-3.5-turbo" , temperature = 0.7)

# Manually pass Retrieved text into the LLM
prompt = f"Based on the following text, answer the question: {query}\n\n{retireved_text}"
answer = llm.predict(prompt)

# Print the answer
print("Answer: ", answer)