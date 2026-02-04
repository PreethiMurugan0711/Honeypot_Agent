def get_reply(step: int):
    replies = [
        "Why will my account be blocked?",
        "Which bank are you calling from?",
        "I don’t understand, can you explain clearly?",
        "Is this urgent? What should I do now?"
    ]
    return replies[step] if step < len(replies) else replies[-1]
