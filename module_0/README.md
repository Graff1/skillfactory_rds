## **The Problem**

The main aim of this task is to create the algorithm that
can guess some provided number with a minimun number of attempts.


## **The Solution**

Ther are a lot of ways to create it , we'll provide three versions to
be ablle compare and decide the better one.

The main idea after the alogrithm provided in the task - to use 
the binary search algorithm  that finds the position of a target value 
within a sorted array.Binary search compares the target value to the
middle element of the array. If they are not equal, the half in which
the target cannot lie is eliminated and the search continues on the
remaining half, again taking the middle element to compare to the 
target value, and repeating this until the target value is found. 
If the search ends with the remaining half being empty, the target 
is not in the array.[(Wikipedia)](https://en.wikipedia.org/wiki/Binary_search_algorithm "Binary search algorithm") 