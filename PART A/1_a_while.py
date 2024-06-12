## 1 (a) write a program to print the multiplication table for the given number

# using while loop

a=int(input("Enter the number of which the user wants to print the multiplication table: "))
b=int(input("Enter the number till which user needs to be printed: "))
print("multiplication table of number is")
i=1
while i<=b:
    print(a,"X",i,"=",a*i)
    i=i+1



'''
Enter the number of which the user wants to print the multiplication table: 4
Enter the number till which user needs to be printed: 8
multiplication table of number is
4 X 1 = 4
4 X 2 = 8
4 X 3 = 12
4 X 4 = 16
4 X 5 = 20
4 X 6 = 24
4 X 7 = 28
4 X 8 = 32

'''