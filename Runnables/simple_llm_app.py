from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

# Intialize the LLM

llm = OpenAI(model_name = 'gpt-3.5-turbo',temperature = 0.7)

# Create a prompt template 
prompt = PromptTemplate(
    input_variables = ['topic'],
    template = 'Suggest a catchy blog title about {topic}'
)

# Define the input
topic = input('Enter the topic: ')

# Format the prompt manually using PromptTemplate
formatted_prompt = prompt.format(topic = topic)

# Call the LLM directly
blog_title = llm.predict(formatted_prompt)

#Print Input
print("Generated Blog Title: ", blog_title)