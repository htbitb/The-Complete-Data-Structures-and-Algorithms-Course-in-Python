# Pytohn Lists
## What is a List? 
A list is a data structure that holds an ordered collection of items
## How to create it?
```python
integers = [1, 2, 3, 4]
string_list = ['Milk', 'Cheese', 'Butter']
```
## Time and Space complexity in Python List

|Operation |Time complexity|Space complexity|
|--|--|--|
|Creating a list| O(1) | O(n)|
|InertinInsa value in alist|O(1)/O(n)| O(1)|
|Traversing a given list|O(n)|O(1)|
|Accessing a given cell| O(1)|O(1)|
|Searching a given value|O(n)|O(1)|
|Deleting a given value|O(1)/O(n)|O(1)|

## List Inverview Quetions

- **Question 1:**
What will be the ouput of the following code snippet?
```python 
def f(value, values):
    v = 1
    values[0] = 44
t = 3
v = [1, 2, 3]
f(t, v)
print(t, v[0])
```
- **Question 2:**
What will be the output if the following code block?
```python
data = [[1, 2], [3, 4], [[5, 6], [7, 8]]]
def fun(m):
    v = m[0][0]
    for row in m:
        for element in row:
            if v < element: v = element
    return v
print(fun(data[0]))
```
- **Question 3:** What will be the ouput of hte following code block?
```python 
a=[1,2,3,4,5,6,7,8,9]
print(a[::2])
```
- **Question 4:** What will be the output of the following code block?
```python
fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
fruit_list2 = fruit_list1
fruit_list3 = fruit_list1[:]
 
fruit_list2[0] = 'Guava'
fruit_list3[1] = 'Kiwi'
 
sum = 0
for ls in (fruit_list1, fruit_list2, fruit_list3):
    if ls[0] == 'Guava':
        sum += 1
    if ls[1] == 'Kiwi':
        sum += 20
 
print(sum)
```