import nltk 
import sys
import os
import string
import math
from data import loadData as data 
from tfidf import tfidf
FILE = 4
SENTENCES = 4

def main():
    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    files = data.load_files(sys.argv[1])
    file_words = {
        filename: data.tokenize(files[filename])
        for filename in files
    }
    file_idfs = tfidf.compute_idfs(file_words)

    # Prompt user for query
    query = set(data.tokenize(input("Query: ")))
    marking = None
    while type(marking) == int:
        marking = input("Marking: ")

    # Determine top file matches according to TF-IDF
    filenames = tfidf.top_files(query, file_words, file_idfs, n=marking)

    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = data.tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = tfidf.compute_idfs(sentences)

    # Determine top sentence matches
    matches = tfidf.top_sentences(query, sentences, idfs, n=SENTENCES)
    for match in matches:
        print(match)























if __name__=="__main__":
    main()
