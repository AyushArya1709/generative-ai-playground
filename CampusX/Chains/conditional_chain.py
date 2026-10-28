from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model_name = "openai/gpt-oss-120b" #Active model on Groq

model = ChatGroq(model = model_name)

parser1 = StrOutputParser()

class Feedback(BaseModel):

    sentiment : Literal['positive','negative'] = Field(description = 'Give the sentiment of the feedback')

parser2 = PydanticOutputParser(pydantic_object = Feedback)

prompt1 = PromptTemplate(
    template = 'Classify the sentiment of the following feedback text into postive or negative \n {feedback} \n {format_instruction}',
    input_variables = ['feedback'],
    partial_variables = {'format_instruction':parser2.get_format_instructions()}
)

# 🔥 STEP 1: CLASSIFIER CHAIN
 
classifier_chain = prompt1 | model | parser2

prompt2 = PromptTemplate(
    template = 'write an appropriate response to this positive feedback \n {feedback}',
    input_variables = ['feedback'],
)
 
prompt3 = PromptTemplate(
    template = 'write an appropriate response to this negative feedback \n {feedback}',
    input_variables = ['feedback'],
)    

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive' , prompt2 | model | parser1),
    (lambda x:x.sentiment == 'negative' , prompt3 | model | parser1),
     RunnableLambda(lambda x: "could not find sentiment") 
    )  # the problem here is that, this is not a chain "you have to execute a chain here"

# 🚀 STEP 2: FINAL CHAIN

final_chain = classifier_chain | branch_chain

print(final_chain.invoke({'feedback':'This is a terrible phone'}))

final_chain.get_graph().print_ascii()