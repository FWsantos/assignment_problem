# Assignment Problem

Implementation of the Hungarian O(n^3) Algorithm in Python.
Linearization method for the quadratic problem.

## Prerequisites
- python >= 3.10
- poetry >= 1.7

## Install & Run
This is a poetry project. Poetry is used to install dependencies.
So far, tests are done by editing main.py.
The test() function with parameter 0 tests the assing files and with any other parameter it tests the assingp files. The results are saved in the output.txt and output_big.txt files respectively.
```
git clone https://github.com/FWsantos/assignment_problem.git
cd assignment_problem
poetry shell
poetry install --no-root
python src/main.py
```