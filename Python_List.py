# Created by htb on 03/04.2023
# Copyright 2023 AppMillers. All rights reserved

# 1. accessing/ Traversing the list

shoppingList = ['Milk', 'Cheese', 'Butter']
print(shoppingList[0])

for i in shoppingList:
    print(i)
    
# 2. Update/ Insert - List

MyList = [1, 2, 3, 4, 5, 6]
MyList.insert(0, 2)
print(MyList)

# 3. Slice/ delete from a list
MyList.pop(2) #delete the element from right to left
print(MyList)

del MyList[3] # delete the element with the index
print(MyList)

MyList.remove(2) # delete the element from left to right
print(MyList)

# 4. Searching for an element in the list

def SearchingList(List, value):
    for i in List:
        if i == value:
            return List.index(value)
    return 'the value does not exit'

print(SearchingList(MyList, 5))

# String and List

a = 'This course so great!'
b = list(a)
print(b)
delimiter = ' '
b = a.split(delimiter)
print(b)

a=[1,2,3,4,5,6,7,8,9]
a[::2]=10,20,30,40,50
print(a)