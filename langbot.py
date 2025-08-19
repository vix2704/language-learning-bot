# language_bot.py
import language_tool_python


tool = language_tool_python.LanguageTool('fr')  


vocab_tips = {
    "faim": "means 'hungry'",
    "merci": "means 'thank you'",
    "bonjour": "means 'hello/good day'",
    "chat": "means 'cat'"
}

def correct_grammar(sentence):
    matches = tool.check(sentence)
    corrected = tool.correct(sentence)
    return corrected, matches

def get_vocab_tip(sentence):
    tips = []
    words = sentence.lower().split()
    for w in words:
        if w in vocab_tips:
            tips.append(f"'{w}': {vocab_tips[w]}")
    return tips

def chatbot():
    print("LinguaBot 🤖: Hello! Let's practice French. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("LinguaBot 🤖: Au revoir! Keep practicing!")
            break
        
        # Grammar correction
        corrected, matches = correct_grammar(user_input)
        if user_input != corrected:
            print(f"LinguaBot 🤖: I think you meant: '{corrected}'")
        
        # Vocabulary tips
        tips = get_vocab_tip(user_input)
        if tips:
            print("LinguaBot 🤖: Vocabulary tips:")
            for t in tips:
                print("  -", t)
        
        # esponse
        print("LinguaBot 🤖: Good job! Keep practicing.")

if __name__ == "__main__":
    chatbot()
