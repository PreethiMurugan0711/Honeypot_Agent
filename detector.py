def analyze_scam(text: str):
    text = text.lower()

    patterns = {
        "Bank Scam": ["bank", "account", "blocked", "verify", "kyc"],
        "UPI Scam": ["upi", "pay", "payment", "send money"],
        "OTP Scam": ["otp", "verification code"],
        "Lottery Scam": ["won", "prize", "reward"]
    }

    keywords = []
    scam_type = "Unknown"

    for t, words in patterns.items():
        for w in words:
            if w in text:
                keywords.append(w)
                scam_type = t

    confidence = min(len(keywords) * 0.2, 1.0)

    return {
        "scamType": scam_type,
        "keywords": list(set(keywords)),
        "confidence": round(confidence, 2)
    }
