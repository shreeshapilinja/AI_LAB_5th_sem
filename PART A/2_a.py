"""
 2 (a) Write a python program to implement list operations
        i) nested list
        ii) length
        iii) concatination
        iv) membership
        v) iteration
        vi) indexing
        vii) slicing
        viii) replication
"""

print()


# i nested list
print("========== nested list ==============")
nested_list = [1,[2,3],'hi',['hello','world']]
print("The nested list is ",nested_list)
print("nested_list[0] : ",nested_list[0])
print("nested_list[-1][-1]: ",nested_list[-1][-1])
print("nested_list[1][1]: ",nested_list[1][1])
print("======================================")
print()


# ii lenth of the list
print("========== length of list ==============")
L1 = ['hello','how','are','you']
print("The list is ",L1)
print("The length of list ",len(L1))
print("======================================")
print()


# iii concatination
print("========== concatination list ==============")
L1 = ['hello','how','are','you']
L2 = ['i am','fine',1,2]
print("The list 1  is ",L1)
print("The list 2  is ",L2)
L3 = L1+L2
print("The concatination of list 1 and 2 is ",L3)
print("======================================")
print()



# iv membership 
print("========== membership list ==============")
L1 = ['hello','how','are','you']
print("The list is ",L1)
ans1 = 'apple' in L1
print("checking is 'apple' in the list ",ans1)
ans2 = 'hello' in L1
print("checking is 'hello' in the list ",ans2)
print("======================================")
print()



# v iteration
print("========== iteration list ==============")
L1 = ['hello','how','are','you']
print("The list is ",L1)
print("printing element of list")
for i in L1:
    print(i)
print("======================================")
print()



# vi indexing
print("========== indexing list ==============")
L1 = ['hello','how','are','you']
print("The list is ",L1)
print("printing individual element of list")
print(L1[0])
print(L1[1])
print(L1[2])
print(L1[3])
print("======================================")
print()



# vii slicing
print("========== slicing list ==============")
L1 = ['hello','how','are','you']
print("The list is ",L1)
print("The L1[0:3]: ",L1[0:3])
print("The L1[2:]: ",L1[2:])
print("The L1[2:3]: ",L1[2:3])
print("======================================")
print()



# viii replication
print("========== replication list ==============")
L2 = ['i am','fine',1,2]
print("The list is ",L2)
L4 = L2 * 3
print("The list after replicating 3 times is ",L4)
print("======================================")
print()


'''
========== nested list ==============
The nested list is  [1, [2, 3], 'hi', ['hello', 'world']]
nested_list[0] :  1
nested_list[-1][-1]:  world
nested_list[1][1]:  3
======================================

========== lenth of list ==============
The list is  ['hello', 'how', 'are', 'you']
The length of list  4
======================================

========== concatination list ==============
The list 1  is  ['hello', 'how', 'are', 'you']
The list 2  is  ['i am', 'fine', 1, 2]
The concatination of list 1 and 2 is  ['hello', 'how', 'are', 'you', 'i am', 'fine', 1, 2]
======================================

========== membership list ==============
The list is  ['hello', 'how', 'are', 'you']
checking is 'apple' in the list  False
checking is 'hello' in the list  True
======================================

========== iteration list ==============
The list is  ['hello', 'how', 'are', 'you']
printing element of list
hello
how
are
you
======================================

========== indexing list ==============
The list is  ['hello', 'how', 'are', 'you']
printing individual element of list
hello
how
are
you
======================================

========== slicing list ==============
The list is  ['hello', 'how', 'are', 'you']
The L1[0:3]:  ['hello', 'how', 'are']
The L1[2:]:  ['are', 'you']
The L1[2:3]:  ['are']
======================================

========== replication list ==============
The list is  ['i am', 'fine', 1, 2]
The list after replicating 3 times is  ['i am', 'fine', 1, 2, 'i am', 'fine', 1, 2, 'i am', 'fine', 1, 2]
======================================
'''

