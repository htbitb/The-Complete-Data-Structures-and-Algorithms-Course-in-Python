# Creat by htb on 02/04/2023
# Practice Array Copyright 2020 AppMillers. All rights reserved
from array import *

# 1. Creat an array and traverse. 

My_Array = array('i', [1,2,3,4,5])

for i in My_Array:
    print(i)
    
# 2. Access individual elements through indexes

print("Access to the first element of array:My_Array[0] = ", My_Array[0])

# 3. Append any value to the array using append() method

My_Array.append(6)
print("add more element to the array: ", My_Array)

# 4. Insert value in an array using insert() method

My_Array.insert(0, 11)
print("exchange the first element from 1 to 11: My_Array[0] = ", My_Array[0])

# 5. Extend python array using extend() method

My_Array2 = array('i', [7,8,9])
My_Array.extend(My_Array2)
print("Extend the old array with more element: ",My_Array)

# 6. Add items from list into array using fromlist() method

templist = [10, 11, 12]
My_Array.fromlist(templist)
print("Add more element from lít to my aray: ",My_Array)

# 7. Remove any aray element using remove() method

My_Array.remove(11) # from left to right, which is the first value will be deleted
print("Delte element in aray: ", My_Array)

# 8. Remove last array element using pop() method

My_Array.pop()
print("The last element has been deleted: ", My_Array)

#9. Fetch any element through its index using index() method

print("Return the index of the element: ",My_Array.index(3))

# 10. Reverse a python aarray using reverse() method

My_Array.reverse()
print("the arrat has been reversed: ", My_Array)

# 11. Get array buffer information through buffer_info() method

print(My_Array.buffer_info())

# 12. Check for number of occuurences of an element using count() method

print("How many time that element appear in array: ", My_Array.count(11))

# 13. Convert array to string using tostring() method

strTemp = My_Array.tobytes()
print("Change the array into string: ", strTemp)
ints = array('i')
ints.frombytes(strTemp)
print("change string into array: ", ints)

# 14. Convert array to a python list withh same elements using tolist() method

# print(My_Array.tolist())

# 15. Slice Elemetns froma n array 
print("Slice the elemtent: ", My_Array[1:4])