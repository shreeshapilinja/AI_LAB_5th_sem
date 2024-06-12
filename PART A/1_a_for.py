## 1 (a) write a program to print the multiplication table for the given number

# using for loop

n=int(input("Enter the number of which the user wants to print the multiplication table: "))
print("multiplication table of ",n," is")
for i in range(1,11):
    print(n,"X",i,"=",n*i)


'''
Enter the number of which the user wants to print the multiplication table: 7
multiplication table of  7  is
7 X 1 = 7
7 X 2 = 14
7 X 3 = 21
7 X 4 = 28
7 X 5 = 35
7 X 6 = 42
7 X 7 = 49
7 X 8 = 56
7 X 9 = 63
7 X 10 = 70
'''