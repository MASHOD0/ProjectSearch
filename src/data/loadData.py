import nltk


def load_files(directory):
    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """
    dataDir = os.path.join(os.path.dirname(os.path.abspath(__file__)),directory)  
    info = {} # Dict to store all the information
    file_names = os.listdir(dataDir)
    
    for file in file_names:

        filePath = os.path.join(dataDir, file)
        f = open(filePath, "r", encoding = "utf8")
        info[file] = f.read()
        

    return info


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
    