import os
from google import genai

MODEL_NAME = "gemini-3.8-flash"

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def get_learning_recommendations(topic: str) -> str:

    prompt = f"""
You are an AI tutor.

The student wants to learn about:
{topic}

Suggest a structured and adaptive learning path including:

1. Beginner level
2. Intermediate level
3. Advanced level
4. Key topics
5. Order of learning
6. Useful resources

Give the guidance in simple language.
"""

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )

        if response.text:
            return response.text

        return "❌ Could not extract content from Gemini response."

    except Exception as e:
        return f"❌ Error occurred: {e}"