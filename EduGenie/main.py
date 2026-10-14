from fastapi import FastAPI, Request, Query
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from explanation_module import explain_topic
from qna import answer_question_with_gemini
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations

app = FastAPI()

templates = Jinja2Templates(directory="templates")

# Connect CSS/static folder
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )


# Q&A
@app.get("/qa")
async def answer_question(question: str = Query(...)):
    answer = answer_question_with_gemini(question)
    return {"answer": answer}


# Explanation
@app.post("/explain")
async def explain_api(request: Request):
    data = await request.json()
    topic = data.get("topic")

    if not topic:
        return JSONResponse(
            content={"error": "Please provide a topic."},
            status_code=400
        )

    explanation = explain_topic(topic)
    return {"topic": topic, "explanation": explanation}


# Summary
@app.post("/summarize")
async def summarize_api(request: Request):
    data = await request.json()
    text = data.get("text")

    if not text:
        return JSONResponse(
            content={"error": "Please provide text to summarize."},
            status_code=400
        )

    summary = summarize_text(text)
    return {"summary": summary}


# Quiz
@app.post("/quiz")
async def quiz_api(request: Request):
    data = await request.json()
    text = data.get("text")

    if not text:
        return JSONResponse(
            content={"error": "Please provide text for quiz."},
            status_code=400
        )

    quiz = generate_quiz(text)
    return {"quiz": quiz}


# Learning Recommendations
@app.get("/learn/recommendations")
async def learning_recommendation_api(
    topic: str = Query(...)
):
    recommendation = get_learning_recommendations(topic)
    return {
        "topic": topic,
        "recommendation": recommendation
    }