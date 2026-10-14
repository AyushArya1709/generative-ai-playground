import os
from dotenv import load_dotenv
import instructor
from groq import Groq
from pydantic import BaseModel, Field

# ==========================================
# 1. LOAD ENVIRONMENT & INITIALIZE CLIENT
# ==========================================
load_dotenv()  # Automatically loads GROQ_API_KEY from your .env file

base_client = Groq()
client = instructor.from_groq(base_client)

# Using Groq's active model string
SELECTED_MODEL = "openai/gpt-oss-20b"


# ==========================================
# 2. DEFINE YOUR PYDANTIC SCHEMA
# ==========================================
class SentimentAnalysis(BaseModel):
  sentiment: str = Field(description="Positive, Negative, or Neutral")
  confidence_score: float = Field(description="Confidence score between 0.0 and 1.0")
  key_points: list[str] = Field(
      description="Main reasons behind the sentiment"
  )


# ==========================================
# 3. RUN YOUR CODE / LOGIC
# ==========================================
response = client.chat.completions.create(
    model=SELECTED_MODEL,
    response_model=SentimentAnalysis,
    messages=[
        {
            "role": "system",
            "content": (
                "You are an expert sentiment analysis system. Extract the"
                " required structure accurately."
            ),
        },
        {
            "role": "user",
            "content": (
                "I absolutely love this new framework! Building pipelines"
                " has never been this smooth."
            ),
        },
    ],
)

# Output results
print("--- Extracted Pydantic Object ---")
print(response)
print(f"\nSentiment: {response.sentiment}")
print(f"Confidence: {response.confidence_score}")