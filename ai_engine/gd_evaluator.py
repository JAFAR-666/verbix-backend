def evaluate_gd(chat_history):
    total_words = 0
    user_turns = 0

    for role, msg in chat_history:
        if "You" in role:
            total_words += len(msg.split())
            user_turns += 1

    # Basic scoring logic
    participation = min(10, user_turns * 2)
    clarity = min(10, total_words // 5)
    confidence = min(10, user_turns + 3)

    # Suggestions
    if total_words < 20:
        suggestion = "Try to speak more and elaborate your points."
    elif total_words < 50:
        suggestion = "Good, but you can improve clarity and structure."
    else:
        suggestion = "Excellent participation and detailed responses."

    return {
        "participation": participation,
        "clarity": clarity,
        "confidence": confidence,
        "suggestion": suggestion,
        "overall": (participation + clarity + confidence) // 3
    }