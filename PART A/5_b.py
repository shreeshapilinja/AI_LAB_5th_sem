"""
5 b) write a program to illustrate dictionary operations([],in,traversal) and methods :
keys() ,values() , items()
"""
print("Dictionary Operations".center(55,'-'))

my_dict = {'name':'shreesha','age':20,'gender':'male'}

print("\naccessing values with []")
print(my_dict['name'])

print("\naccessing values with get() method")
print(my_dict.get('age'))

print("\naccessing non existing values with get() method")
print(my_dict.get('address','do not exist'))

print("\naccessing non existing values with [] error handeled")
try:
    print(my_dict['address'])      # error
except:
    print("error:  KeyError")
    
print("-".center(55,'-'))
print()
print("without keys and values".center(55,'-'))

statecapital = {'gujarat':'gandhinagar','maharastra':'mumbai','rajastan':'jaipur','bihar':'patna'}

print("\nThe states and capital : ",statecapital)

print("\naccessing keys without using keys()")
for state in statecapital:
    print(state)
    
print("\naccessing keys without using values()")
for capital in statecapital:
    print(statecapital[capital])

print("keys and values".center(55,'-'))

print("\naccessing keys with using keys()")
keys = statecapital.keys()
print("keys: ",keys)
    
print("\naccessing keys with using values()")
values = statecapital.values()
print("values: ",values)
    
print("\naccessing keys and values with using items()")
for i in statecapital.items():
	print(i)

    
print()
print("-".center(55,'-'))
print("in operators".center(55,'-'))
print()

spam = {'name':'shreesha','age':7,'color':'white'}
print('spam =',spam)
res1 = 'name' in spam.keys()
print("'name' in spam.keys(): ",end='')
print(res1)

res2 = 'nature' in spam.keys()
print("'nature' in spam.keys(): ",res2)

print("-".center(55,'-'))
print()
print("not in operators".center(55,'-'))
print()

res3 = 'name' not in spam.keys()
print("'name' not in spam.keys(): ",res3)

res4 = 'shreesha' not in spam.values()
print("'shreesha' not in spam.values(): ",res4)

res5 = 8 not in spam.values()
print("8 not in spam.values(): ",res5)
print()
