from random import choice


def get_questions_and_answers(topic):
    questions_and_answers = {
        "Animals": [
            ("How many eyes does a horse have?", 2),
            ("How many legs does a dog have?", 4),
            ("What is the most common animal in Germany? (1): Dog (2): Cat (3): Pig", 2)],
        "General": [
            ("How many states does Germany have?", 16),
            ("How many female chancellors has Germany had?", 1),
            ("How many planets are there in the solar system?", 9)],
        "Sports": [
            ("How many goals did Germany score against Brazil in the 2016 World Cup?", 7),
            ("How many FIFA World Cup titles has Germany won?", 4),
            ("How many singles tournaments did Boris Becker win? (1): 17 (2): 49 (3): 71", 2)]
    }
    question_and_answer = choice(questions_and_answers[topic])
    return question_and_answer


def answer_question(name: str, topic: str) -> bool:
    question_and_answer = get_questions_and_answers(topic)
    question = question_and_answer[0]
    correct_answer = question_and_answer[1]
    print(f"--- {name}, please answer the following question: ---")
    print(question + "\n")
    while True:
        try:
            user_answer = int(input("Enter a whole number from 0-100: "))
            break
        except:
            print("\nInvalid input. Please make sure to enter a number. Try again. \n")
    if user_answer == correct_answer:
        print("\n--> The answer is correct.")
        return True
    else:
        print(f"\n--> The answer is incorrect. The correct answer is: {correct_answer}")
        return False