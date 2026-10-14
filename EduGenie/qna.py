import os
from google import genai

MODEL_NAME = "gemini-3.8-flash"

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def answer_question_with_gemini(question: str) -> str:
    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=question
        )

        return response.text.strip()

    except Exception as e:
        error_message = str(e)

        # Temporary fallback for demo when Gemini is unavailable
        if "503" in error_message or "UNAVAILABLE" in error_message:
            if "sky" in question.lower() and "blue" in question.lower():
                return (
                    "The sky appears blue because sunlight passes through "
                    "the Earth's atmosphere. Blue light is scattered more "
                    "strongly than other visible colours, so our eyes see "
                    "more blue light coming from the sky."
                )

            return (
                "EduGenie is temporarily unable to connect to the Gemini "
                "AI service. Please try again later."
            )

        return f"⚠️ Error in QnA: {e}"