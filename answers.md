# CITS2200 Lab 1: Sorting and Searching

Name: YOUR NAME

Student Number: 23XXXXXX


## Question 1 (1 mark)
Write a short paragraph explaining the relationship between this problem and more abstract computer science topics we have covered in class.

We have covered the topics some of which I have implemented in speedrunning. Making classes and objects in python allow us to encapsulate data and make the code reusable. Insertion sorting algorithm used for sorting in leader board and for searching linear search algorithm is used which is a basic example of complexity analysis we can further enhance the code by using efficient algorithm like merge sort and binary search.


## Question 2 (1 mark)
What data do you need to store in the `Leaderboard` class?
What algorithm do you intend to use for each method?

The Leaderboard class maintains a list of tuples that store both the runner's name and their completion time.

Algorithm I  have used for searching is linear search and for sorting is insertion sort 

## Question 3 (5 marks)
Implement your design by filling out the method stubs in `speedrunning.py`.
Your implementation must pass the tests given in `test_speedrunning.py`, which can be invoked by running `python -m unittest`.

See `speedrunning.py`.


## Question 4 (1 mark)
Give an argument for the correctness and complexity of your `__init__()` function.

Correctness of __init__()
The __init__() method properly sets up the run and time

Complexity of __init__()
The insertion run are at their correct place


## Question 5 (1 mark)
Give an argument for the correctness and complexity of your `submit_run()` function.

Correctness of submit_run()
The submit_run() method inserts the new run 

Complexity of submit_run()
while inserting the new run mainting the the sequnce and order of previous runs. Time complexity is O(N)

## Question 6 (1 mark)
Give an argument for the correctness and complexity of your `count_time()` function.

Correctness of count_time()
The count_time() method run a loop and on leaderboard to find count without changing list 

Complexity of count_time()
The time complexity of this operation is O(N), N represents the total number of runs.