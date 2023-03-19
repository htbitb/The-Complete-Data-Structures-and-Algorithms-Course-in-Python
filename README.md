<!-- Heading -->
## What is Recursion?
- Recursion = a way of solving a problem by having a function calling itself
- Performing the same operation multiple times with the different inputs
- In every step we try smaller inputs to make the problem smaller
- Base condition is needed to stop the recursion, otherwise infinite loop will occur.
``` python
def openRussianDoll(doll):
    if doll == 1:
        print("All doll is opened")
    else:
        openRussianDoll(doll - 1)
```
# Why Recursion?
1. Recursive thinking is really important in programming and it helps you break down big problem into smaller ones and easier to use
- when to choose recursion?
    - If you can drive the problem into similar sub problem
    - Design an algorithm to computer nth...
    - write code to list the n...
    - Implement a method to compute all.
    - Practice
2. The prominent usage of recursion in data structures like trees and graph
3. Interviews
4. It is used in many algorithms (divide and conquer, greedy and dynamic programming)
## How Recursion works?
1. A method calls it self
2. Exit from infinite loop
``` python
def recursionMethod(parameters): 
    if exit from condition satisfied: # Condition to exit the recursion
        return some value
    else:
        recursiveMethod(modified parameters) # it call itself
```
## Recursive vs Iterative Solution
### Recursive
```python
def powerOfTwo(n):
    if n ==  0:
        return
    else:
        power = powerOfTwo(n - 1)
        return power + 2
```

### Iterative
```python
def powerOfTwo(n):
    i = 0 
    power = 1
    while 1 < n:
        power = power + 2
        i = i + 1
    return power
```
| Points | Recursive | Iteration | |
| ------ | --------- | ----------|---|
| Space efficient?| No | Yes | No stack memory require in case of iteration |
| Time efficient? | No | Yes | In case of recursion system needs more time for pop and push elements to stack memory which makes recursion less time efficient |
| Easy to code? | Yes | No | We use recursive especially in the cases we know that a problem can be divide into similar sub problem|

## When Use/Avoid Recursion?
- **When to use it?**
  - when we can easily breakdown a problem into similar subproblem
  - when we are fine with extra overhead (both time and space) that comes wiht it
  - When we need a quick working solution instead of efficient one
  - When traverse a tree
  - When we use memoization in recursion 
- **When avoid it?**
  - If time and space complexity matters for us
  - Recursion uses more memory. If we use embedded memory. For example an application that takes more memory in the phone is not efficient
  - Recursion can be slow  