conversation_history = []

def add_to_history(user_question):
    conversation_history.append(user_question)
    
    if len(conversation_history) > 3:
        conversation_history.pop(0)

def get_history_context():
    if not conversation_history:
        return "No previous history."
    
    return "\n".join(conversation_history)