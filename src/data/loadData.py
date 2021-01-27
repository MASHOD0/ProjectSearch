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


