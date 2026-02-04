import re

def extract_intelligence(text: str, store: dict):
    store["upi"].extend(re.findall(r"\b[\w.-]+@[\w.-]+\b", text))
    store["phones"].extend(re.findall(r"\b\d{10}\b", text))
    store["links"].extend(re.findall(r"https?://\S+", text))
