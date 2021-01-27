import nltk 
import sys
import os
import string
import math
from data import loadData as data # data directory is where we have the functions defined to curate data.
from tfidf import tfidf as tfidf
FILE = 1
SENTENCES = 1

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
    file_idfs = compute_idfs(file_words)

    # Prompt user for query
    query = set(tokenize(input("Query: ")))
    marking = None
    while type(marking) == int:
        marking = input("Marking: ")

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=marking)

    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = compute_idfs(sentences)

    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
    for match in matches:
        print(match)























if __name__=="__main__":
    main()
