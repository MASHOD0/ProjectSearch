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
    :param input: documents to compute idfs from
    :return: idfs
    """
    counts = {} # counts the presence of a given word
    idfs = {}
    num_docs = len(documents)
    # counting the the occurance of indivisual words
    for doc in documents:
        if documents[doc] != None:
            for word in documents[doc]: 
                if word in counts.keys():
                    counts[word] += 1
                else:
                    counts[word] = 1
    # calculating the idf value for indivisual words
    for word, value in counts.items():
        idfs[word] = math.log( (num_docs / value) )
    return idfs


def top_files(query, files, idfs, n):
    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    :param query: set of words
    :param files: Dict maping names of files to a list of words
    :param idfs: Dict mapping words to idf values 
    :param n: no of files to return
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

def top_sentences(query, sentences, idfs, n):
    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to idf. If there are ties, preference should
    be given to sentences that have a higher query term density.
    :param query: set of words
    :param sentences: Dict of sentences mapped to words
    :param idfs: Dict of words mapped to idf values
    :param n: Number of sentences to return
    """
    
    sentence_idf = {}
    idf_sum = 0 
    density = 0
    density_to_idf = {}

    for sentence in sentences:
        for word in query:
            if word in sentences[sentence]:
                idf_sum = idf_sum + idfs[word]
                density += 1
            else:
                continue
        if density != 0:
            length = len(sentences[sentence])
            density = density /length
            sentence_idf[sentence] = (idf_sum , density)
            density = 0
            idf_sum = 0
    sentence_idf = sorted(sentence_idf , key = lambda k:(sentence_idf[k][0],sentence_idf[k][1]), reverse = True)        
    return sentence_idf[:n]   