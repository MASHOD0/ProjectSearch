import string
import nltk

def filter(q_words):
    """
    Filters all the unwanted words in the question list .
    :param question: the list containing keyords from question
    """
    filtered_words = ["how","what"]
    for word in q_words:
        if word in filtered_words:
            q_words.remove(word)

def q_tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.

    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    :param document: string to tokenize
    :return: tokenized list
    """
    final_words = []
    avoided_words = [] # WORDS WHICH ARE TO BE AVOIDED IN THE FINAL LIST
    
    # making the avoided_words list
    for word in string.punctuation: # the string library has a string of punctuations
        avoided_words.append(word)
    for word in nltk.corpus.stopwords.words("english"): # the nltk lib. has a list of stopwords commonly used in english
        avoided_words.append(word)

    tokens = nltk.word_tokenize(document)
