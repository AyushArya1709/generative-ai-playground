import random
from abc import ABC, abstractmethod

# 1. The abstract base class that standardizes all components
class Runnable(ABC):
    @abstractmethod
    def invoke(self, input_data):
        pass

# 2. A dummy LLM that returns a random canned response
class NakliLLM(Runnable):
    def __init__(self):
        print("LLM created")

    def invoke(self, prompt):
        responses = [
            'Honey never expires and was found preserved in Egyptian tombs',
            'Octopuses have three hearts and blue blood',
            'A day on Venus is longer than a year on Venus'
        ]
        return {'response': random.choice(responses)}

# 3. A dummy prompt template that formats a string with input variables
class NakliPromptTemplate(Runnable):
    def __init__(self, template, input_variables):
        self.template = template
        self.input_variables = input_variables

    def invoke(self, input_dict):
        # Format the template with the provided dictionary
        return self.template.format(**input_dict)

# 4. A connector that chains multiple runnables together
class RunnableConnector(Runnable):
    def __init__(self, runnable_list):
        self.runnable_list = runnable_list

    def invoke(self, input_data):
        for runnable in self.runnable_list:
            input_data = runnable.invoke(input_data)
        return input_data

# --- Your original code (now fully executable) ---

template1 = NakliPromptTemplate(
    template='Create a short murder mystery involving {location}',
    input_variables=['location']
)

template2 = NakliPromptTemplate(
    template='Identify the culprit in this mystery and explain why: {response}',
    input_variables=['response']
)

llm = NakliLLM()

chain1 = RunnableConnector([template1, llm])

chain2 = RunnableConnector([template2, llm])

final_chain = RunnableConnector([chain1, chain2])

result = final_chain.invoke({'location': 'a haunted mansion'})
print(result)