import nltk 
import sys
from data import loadData as data 
from process import tfidf as tfidf
from process import qprocess as qprocess
#FILE = 4
#SENTENCES = 4

def main():
    """
    This is the main function which links all the other functions to run the program.
    """    
    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python src/main.py corpus")

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
    while True:
        try:
            while type(marking) != int:
                marking = int(input("Marking: "))
        except Exception as e:
            print("Please enter a valid integer")
        if type(marking) == int:
            break
        

    # Determine top file matches according to TF-IDF
    filenames = tfidf.top_files(query, file_words, file_idfs, marking)

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
    matches = tfidf.top_sentences(query, sentences, idfs, marking)
    for match in matches:
        print(match)

if __name__=="__main__":
    main()
