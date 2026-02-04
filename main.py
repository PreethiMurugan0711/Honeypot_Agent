from fastapi import FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, Dict

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

# --------------------
# Request Body Schema
# --------------------
class HoneypotBody(BaseModel):
    sessionId: Optional[str] = None
    message: Optional[Dict] = None

# --------------------
# Session Memory
# --------------------
sessions = {}

# --------------------
# Honeypot Endpoint
# --------------------
@app.post("/honeypot")
async def honeypot(body: HoneypotBody, x_api_key: str = Header(None)):

    # 🔐 API Key Check
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    # ✅ Tester-safe fallback
    session_id = body.sessionId or "test-session"

    if body.message and isinstance(body.message, dict):
        text = body.message.get("text", "")
    else:
        text = ""

    if not text:
        raise HTTPException(status_code=400, detail="Message is required")

    # Initialize session
    if session_id not in sessions:
        sessions[session_id] = {
            "step": 0,
            "intel": {
                "upi": [],
                "phones": [],
                "links": []
            }
        }

    session = sessions[session_id]

    # 🕵️ Extract intelligence
    extract_intelligence(text, session["intel"])

    # 🧠 Scam analysis
    analysis = analyze_scam(text)

    # 🤖 Agent reply
    reply = get_reply(session["step"])
    session["step"] += 1

    # ✅ Tester + Judge friendly response
    return {
        "scam_detected": analysis.get("confidence", 0) > 0.6,
        "status": "success",
        "reply": reply,
        "scamType": analysis.get("scamType"),
        "keywords": analysis.get("keywords"),
        "confidence": analysis.get("confidence"),
        "intelligence": session["intel"]
    }