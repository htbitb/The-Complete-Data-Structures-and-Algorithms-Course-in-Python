# Creat by htb on 02/04.2023
# Coppyright 2020 AppMillers. All rights reserved

import numpy as np

# 1. Create a two dimensional array
twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8]])
print(twoDArray)

# 2. Insert new value for an Array
New_Two_DAray = np.insert(twoDArray, 0, [[1, 2, 3, 4]], axis=0)
print(New_Two_DAray)

# 3. Accessing an element of two dimensional array

def accessElements(array, rowindex, colIndex):
    if rowindex >= len(array) or colIndex >= len(array[0]):
        print('Incorrect index')
    else:
        print(array[rowindex][colIndex])
        
accessElements(twoDArray, 2, 3)

# 4. Traversal - Two Dimensional Aray

def TraverseTDArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])
TraverseTDArray(twoDArray)
print(len(twoDArray[0]))

# 5. Searching Two dimensional array

def SearchingTDArray(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return 'the value is located at index '+ str(i)+ " " + str(j)
    return 'the element is not exist'

print(SearchingTDArray(twoDArray, 11))

# 6. Deletion - Two dimensional array

newTDArray = np.delete(twoDArray, 1, axis = 1)
print(newTDArray)