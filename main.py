from random import random
from random import randint
from random import choice
from module.print_functions import print_function
from module.quiz import answer_question
from module.topic import choose_topic
from module.input import user_input


def main():
    print_function("welcome")
    name = user_input()
    rounds = 1
    round_num = 1
    score = 0
    while round_num <= rounds:
        print_function("round", round_num, rounds)
        topic = choose_topic(name)
        is_answer_correct = answer_question(name, topic)
        if is_answer_correct:
            print_function("answer_correct")
            score = score + 1
        else:
            print_function("answer_incorrect")
        round_num = round_num + 1
    print_function("score", score=score)
    print_function("exit")


if __name__ == "__main__":
    main()
