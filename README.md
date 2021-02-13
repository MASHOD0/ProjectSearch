# ProjectSearch
This is a pseudo-search engine which goes through notes and gives answers to questions.
This project is work in progress(the code works).
We expect to make a python program which takes notes in `.txt` format and ask for questions and answer them.

## Instructions to run the code
1. Make a python virtual environment by running this command in the terminal.
```
python3 -m venv venv
```
2. Activate the virtual environment by running this command
```
source venv/Scripts/activate
```
3. Install all the required packages by running this command
```
pip3 install requirements.txt
```
4. Run the code by running this command.
```
python3 src/main.py corpus
```

## Directory structure  
-     `src/`____|_____`data/`
-               |
-               |
-               |_____ `process/`
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-

### `src/` directory
- `src/` directory has `main.py` and two other directories `data/` and `process/`
### `data/` directory
- It has `data.py` and the `corpus/` directory
### `process/` directory 
- It has two files `tfidf.py` and `qprocess.py`

## files
We have 4 scripts as of now 
- `main.py`
- `data.py`
- `tifidf.py`
- `qprocess.py`

### `main.py`
- It is the main script which links all other files

### `data.py`
- It has functions to curate the data , to search from 

### `tfidf.py`
- It has the functions to find the results.

### `qprocess.py`
- It has the funtions to filter the questions to provide better answers.
<!--
## Current Deliverables
- [x] take an input from `.txt` files and 
- [x] take questions as input and also the marking for the question
- [x] make a tf-idf algorithm to rank the sentences
- [x] and return those sentences
-->
<!--
## Deadline 
 We expect to complete this project before March 2021
-->
