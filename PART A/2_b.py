"""
2 b) Write a python program to implement List methods
      i) append
      ii) add - insert
      iii) extend
      iv) delete
"""

# i append to list at last

print("========= append to list ===========")
L1 = ['hello', 'how', 'are']
print("The list before appending is: ",L1)
L1.append('you')
print("The list after appending 'you' is: ",L1)
print("=============================================")
print()

# ii insert to list
L1 = ['hello', 'how', 'are','you']
print("========= insert to list ===========")
print("The list before insertion is: ",L1)
L1.insert(1,'shreesha')
print("The list after adding 'shreesha' to 2nd position is: \n",L1)
print("=============================================")
print()

# iii extend the list 1
print("========= extend list ===========")
L1 = ['hello', 'how', 'are']
L2 = ['i', 'fine', 1, 2]
print("The is 1st list is: ",L1)
print("The is 2nd list is: ",L2)
L1.extend(L2)
print("after the extention of list 1 it becomes : \n",L1)
print("=============================================")
print()


# iv delete - remove the particular element
print("========= delete using remove ===========")
L1 = ['hello', 'how', 'are','you']
print("The is list before removing is: ",L1)
L1.remove('hello')
print("The is list after removing 'hello' is: ",L1)
print("=============================================")
print()


# v delete last , 1st element using pop
print("========= delete using pop ===========")
L1 = ['hello', 'how','are','you']
print("The is list before poping is: ",L1)
L1.pop()
print("The is list after poping from last is: ",L1)
print()
print("The is list before poping is: ",L1)
L1.pop(0)
print("The is list after poping from 1st is: ",L1)
print("=============================================")
print()

# delete using keyword del
print("========= delete using del ===========")
L1 = ['hello', 'how', 'are','you']
print("The is list before deleting is: ",L1)
del L1[1]
print("The is list after deleting 2nd element is: ",L1)
print("=============================================")
print()

'''
========= append to list ===========
The list before appending is:  ['hello', 'how', 'are']
The list after appending 'you' is:  ['hello', 'how', 'are', 'you']
=============================================

========= insert to list ===========
The list before insertion is:  ['hello', 'how', 'are', 'you']
The list after adding 'shreesha' to 2nd position is: 
 ['hello', 'shreesha', 'how', 'are', 'you']
=============================================

========= extend list ===========
The is 1st list is:  ['hello', 'how', 'are']
The is 2nd list is:  ['i', 'fine', 1, 2]
after the extention of list 1 it becomes : 
 ['hello', 'how', 'are', 'i', 'fine', 1, 2]
=============================================

========= delete using remove ===========
The is list before removing is:  ['hello', 'how', 'are', 'you']
The is list after removing 'hello' is:  ['how', 'are', 'you']
=============================================

========= delete using pop ===========
The is list before poping is:  ['hello', 'how', 'are', 'you']
The is list after poping from last is:  ['hello', 'how', 'are']

The is list before poping is:  ['hello', 'how', 'are']
The is list after poping from 1st is:  ['how', 'are']
=============================================

========= delete using del ===========
The is list before deleting is:  ['hello', 'how', 'are', 'you']
The is list after deleting 2nd element is:  ['hello', 'are', 'you']
=============================================

'''
