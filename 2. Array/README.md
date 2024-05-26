## What is an Array?
- Array can store data of specified type
- Elements of an array are located in contiguous
- Each elements of an array has a unique index
- the size of an an array is predefined and cannot be modified
## Why do we need an Array?
- In computer science, an Array is a data structure consisting of a collection of elements, each identified by at least one array index or key. An array is stored such that the position of each element can be computed from its index by a mathematical formula.
## Types of Array
- **One dimension array**: an array with a bunch of values having been declared with a single index
**a[i] -> i between 0 and n**

|5|4|10|11|8|11|68|87|12|
|:-----|-----|---|----|----|----|---|---|----:|
|[0]|[1]|[2]|[3]|[4]|[5]|[6]|[7]|[8]|

so when access to a[2] it will be 10

- **Two dimensional array**: an array with a bunch of values having been declared with double index
**a[i][j] -> i and j between 0 and n**

||[0]|[1]|[2]|[3]|[4]|[5]|[6]|[7]|[8]|
|:-----|---|--|---|----|----|----|---|---|----:|
|**[0]**|1|33|55|91|20|51|62|74|13|
|**[1]**|5|3|5|9|0|1|2|4|13|
|**[2]**|1|3|55|1|2|5|6|7|3|

- **Three dimensional array**: an array with a bunch of values having declared with triple index.
**a[i][j][k] -> i, j and k between 0 an n**

## Creating an array
- **When we create an array, we**:
    - Assign it to a variable
    - define the type of elements that it will store
    - define its size (the maximum numbers of elements)
## Creating an Array
```python
from array import*
arrayName = array(typecode, [Initializers])
```
## Insert, when array is full
```python
from array import *
arr1 = array('i', [1,2,3,4,5,6])

arr1.insert(6, 7)
```
## Delete element in array
```python
from array import *
arr1 = array('i', [1,2,3,4,5,6])

arr1.remove(1)
```
## Time and Space complexity in One Dimensional Array
|Operation|Time Complexity| Space Complexity|
|---|---|---|
|Creating an empty array|O(1)|O(n)|
|Inserting an value in an array|O(1)/O(n)|O(1)|
|Traversing a given array|O(n)|O(1)|
|Accessing a given cell|O(1)|O(1)|
|Searching a given value|O(n)|O(1)|
|Deleting a given value|O(1)/O(n)|O(1)|

## Time and Space complexity in Two Dimensional Array
|Operation|Time Complexity| Space Complexity|
|---|---|---|
|Creating an empty array|O(1)|O(mn)|
|Inserting a column/row in an array|O(mn)/O(1)|O(1)|
|Traversing a given array|O(mn)|O(1)|
|Accessing a given cell|O(1)|O(1)|
|Searching a given value|O(mn)|O(1)|
|Deleting a given value|O(1)/O(mn)|O(1)|

## When to use/avoid Arrays
**When to use**
```
- To store multiple variables of same data type
- Random access
```
\
&nbsp;
**When to avoid**
```
- Same data type elements
- Reseve memory
```