from langchain_groq import ChatGroq

model_name = "openai/gpt-oss-20b"
llm = ChatGroq(model="openai/gpt-oss-20b") #model = ChatGroq(model="openai/gpt-oss-20b")
StructuredModel = llm.with_structured_output(Review) #Refer to class Review(BaseModel):
result = StructuredModel.invoke("your prompt here")