def choose_topic(name_with_greeting):
    topic_list = ["addition", "multiplication", "division"]
    topics_string = ", ".join(topic_list)
    while True:
        topic = input(f"{name_with_greeting} - Choose one of the following topics ({topics_string}): ")
        print("\n")
        if topic not in topic_list:
            print("The input value is not valid. Please make sure to enter a valid topic name.")
        else:
            break
    return topic
