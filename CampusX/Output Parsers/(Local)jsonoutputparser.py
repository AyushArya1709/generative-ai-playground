from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate

model = ChatOpenAI( 
    model="qwen3.5-2b",
    base_url="http://127.0.0.1:1234/v1", 
    api_key="lm-studio",
)

parser = JsonOutputParser()

template = PromptTemplate(
    template = 'give me the name, age and city of a fictional person \n {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction': parser.get_format_instructions()}
    
)

''' prompt = template.format()

print(prompt) #just in case if you're wondering what is this prompt doing here

result = model.invoke(prompt)

final_result = parser.parse(result.content)

print(final_result)

print(final_result['name']) #so as this is a dictionary we can directly fetch name from it

print(type(final_result)) 

# we can write this code in an easy/simple way using chains
'''

chain = template | model | parser 

result = chain.invoke({})

print(result)


''' So everything is well and fine but here's a limitation of output parser that
we cannot enforce our desired JSON structure to JsonOutputParser so for that we'll have to use a different Structured output parser'''

