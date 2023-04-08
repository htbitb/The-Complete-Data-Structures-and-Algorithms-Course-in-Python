# Created by htb on 04/04/2023.
# Copyright 2020 AppMillers. All rights reserved.

# List operation / function

a = [12, 22, 31]
b = [44, 5, 6]
c = a + b
print('List a plus list b equal to: ', c)
print('Minimum value in list C', min(c))
print('Maximum value in list c', max(c))
print('Sum of list c', sum(c))

##############################################

total = 0
count = 0
while(True):
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    total = total + value
    count = count + 1
    average = total / count
    
print('Average:', average)

###### Another way to write the easy function

mylist = list()
while(True):
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    mylist.append(value)
    average = sum(mylist) / len(mylist)
    
print('Average:', average)

# Calculate average Temperature

mylist = list()

num_day = int(input("How many day's temperatur?"))

for i in range (1, num_day+1):
    nextday = int(input("Day" + str(i) + "'s high temp:"))
    mylist.append(nextday)
    
average = sum(mylist) / len(mylist)
count = 0

for i in range (0, len(mylist)):
    if mylist[i] > average:
        count = count + 1

print('Average = ', average)
print(str(count) + " Day(s) above average")