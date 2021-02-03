# ProjectSearch
This is a pseudo-search engine which goes through notes and gives answers to questions.
This project is work in progress(the code works).
We expect to make a python program which takes notes in `.txt` format and ask for questions and answer them.

## Instructions to run the code
1. make a python virtual environment by running this command in the terminal.
```
python3 -m venv venv
```
2. activate the virtual environment by running this command
```
source venv/Scripts/activate
```
3. install all the required packages by running this command
```
pip3 install requirements.txt
```
4. run the code by running this command.
```
python3 src/main corpus
```

## Directory structure  

### `src/` directory
- `src/` directory has `main.py` and two other directories `data/` and `process/`
### `data/` directory
- it has `data.py` and the `corpus/` directory
### `process/` directory 
- it has two files `tfidf.py` and `qprocess.py`

## files
we have 3 scripts as of now 
- `main.py`
- `data.py`
- `tifidf.py`
- `qprocess.py`




## Current Deliverables
- [x] take an input from `.txt` files and 
- [x] take questions as input and also the marking for the question
- [x] make a tf-idf algorithm to rank the sentences
- [x] and return those sentences

## Deadline 
 We expect to complete this project before March 2021
