from config import SECRET_KEY

def verify_user(username: str, password: str):
    # demo auth (can be replaced with real DB later)
    if username == "admin" and password == "admin123":
        return True
    return False
