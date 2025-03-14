from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4",temperature= 0.7, max_completion_tokens=10)
# temperature is a value between from 0 that controls the randomness of the model's responses.

# for more realistic and deterministic task temp should  be like 0,0.1, 0.2 .
# for creative and more imaginative tasks temp should be like 0.9, 1,1.5+ .

result = model.invoke("What is the capital of India?")

print(result)
#returns many things like tokens, answer, choices, etc. but the answer is in the 'content' .

print(result.content)
#returns the answer to the question.