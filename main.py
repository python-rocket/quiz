from random import random
from random import randint
from random import choice
from module.print_functions import print_function
from module.salutation import get_salutation
from module.csv import read_ranking
from module.csv import write_ranking
from module.quiz import answer_question
from module.topic import choose_topic
from module.input import user_input


def main():
    print_function("welcome")
    read_ranking()
    name = user_input()
    rounds = 2
    round_num = 1
    score = 0
    while round_num <= rounds:
        print_function("round", round_num, rounds)
        name_with_salutation = get_salutation(name)
        topic = choose_topic(name_with_salutation)
        is_answer_correct = answer_question(name_with_salutation, topic)
        if is_answer_correct:
            print_function("answer_correct")
            score = score + 1
        else:
            print_function("answer_incorrect")

        if round_num < rounds:
            input("Press Enter for the next round")
            round_num = round_num + 1
        else:
            print_function("score", score=score)
            write_ranking(name, score)
            print_function("end")
            play_again = input("To play again, enter the capital letter 'Y'. To exit, enter any other letter: ")
            if play_again == "Y":
                main()
            else:
                round_num = round_num + 1

    print_function("exit")


if __name__ == "__main__":
    main()
