# Creat by htb
# Date: 20/02/2023

""" Interview Questions - 1 """
# How to find the sum of 'digits' of a positive integer number using recursion?
def sumOfDigits(num):
    assert num >= 0 and int(num) == num, 'The number must be positive integer only!'
    if num == 0:
        return num
    else:
        return (num % 10) + sumOfDigits(num//10)
# number = input()
num = int(123)
print('the sum of digits of a positive integer number %d: %d'  %(num, sumOfDigits(num)))
        
##################################################################################

""" Interview Question - 2 """    
# How to calculate power of a number using recursion?
def powerOfNumber(base, exp):
    assert base >= 0 and int(exp) == exp, 'The number must be positive integer only!'
    if exp < 0:
        return 1/base * powerOfNumber(base, exp +1)
    elif exp == 0:
        return 1
    else:
        return base * powerOfNumber(base, exp - 1)
print('the power of a number is: ' ,powerOfNumber(2, -1))

##################################################################################

""" Interview Question - 3 """
# How to find GCD ( Greatest Common Divisor) of two numbers using recursion?
# I will explain the steps to find the GCD of 2 number
# Ex: GCD(20, 12)
# Step 1: 20 % 12 = 1 and remainder 8
# step 2: 12 % 8 = 1 and remainder 4
# Step 3: 8 % 4 = 2 remainder 0 => so GCD(20, 12) = 4 

def GCD(num1, num2):
    assert int(num1) == num1 and int(num2) == num2, 'The number must be positive integer'
    if abs(num1) > abs(num2):
        if num1 % num2 == 0:
            return abs(num2)
        else:
            return GCD(num2, (num1 % num2))
    elif abs(num1) < abs(num2):
        if num2 % num1 == 0:
            return abs(num1)
        else:
            return GCD((num2 % num1), num1)
    else:
        return num1
print(GCD(-18,-48))

""" Interview Question - 4 """
# How to convert a number from Demical to Binary using recursion
# I will explain the steps, for example convert 13 to binary
# step 1: 13 / 2 = 7 and remainder 1 (LSB)
# Step 2: 7 / 2 = 3 and remainder 1 
# Step 3: 3 / 2 = 1 and remainder 1
# Step 4: 1 / 2 = 0 
# So convert 13 to binary will be 0111
 
def DemicaltoBinary(Dec):
    # assert Dec >= 0 and int(Dec) == Dec, 'The number must be positive integer'
    if Dec == 0:
        return 0
    else:
        return (Dec % 2) + 10 * DemicaltoBinary(Dec // 2)
print(DemicaltoBinary(123))
print(1 // 2)