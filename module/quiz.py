from random import choice


def get_questions_and_answers(topic):
    questions_and_answers = {
        "addition": [
            ("1 + 100 - 4", 97),
            ("1001 -4 + 3", 1000),
            ("79 -3 + 12", 88)],
        "multiplication": [
            ("7 * 3", 21),
            ("100 * 0.91", 91),
            ("6 * 11", 66)],
        "division": [
            ("200 / 20", 10),
            ("77 / 7", 11),
            ("30 / 2", 15)]
    }
    question_and_answer = choice(questions_and_answers[topic])
    return question_and_answer


def answer_question(name: str, topic: str) -> bool:
    question_and_answer = get_questions_and_answers(topic)
    question = question_and_answer[0]
    correct_answer = question_and_answer[1]
    print(f"--- {name}, What is the result of following math equation: ---")
    print(question + "\n")
    user_answer = input("Enter a whole number from 0-100: ")
    if user_answer == correct_answer:
        print("\n--> The answer is correct.")
        return True
    else:
        print(f"\n--> The answer is incorrect. The correct answer is: {correct_answer}")
        return False