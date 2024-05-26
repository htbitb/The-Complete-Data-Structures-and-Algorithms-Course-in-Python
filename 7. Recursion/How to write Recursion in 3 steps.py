""" Factorial: 
        - It is the product of all positive integer less than or equal to n
        - Denoted by !n
        - Only positive number
        - 0! = 1 
        
    Example: 
        4! = 4*3*2*1 = 24 """

# Step 1: Recursive case - the Flow 
#       n! = n*(n - 1)*(n - 2)*....*1

# Step 2: Base case - the Stopping criterion 
#       0! = 1! = 1

# Step 3: Unintentional case - the constraint


def factorial(n):
    assert n > 0 and int(n) == n, 'The number must be positive integer only!'
    # this assert key word lets you test if the condition in your code return True, if not the
    # program will raise an AssertionError than can be write by ownselves
    if n in [0, 1]:
        return 1
    else: 
        return n * factorial (n - 1)
    
print(factorial(3))