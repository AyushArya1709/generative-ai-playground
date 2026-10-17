from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

prompt1 = PromptTemplate(
    input_variables = ['topic'],
    template = 'Generate a detailed report on {topic}',
)

prompt2 = PromptTemplate(
    template = 'Generate a 5 pointer summary from the following text \n {text}',
    input_variables = ['text']
)

#Defining the model
model_name = "openai/gpt-oss-20b" #Active model on Groq

model = ChatGroq(model = model_name)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({'topic': 'AI Industry'})

print(result)