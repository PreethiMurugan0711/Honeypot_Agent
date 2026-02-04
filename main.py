from fastapi import FastAPI, Request, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from config import API_KEY
from detector import analyze_scam
from agent import get_reply
from extractor import extract_intelligence

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

sessions = {}

@app.post("/honeypot")
async def honeypot(request: Request, x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    body = await request.json()
    session_id = body["sessionId"]
    text = body["message"]["text"]

    if session_id not in sessions:
        sessions[session_id] = {
            "step": 0,
            "intel": {"upi": [], "phones": [], "links": []}
        }

    session = sessions[session_id]

    extract_intelligence(text, session["intel"])
    analysis = analyze_scam(text)

    reply = get_reply(session["step"])
    session["step"] += 1

    return {
        "status": "success",
        "reply": reply,
        "scamType": analysis["scamType"],
        "keywords": analysis["keywords"],
        "confidence": analysis["confidence"],
        "intelligence": session["intel"]
    }
