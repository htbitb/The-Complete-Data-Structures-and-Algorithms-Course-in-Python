## What is Big O?
- Big O is the language and metric we use to describe the efficiency of algorithms
  -  Time Complexity: A way of showing how the runtime of a function increases as the size of input increase
- Types of Runtimes: O(N), O( $N^2$ ), O( $2^N$ )
\
&nbsp;
 ![](https://i0.wp.com/dotnetsimplified.com/wp-content/uploads/2021/10/image-6.png?w=1222&ssl=1)
\
&nbsp;
- **Big O** : It is a complexity that is going to be less or equal to the worst case.
- **Big - $\Omega$** : It is a complexity that is going to be at least more than the best case
- **Big - $\Theta$** : It is a complexity that is within bounds of the worst and the best case 
## Runtime Complexities
|Complexity|Name|Sample|
|----------|----|------|
|O(1)|Constant|A simple and numbers function|
|O(N)|Linear|Loop through numbers from 1 to n|
|O(LogN)|Logaithmic|Find an element in sorted array|
|O($N^2$)|Quadratic|Nested Loops|
|O($2^N$)|Exponential|Double recursion in Fibonacci|

- **O(1)** : This means that for any given input, the execution will not change. It will remain constatn.
``` python
def multiply_numbers(n):
    return n*n
```


- **O(n)** : this mean time complexity will grow in direct proportion to the size of input data
``` python
def print_items(n):
  for i in range(n):
    print(i)
```
- **Drop ContantCon** : i in the program haa moe than 1 for loop, the complexity will be O(2n) -> O(N)
  - It is very possible that O(N) code is faster than O(1) code for specific inputs 
  - Different computers with different architectures have different constant factors.
  - Different algorithms with the same basic idea and computational complexity might have slightly different constants
    ```
    Example: a*(b-c) vs a*b - a*c
    ```
- **O($n^2$)**:
```python
def print_items(n): # the complexity here is O(N)
  for i in range(n): # the complexity here is O(N)
    for j in range(n):
      print(i , j)
```    
- **O(_logN_)**: to find a number in the array, for example from 1 to 8 you have to find where is 8 stored
```
[1][2][3][4][5][6][7][8] divide this array into 2 parts
[1][2][3] | [5][6][7][8] here, 8 is the second part
continuous divide the array and find the number 8
```
So it is not going to be as flat as O(1), but it is very flat and efficient compared to O(n) and O($n^2$) complexity