# Creat by: htb
# Date: 19/03/2023

""" the Fibonacci sequence is the sequence in which number is the sum of preceding ones
    f(n) = f(n - 1) + f(n - 2)"""

def fibonacci(n):
    # assert n > 0 and int(n) == n, 'the number must be positive integer only!'
    if n in [0, 1]:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))
