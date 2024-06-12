'''
5 a) write a python program to implement a function that counts number of times 
string(s1) occurs in string (s2)
'''
s1 = input("Enter the substring: ").lower()
s2 = input("Enter the string: ").lower()
count = s2.count(s1)
print("The substring",s1,"string occured in string",s2,count,"times")


"""
Enter the substring: vc
Enter the string: vcetputtur vc
The substring vc string occured in string vcetputtur vc 2 times
"""