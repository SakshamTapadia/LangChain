from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# Load the LLM
llm = OpenAI(model_name = "gpt-3.5-turbo",temperature=0.7) 

# Create a prompt template
prompt = PromptTemplate(
    input_variables=["topic"],
    template="Suggest a catchy blog title about {topic}"
)

# Create the LLMChain
llmchain = LLMChain(llm=llm, prompt=prompt)

# Run the LLMChain
topic = input("Enter a topic: ")
output =  llmchain.run(topic)

print("Generated Blog Title: ", output)