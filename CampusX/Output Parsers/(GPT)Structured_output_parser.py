from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_classic.output_parsers.structured import StructuredOutputParser , ResponseSchema


load_dotenv()

#Defining the model

model = ChatGroq(
    model="openai/gpt-oss-20b",  # keeps responses focused
)

schema = [
    ResponseSchema(name='fact_1', description='Fact 1 about the topic'),
    ResponseSchema(name='fact_2', description='Fact 2 about the topic'),
    ResponseSchema(name='fact_3', description='Fact 3 about the topic'),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    
    input_variables = ['topic'],
    partial_variables = {'format_instruction':parser.get_format_instructions()}, 
    template = 'Give 3 facts about the {topic} \n {format_instruction}',
)

prompt = template.invoke({'topic':'black hole'})

result = model.invoke(prompt)

print(result.content)
