class AIModel:
    """Base class for AI models."""

    def __init__(self, model_name):
        self.model_name = model_name

    def display_info(self):
        print(f"Model Name: {self.model_name}")

    def generate_response(self, prompt):
        raise NotImplementedError(
            "Subclasses must implement generate_response()"
        )


class TextModel(AIModel):
    """A simple model that generates text responses."""

    def __init__(self, model_name, provider):
        super().__init__(model_name)
        self.provider = provider

    def display_info(self):
        super().display_info()
        print(f"Provider: {self.provider}")

    def generate_response(self, prompt):
        return f"{self.model_name} received: {prompt}"


class SentimentModel(AIModel):
    """A simple model that classifies sentiment."""

    def generate_response(self, prompt):
        prompt = prompt.lower()

        if any(word in prompt for word in ["good", "great", "excellent", "love"]):
            return "Positive sentiment"

        elif any(word in prompt for word in ["bad", "terrible", "hate", "poor"]):
            return "Negative sentiment"

        return "Neutral sentiment"


# Creating objects
text_model = TextModel("Demo-LLM", "Local Provider")
sentiment_model = SentimentModel("Demo-Sentiment")

# Displaying model information
text_model.display_info()

# Generating responses
print("\nText Model:")
print(text_model.generate_response("Explain artificial intelligence"))

print("\nSentiment Model:")
print(sentiment_model.generate_response("This product is excellent!"))
print(sentiment_model.generate_response("This product is terrible!"))
print(sentiment_model.generate_response("The product arrived today."))
