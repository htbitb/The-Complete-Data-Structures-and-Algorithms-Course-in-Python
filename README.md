<!-- Heading -->
# The Complete Data Structures and Algorithms Course in Python

## What is a Data Structure?
- Data Structures are different ways of organizing data on your conputer, that can be used effectively
## What is an Algorithm?
- Algorithms in Computer Science: Set of rules for a computer prograrm to accomplish a Task

``` mermaid
flowchart TD
    A[Input Data]-->B[Calculation];

    B[Calculation]-->C[Stop When answer found]
```

### What makes a good algrithms?
- Correctness
- Efficiency 

### Type of Data Strucures

``` mermaid
graph TD
A[Data Structure] --> B[Primitive]
A[Data Structure] --> C[Non Primitive]

B --> D[Integer \n Float \n Character \n String \n Boolean ];
C --> E[Linear];
C --> F[Non Linear];
E --> G[Static];
G --> H[Array];
E --> J[Dynamic];
J --> K[Linked List \n Stack \n Queue];
F --> L[Tree \n Graph];
```
### Types of Algorithms
- Simple recursive algorithms
- Divide and conquer algorrithms
- Dynamic programming algorithms
- Greedy algorithms
- Brute force algorithms
- Ramdomized algorithms
\
&nbsp;

_**Simple recursive algorithms**_:

``` javascript
Algorithm Sum(A, n)
    if n = 1
        return A[0]
    s = Sum(A, n-1) /* recure on all but last */
    s p s + A[n-1] /* add last element */
return s
```
\
&nbsp;
_**Divide and conquer algorithms:**_
```
- Divide the problem into smaller subproblems of the same type, and solve these subproblems recursively
- Combine the solution to the subproblems into a solution to the original problem
```
\
&nbsp;
_**Dynamic programming algoritms:**_
```
- They work based on memoization
- To find the best solution
```
\
&nbsp;
_**Greedy algorithms:**_
```
- We take the best we can without about future consequence.
- We hope that by chosing a local optimum solution at each step, we will end up at a global optimum solution
```
\
&nbsp;
_**Brute force algorithms:**_
```
- It simply all possible until a satisfactory solution is found
```
\
&nbsp;
_**Randomized algorithms:**_
```
- Use a random number at least once during the computation to make a decision
```

### Lecture Notes

[Click here to get the document about Data Structure and Algorithms in Python](https://docdro.id/JQpxdhI)
\
&nbsp;
### Acknowledgements
- [UDEMY](https://www.udemy.com/course/data-structures-and-algorithms-bootcamp-in-python/)
