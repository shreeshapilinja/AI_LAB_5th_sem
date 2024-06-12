## 1 (b) write a python program to check whether the given number is prime or not

num=int(input("Enter the number that is to checked prime or not: "))
if num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:                                        # see the indentation of else not below if below for
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")


'''
Enter the number that is to checked prime or not: 6
6 is not a prime number

'''