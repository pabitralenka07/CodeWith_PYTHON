questions = {
    "What is the capital of France?": "paris",
    "Which planet is known as the Red Planet?": "mars",
    "What language is this?": "python"
}


def ask_question(question, answer):
    user_answer = input(f"{question} ").strip().lower()
    return user_answer == answer


score = 0

for q, a in questions.items():

    if ask_question(q, a):
        print("Correct!")
        score += 1
    else:
        print(f"Nope! The answer was {a}.")


print(f"\nYour final score: {score}/{len(questions)}")
