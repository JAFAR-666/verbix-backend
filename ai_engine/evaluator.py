def evaluate_response(user_input):
    # Simple logic-based mock evaluation

    word_count = len(user_input.split())

    fluency_score = min(10, max(4, word_count // 2))

    grammar_feedback = "Good" if user_input[0].isupper() else "Start sentences with a capital letter."

    suggestion = "Try adding more details to your response." if word_count < 5 else "Good structure. You can improve vocabulary."

    improved = user_input.capitalize()
    if not improved.endswith("."):
        improved += "."

    return {
        "fluency": fluency_score,
        "grammar": grammar_feedback,
        "suggestion": suggestion,
        "improved": improved
    }