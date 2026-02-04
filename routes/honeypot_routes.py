from fastapi import APIRouter

router = APIRouter()

@router.get("/status")
def honeypot_status():
    return {"status": "Honeypot Active"}
