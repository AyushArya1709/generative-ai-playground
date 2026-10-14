from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import Optional, Literal
from pydantic import BaseModel, Field
import os

load_dotenv()


# Model
model_name = "openai/gpt-oss-20b"

model = ChatGroq(model = model_name)

# Schema
class Review(BaseModel):

    name: Optional[str] = Field(
        default=None,
        description="The name of the product being reviewed"
    )

    key_themes: list[str] = Field(
        description="A list of key themes or topics mentioned in the review"
    )

    summary: str = Field(
        description="A short summary of the review"
    )

    sentiment: Literal[
        "positive",
        "negative",
        "neutral"
    ] = Field(
        description="The sentiment of the review"
    )

    pros: Optional[list[str]] = Field(
        default=None,
        description="A list of pros mentioned in the review"
    )

    cons: Optional[list[str]] = Field(
        default=None,
        description="A list of cons mentioned in the review"
    )


# Structured output
StructuredModel = model.with_structured_output(Review)


# Invoke
result = StructuredModel.invoke("""
Analyze the following product review.

Review:

I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say,
it's an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes
everything lightning fast whether I'm gaming, multitasking, or editing
photos. The 5000mAh battery easily lasts a full day even with heavy use,
and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches.
The 200MP camera is excellent, especially in low light. Zooming up to 100x
works well for distant objects, but anything beyond 30x loses quality.

However, the phone is heavy and uncomfortable for one-handed use.
Samsung's One UI also contains bloatware, and the $1,300 price is high.

Pros:
- Powerful processor
- Excellent 200MP camera
- Long battery life
- S-Pen support

Cons:
- Heavy and bulky
- Bloatware
- Expensive
""")


print(result)

print("\nSummary:", result.summary)
print("Sentiment:", result.sentiment)
print("Name:", result.name)
print("Key themes:", result.key_themes)
print("Pros:", result.pros)
print("Cons:", result.cons)