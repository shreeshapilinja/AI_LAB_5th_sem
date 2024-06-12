# 3) write a python program to implement simple Chatbot with minimum 10 conservation


print("Simple question and answering program")
print("======================================================")
print("hi")
print("how are you")
print("what is your name")
print("are you studing")
print("what did you do yesterday")
print("what is your hobby")
print("your fav color")
print("your fav singer")
print("any future plans")
print("are you hungry now")
print("quit")
print("======================================================")
while True:
    question = input("enter any one question from the list: ")
    if question in ["hi"]:
        print("hello")
    elif question in ["how are you"]:
        print("fine")
    elif question in ["what is your name"]:
        print("shreesha")
    elif question in ["are you studing"]:
        print("no")
    elif question in ["what did you do yesterday"]:
        print("gone to hospital")
    elif question in ["what is your hobby"]:
        print("drawing")
    elif question in ["your fav color"]:
        print("green")
    elif question in ["your fav singer"]:
        print("shreya")
    elif question in ["any future plans"]:
        print("become teacher")
    elif question in ["are you hungry now"]:
        print("no")
    elif question in ["quit"]:
        print("thank you")
        break
    else:
        print("I don't understand what are you saying")



'''
Simple question and answering program
======================================================
hi
how are you
what is your name
are you studing
what did you do yesterday
what is your hobby
your fav color
your fav singer
any future plans
are you hungry now
quit
======================================================
enter any one question from the list: hi
hello
enter any one question from the list: how are you
fine
enter any one question from the list: what did you do yesterday
gone to hospital
enter any one question from the list: fav color
I don't understand what are you saying
enter any one question from the list: what is your fav color
I don't understand what are you saying
enter any one question from the list: your fav color
green
enter any one question from the list: are you hungry now
no
enter any one question from the list: quit
thank you

'''