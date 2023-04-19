def print_function(category, round_num=None, total_rounds=None, score=None):
    if category == "welcome":
        print("\n")
        print("##################################################################################################")
        print("Welcome to this interactive Quiz game. Simply follow the instructions and have fun!")
        print("##################################################################################################")
        print("\n")
    elif category == "round":
        print("\n")
        print(f"### Welcome to round {round_num} of {total_rounds} ###")
    elif category == "end":
        print("\n")
        print("##################################################################################################")
        print("Game over. Do you want to play again?")
        print("##################################################################################################")
        print("\n")
    elif category == "correct_answer":
        print("Correct answer! Player receives a point.")
    elif category == "wrong_answer":
        print("Wrong answer. Player unfortunately does not receive a point.")
        print("\n")
    elif category == "again":
        print("Let's ")
    elif category == "exit":
        print("Exiting program.")
    elif category == "score":
        print(f"Your score is: {score}")
