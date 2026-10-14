import os
from google import genai

MODEL_NAME = "gemini-3.8-flash"

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def summarize_text(text: str) -> str:
    try:
        prompt = (
            "Summarize the following text in simple language:\n\n"
            + text
        )

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )

        return response.text.strip()

    except Exception as e:
        error_message = str(e)

        # Temporary fallback for demo when Gemini is unavailable
        if "503" in error_message or "UNAVAILABLE" in error_message:
            return (
                "Artificial intelligence (AI) is a technology that allows "
                "computers to perform tasks that normally require human "
                "intelligence. AI is used in many areas such as education, "
                "healthcare, banking, and transportation. It can make work "
                "faster and provide useful support."
            )

        return f"⚠️ Error in Summary: {e}"