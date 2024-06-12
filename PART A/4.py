'''
4 ) write a python program to illustrate different set operation
'''
a = {2,4,6,8}
b = {1,2,3,4,5}
print("Set A = ",a,"Set B = ",b)
print("union of A & B (A U B)= ",a|b)
print("Intersection of A & B (A ^ B) = ",a&b)
print("Set difference  of B and A (A-B) = ",a-b)
print("Set symmetric difference(disjunctive union) of A and B (A-B)U(B-A) = ",(a-b)|(b-a))
print("Set symmetric difference(disjunctive union) of A and B (A ^ B) = ",a^b)
"""
Set A =  {8, 2, 4, 6} Set B =  {1, 2, 3, 4, 5}
union of A & B (A U B)=  {1, 2, 3, 4, 5, 6, 8}
Intersection of A & B (A ^ B) =  {2, 4}
Set difference  of B and A (A-B) =  {8, 6}
Set symmetric difference(disjunctive union) of A and B (A−B)∪(B−A) =  {1, 3, 5, 6, 8}
Set symmetric difference(disjunctive union) of A and B (A ^ B) = {1, 3, 5, 6, 8}
"""