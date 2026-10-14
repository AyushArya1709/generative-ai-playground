from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

model = ChatOpenAI( 
    model="qwen3.5-2b",
    base_url="http://127.0.0.1:1234/v1", 
    api_key="lm-studio",
)

#1st prompt -> detailed report

template1 = PromptTemplate(
    template = 'Write a detailed report on {topic}',
    input_variables = ['topic'] 
)

#2nd prompt -> summary

template2 = PromptTemplate(
    template = 'Write a 5 line summary on the following text. \n {text}',
    input_variables = ['text']
)

prompt1 = template1.invoke({'topic':'black hole'})

result1 = model.invoke(prompt1)

print("Result1 : ", result1.content)

prompt2 = template2.invoke({'text':result1.content})

result2 = model.invoke(prompt2)

print("Result 2 : ", result2.content)