# Dictionaries

## What is Dictionaries?
- A dictionary is a collection which is unordered, changeable and indexed.

## How to create a Dictionary?
```python
myDict = dict()
print(myDict)
```
```python
engtoSp = {"one": "uno", "two": "dos", "three": "tres"}
print(engtoSp)
```
## Dictionary in Memory
A **hash table** is a way of doing **key-value lookups**. You store the values in an array, and then use a **hash function** to find the index of the array ceel that correspond to your key-value pair.

![dictionary](D:\Data_Structure_And_Algothim\Python\The-Complete-Data-Structures-and-Algorithms-Course-in-Python\dictionary_hash.png)

## Inert/ Update an element in a Dictionary
```python
myDict = {'name': 'Edy', 'age': 26}
myDict['address'] = 'London'
print(myDict)
```
```
output:
{'name': 'Edy', 'age': 26, 'address': 'London'}
```
## Traversing through a dictionary
```python 
myDict = {'name': 'Edy', 'age': 26, 'address': 'London'}

def traverseDict(dict):
    for key in dict:
        print(key, dict[key])
traverseDict(myDict)
```
```
output:
name Edy
age 26
address London
```
## Search for an element in a Dictionary
```python
myDict = {'name': 'Edy', 'age': 26, 'address': 'London'}

def searchDict(dict, value):
    for key in dict:
        if dict[key] == value:
            return key, value
    return 'the value does not exist'

print(searchDict(myDict, 27))
```