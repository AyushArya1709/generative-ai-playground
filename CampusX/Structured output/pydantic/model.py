from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    model="qwen3.5-2b",
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio",
)