from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

#Define the model

model_name = "openai/gpt-oss-20b" #Active model on Groq

model = ChatGroq(model = model_name)



prompt = PromptTemplate(
    template = 'Generate 5 interesting facts about {topic}',
    input_variables = ['topic'],
)

Parser = StrOutputParser()

chain = prompt | model  | Parser

result = chain.invoke({'topic':'Ben 10'})

print(result)

chain.get_graph().print_ascii()