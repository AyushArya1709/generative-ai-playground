from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

#Define the model

model_name = "openai/gpt-oss-20b" #Active model on Groq

model = ChatGroq(model=model_name)

class Person(BaseModel):
    
    name: str = Field (description= 'name of the person')
    age: int = Field (gt=18, description = 'age of the person')
    city: str = Field (description = 'Name of the city of the person belongs to')
    
parser = PydanticOutputParser(pydantic_object = Person)

template = PromptTemplate(
    input_variables=['place'],
    partial_variables={'format_instruction': parser.get_format_instructions()},
    template = 'Generate the name, age and city of a fictional {place} person \n {format_instruction}',
)
    
chain = template | model | parser

final_result = chain.invoke({'place':'american'})
    
''' prompt = template.invoke({'place':'indian'})

result = model.invoke(prompt)

final_result = parser.parse(result.content)'''

print(final_result)



