from langchain.llms import Bedrock
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Initialize the Bedrock LLM
llm = Bedrock(
    model_id="anthropic.claude-v2",
    credentials_profile_name="default",
    model_kwargs={"temperature": 0.7}
)

# Create a prompt template
prompt = PromptTemplate(
    input_variables=["topic"],
    template="Write a short paragraph about {topic}."
)

# Create a chain
chain = LLMChain(llm=llm, prompt=prompt)

# Run the chain
response = chain.run(topic="artificial intelligence")
print(response)