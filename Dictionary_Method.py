# Created by htb in 26/04/2023
# Copyright 2020 AppMiller. All rights reserved.

# 1. Clear()

myDict = {'name': 'Edy', 'age': 26, 'address': 'London', 'Education': 'master'}
myDict.clear() # clear all the elemnet in the dictionary
print(myDict)

# 2. copy()
myDict_1 = {'name': 'Edy', 'age': 26, 'address': 'London', 'Education': 'master'}
dict = myDict_1.copy() # copy all the element in the base line dictionary
print(dict)

# 3. fromkeys()
newDict = {}.fromkeys([1,2,3], 0)
print(newDict) # create new dictionary

# 4. get ()

print(myDict_1.get('age', 27)) #if the key does not exist in the dictionary, it will be returned the value

# 5. item()
print(myDict_1.items())

# 6. Key()
print(myDict_1.keys())

# 7. setdefault()
print(myDict_1.setdefault('name', 'added'))

# 8. values()
print(myDict_1.values())

# 9. update()
myDict_1.update(newDict)
print(myDict_1)