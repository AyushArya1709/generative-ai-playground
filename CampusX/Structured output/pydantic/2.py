import os
from dotenv import load_dotenv
import instructor
from groq import Groq
from pydantic import BaseModel, Field

load_dotenv()

# Initialize Groq client wrapped with instructor
client = instructor.from_groq(Groq())

# Active model on Groq
SELECTED_MODEL = "openai/gpt-oss-20b"


# 1. Define your Pydantic schema
class Review(BaseModel):
  key_themes: list[str] = Field(
      description="Write down all the key themes discussed in the review in a list"
  )
  summary: str = Field(description="A brief summary of the review")
  sentiment: str = Field(
      description=(
          "Return sentiment of the review: exactly 'positive', 'negative', or"
          " 'neutral'"
      )
  )
  pros: list[str] | None = Field(
      default=None, description="Write down all the pros inside a list"
  )
  cons: list[str] | None = Field(
      default=None, description="Write down all the cons inside a list"
  )
  name: str | None = Field(
      default=None, description="Write the name of the reviewer"
  )


# 2. Call the model using instructor's response_model parameter
result = client.chat.completions.create(
    model=SELECTED_MODEL,
    response_model=Review,
    messages=[
        {
            "role": "system",
            "content": (
                "You are an expert review analyzer. Extract the requested"
                " information precisely."
            ),
        },
        {
            "role": "user",
            "content": """I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to native ranges works well, but anything beyond loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Review by Nitish Singh""",
        },
    ],
)

print(result)