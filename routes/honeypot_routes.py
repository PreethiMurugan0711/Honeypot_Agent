from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.auth import verify_api_key

router = APIRouter()

class HoneypotRequest(BaseModel):
    message: str

@router.post("/honeypot")
def honeypot(
    data: HoneypotRequest,
    auth: bool = Depends(verify_api_key)
):
    msg = data.message.lower()

    # VERY BASIC scam logic (tester-ku podhum)
    is_scam = any(word in msg for word in ["otp", "blocked", "verify", "link"])

    if is_scam:
        return {
            "scam_detected": True,
            "scam_type": "Phishing",
            "agent_status": "engaged",
            "message": "I am not able to open the link. Can you resend?"
        }

    return {
        "scam_detected": False,
        "scam_type": None,
        "agent_status": "idle",
        "message": "Message looks safe"
    }
