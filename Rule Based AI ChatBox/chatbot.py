from datetime import datetime

def get_response(user_input):

    user_input = user_input.lower().strip()

    # Greetings
    if user_input in ["hi", "hello", "hey", "hyee"]:
        return "Hello! 👋 How can I help you today?"

    # EXIT COMMANDS (Required by PDF)
    elif user_input in ["bye", "exit", "quit", "stop"]:
        return "Goodbye! 👋 Have a great day!"

    # About bot
    elif "your name" in user_input:
        return "I am RuleBot, a rule-based AI chatbot."

    elif "how are you" in user_input:
        return "I'm doing great! Thanks for asking."

    # AI Questions
    elif "what is ai" in user_input:
        return "AI stands for Artificial Intelligence."

    elif "what is machine learning" in user_input:
        return "Machine Learning is a subset of AI that enables computers to learn from data."

    elif "what is python" in user_input:
        return "Python is a popular programming language used in AI and software development."

    # Time
    elif "time" in user_input:
        return f"Current time is {datetime.now().strftime('%H:%M:%S')}"

    # Date
    elif "date" in user_input:
        return f"Today's date is {datetime.now().strftime('%d-%m-%Y')}"

    # Mood
    elif "happy" in user_input:
        return "That's wonderful! 😊"

    elif "sad" in user_input:
        return "I hope things get better soon."

    elif "stressed" in user_input:
        return "Try taking a short break and staying organized."

    # Help
    elif "help" in user_input:
        return """
Commands you can try:
• Hello / Hi
• What is AI / Python / Machine Learning
• Time / Date
• How are you
• I am happy / sad
• **Bye / Exit / Quit**
"""

    else:
        return "Sorry, I don't understand that. Type 'help' to see what I can do!"