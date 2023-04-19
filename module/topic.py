def verify_topic_input(topic, topic_list):
    if topic not in topic_list:
        print("The input value is not valid. Please make sure to enter a valid topic name.")
        return False
    else:
        return True


def choose_topic(name_with_greeting):
    topic_list = ["Animals", "General", "Sports"]
    topics_string = ", ".join(topic_list)
    while True:
        topic = input(f"{name_with_greeting} - Choose one of the following topics ({topics_string}): ")
        print("\n")
        if verify_topic_input(topic, topic_list):
            break
    return topic
