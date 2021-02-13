def filter(question):
    """
    This function filters all the unwanted words in the question list
    :param question: the list containing keyords from question
    """
    for word in question:
        if word == None:
            pass
        filtered_words = ["how","what"]
        if word in filtered_words:
            question.remove(word)