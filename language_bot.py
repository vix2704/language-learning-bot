import json
import random

def load_words():
    with open("words.json", "r", encoding="utf-8") as f:
        return json.load(f)

def quiz(language, words):
    print(f"\nTranslate the given words/phrases into {language.capitalize()}.")
    print("Type 'exit' to leave.\n")

    phrases = list(words.keys())
    correct = 0
    total = 0

    while True:
        phrase = random.choice(phrases)
        answer = input(f"Phrase: {phrase} → ")

        if answer.lower() == "exit":
            break

        total += 1
        if answer.strip().lower() == words[phrase].lower():
            print("✅ Correct!\n")
            correct += 1
        else:
            print(f"❌ Wrong. Correct answer: {words[phrase]}\n")

    print(f"\nYour score: {correct}/{total}")
    print("Thank you for practicing!\n")

def main():
    words = load_words()
    print("Hello, press 1 to practice French or 2 to practice German ?")
    choice = input("Enter your choice: ")

    if choice == "1":
        quiz("french", words["french"])
    elif choice == "2":
        quiz("german", words["german"])
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
