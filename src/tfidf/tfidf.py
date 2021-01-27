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
