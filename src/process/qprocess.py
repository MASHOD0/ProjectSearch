def filter(question):
    for word in question:
        filtered_words = ["how","what"]
        if word in filtered_words:
            question.pop(word)