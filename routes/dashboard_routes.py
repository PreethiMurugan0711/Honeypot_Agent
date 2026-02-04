from fastapi import APIRouter

router = APIRouter()

@router.get("/dashboard/summary")
def dashboard_summary():
    return {
        "total_scams": 128,
        "bank_scams": 56,
        "upi_scams": 42,
        "otp_scams": 30
    }
