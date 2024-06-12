from collections import defaultdict
jug1 = int(input("max capacity of jug1: "))
jug2 = int(input("max capacity of jug2: "))
goal = int(input("Enter capacity to be measured: "))
visited = defaultdict(lambda:False)

def waterjug(a1,a2):
  if(a1==goal and a2==0) or (a2==goal and a1==0):
    print(a1,a2)
    return True
  if visited[(a1,a2)] == False:
    print(a1,a2)
    visited[(a1,a2)] = True
    return (waterjug(0,a2) or waterjug(a1,0) or waterjug(jug1,a2) or waterjug(a1,jug2) or 
            waterjug(a1+min(a2,jug1-a1) , a2-min(a2,jug1-a1)) or waterjug(a1-min(a1,jug2-a2),a2+min(a1,jug2-a2)))
  else:
    return False

print('Steps: ')
waterjug(0,0)

"""

This code uses a depth-first search (DFS) algorithm to solve the water jug problem.

In the water jug problem, the goal is to measure a specific volume of water using two jugs with given capacities. The jugs can be filled and emptied, and water can be transferred from one jug to the other. The solution is a sequence of steps that leads to the goal state, which is defined as having one of the jugs filled with the desired volume of water and the other jug empty.

The DFS algorithm works by starting from the initial state (in this case, both jugs empty) and exploring as far as possible along each branch before backtracking. It continues this process until it either finds a solution or exhausts all possibilities. In each step, the algorithm tries the following actions:

Fill jug1
Fill jug2
Empty jug1
Empty jug2
Transfer water from jug2 to jug1
Transfer water from jug1 to jug2

The algorithm also keeps track of the states it has visited using a visited dictionary to avoid exploring the same state more than once.

If the algorithm reaches a state where one of the jugs has the desired volume and the other is empty, it returns True, indicating that a solution has been found. If it exhausts all possibilities without finding a solution, it returns False.

another -> explaination
This code is using a recursive depth-first search algorithm to solve the water jug problem.

The water jug problem is a classic problem in artificial intelligence and computer science in
 which two jugs with known capacities must be used to measure out a specific amount of water. 
 In this code, the function waterjug() is a recursive function that tries different combinations 
 of filling, pouring, and emptying the jugs in an attempt to find a sequence of actions that will result in one 
 of the jugs containing the desired amount of water.

The function waterjug() takes two arguments, a1 and a2, which represent the current amounts of water 
in the two jugs. The function returns True if it is able to find a sequence of actions that results in one of the 
jugs containing the desired amount of water, and False if it is not able to find a solution. The function makes use of 
a dictionary, visited, to keep track of the states of the jugs that have already been explored, in order to avoid repeating the same 
state and getting stuck in an infinite loop.

The function waterjug() considers six different actions: filling jug 1, filling jug 2, emptying jug 1, emptying jug 2, 
pouring the contents of jug 1 into jug 2, and pouring the contents of jug 2 into jug 1. It tries each of these actions in
 turn and calls itself recursively with the updated state of the jugs. If any of these recursive calls returns True, 
 the function waterjug() returns True, indicating that a solution has been found. If none of the recursive calls returns True,
  the function waterjug() returns False, indicating that no solution was found.

"""


