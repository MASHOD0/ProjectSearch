def filter(question):
    for word in question:
        if word in filtered_words:
            question.pop(word)