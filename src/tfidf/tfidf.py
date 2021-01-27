import nltk
import sys
import string
import os
import math

def compute_idfs(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.

    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """
    counts = {} # counts the presence of a given word
    idfs = {}
    num_docs = len(documents)
    # counting the the occurance of indivisual words
    for doc in documents:
        for word in set(documents[doc]): 
            if word in counts.keys():
                counts[word] += 1
            else:
                counts[word] = 1
    # calculating the idf value for indivisual words
    for word, value in counts.items():
        idfs[word] = math.log( (num_docs / value) )


def tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.

    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """
    final_words = []
    avoided_words = [] # WORDS WHICH ARE TO BE AVOIDED IN THE FINAL LIST
    
    # making the avoided_words list
    for word in string.punctuation: # the string library has a string of punctuations
        avoided_words.append(word)
    for word in nltk.corpus.stopwords.words("english"): # the nltk lib. has a list of stopwords commonly used in english
        avoided_words.append(word)

    tokens = nltk.word_tokenize(document)

    # filtering the tokens
    for token in tokens :
        if token not in avoided_words:
            final_words.append(token.lower())

    return final_words
    