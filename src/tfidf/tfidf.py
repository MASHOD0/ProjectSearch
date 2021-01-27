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


def top_files(query, files, idfs, n):
    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    """
    
    tfidf = {}
    for file in files:
        tfidf[file] = 0
        tokens = len(files[file])
        for word in query:
            if word in files[file]:
                freq = files[file].count(word) + 1
            else:
                freq = 1
            tf = freq / tokens
            if word in idfs.keys():
                idf = idfs[word]
            else: 
                idf = 1
            tfidf[file] = tf * idf

    top_files = sorted(tfidf , key=tfidf.get, reverse = True)
    return top_files[:n]

    