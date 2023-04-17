# Created by htb on 07/04/2023
# Copyright 2020 AppMillers. All rights reserved.

# Questin 1 - Missing number
# How to find the missing number in an integer array of 1 to 100?

# create a list from 1 to 100 and miss random number

def findmiss(list):
    sum = 100*101/2
    sum_list = sum(list)
    print(sum - sum_list)
    
#---------------------------------------------------------------#

# Question 2 - Pairs/ Two Sum
# write a program to find all pairs of integers whose sum is equal to given number
list = [1, 2, 3, 4, 5, 6]

def findpairs(list, num):
    for i in range(0, len(list)):
        for j in range(i+1, len(list)):
            pair = list[i] + list[j]
            if pair == num:
                 print(i, j)
            
findpairs(list, 9)

# Question 3 - How to check if an array contains a number in Python
import numpy as np

myArray = np.array([4, 2, 1, 4, 2, 8, 7])
print(myArray)
def findnumber(array, number):
    array.sort()
    if number < array[len(array) // 2]:
        for i in range(0, len(array) // 2):
            if array[i] == number:
                
                print(i)
    elif number > array[len(array) // 2]:
        for i in range (len(array) // 2, len(array)):
            if array[i] == number:
                print(i)
    else: print(len(array) // 2)
    
findnumber(myArray, 8) 

# Question 4 - How to find maximum products of two integers in array which all element are postitive

array = [11, 10, 27, 9, 14, 16, 48]
pairs = []
def Max_product(array):
    temp = 0
    for i in range(0, len(array) - 1):
        for j in range(i, len(array)):
            if temp < (array[i] * array[j]):
                temp = array[i] * array[j]
                pairs = str(array[i]) + " " + str(array[j])
    print(pairs)
    print(temp)

Max_product(array)

# Question 5 - is unique: Implement an algorithm to determine if a list has all unique characters, using python list.

my_list = [1, 20, 30, 44, 5, 56, 57, 8, 11, 10, 31, 12, 13, 14, 35, 16, 27, 58, 19, 21]

def isUnique(list):
    temp = []
    for i in list:
        if i in temp:
            print(i)
            return False
        else:
            temp.append(i)
    
print(isUnique(my_list))

# Question 6 - Permutation

def permutation(list1, list2):
    if len(list1) != len(list2):
        return False
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    else:
        return False

List1 = [1,2,3]
List2 = [3,2,1]
print(permutation(List1, List2))

# Question 7 - Rotate Matrix: Given an matrix NxN, write a mrthod to rotate the matrix by 90 degrees

import numpy as np

myArray = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(myArray)
temp = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
def rotate_matrix(matrix):
    n = len(matrix)
    for i in range(0, n):
        first = i
        last = n - i - 1 
        for j in range (0, n):
            temp[j][first] = matrix[last][j]
    print(temp)
    
rotate_matrix(myArray)