## 1 (c) write a python program to find factorial of given number


n = int(input("Enter the nos whose factorial needs to be found: "))
fact = 1
if n<0:
    print("cannot find the factorial of negetive number")
else:
    if n==0:
        print("factorial of 0 is 1")
    else:
        for i in range(1,n+1):
            fact = fact*i
        print("factorial of number ",n," (",n,"!) is ",fact)


'''
Enter the nos whose factorial needs to be found: 5
factorial of number  5  ( 5 !) is  120

'''