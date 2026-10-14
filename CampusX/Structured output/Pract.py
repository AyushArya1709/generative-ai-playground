from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from typing import Optional, TypedDict, Annotated
import os

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen3-4B-Instruct-2507",
    task="text-generation",
    provider="nscale",
    huggingfacehub_api_token=os.getenv("HF_TOKEN"),
)

model = ChatHuggingFace(llm=llm)

#schema for the structured output/data format 

class Review(TypedDict):
    name: Annotated[Optional[str], "The name of the reviewer"]
    key_themes: Annotated[list[str], "A list of key themes or topics mentioned in the review"]
    summary: Annotated[str, "A short summary of the review"]
    sentiment: Annotated[str, "Either 'positive', 'negative', or 'neutral'"]
    pros: Annotated[Optional[list[str]], "A list of pros mentioned in the review"]
    cons: Annotated[Optional[list[str]], "A list of cons mentioned in the review"]
    

StructuredModel = model.with_structured_output(
    Review,
    method="json_mode"
)




result = StructuredModel.invoke("""
Analyze the following product review.

Return ONLY valid JSON.

The JSON MUST contain exactly these fields:
- name: the name of the reviewer
- summary: a short summary of the review
- sentiment: either "positive", "negative", or "neutral"
- key_themes: a list of key themes or topics mentioned in the review
- pros: a list of pros mentioned in the review
- cons: a list of cons mentioned in the review


Review:
I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it's an absolute powerhouse! The Snapdragon 8 Gen 3
processor makes everything lightning fast-whether I'm gaming, multitasking, or editing photos. The 5000mAh battery easily
lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me
away is the 200MP camera-the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x
actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung's One UI still comes with
bloatware-why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard
pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful

Cons:
Bulky and heavy-not great for one-handed use
Bloatware still exists in One UI
Expensive compared to competitors

Reviewer: Ayush Arya
""")

print(result["name"])