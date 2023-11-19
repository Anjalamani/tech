import random
guess_time=0
print("Hello! what is your name:")
name=input()
number=random.randint(1,50)
guess=int(input("I am thinking of a number between 1 and 50,can you guess what it is?"))
while guess_time<4:
    guess_time=guess_time+1
    if guess<number:
        print("you need to guess higher..Try again?")
        guess=int(input("I am thinking of a number between 1 and 50,"))
    else: 
         print("you need to guess lower..Try again?")
         guess=int(input("I am thinking of a number between 1 and 50,"))
    if guess==number:
        break
if guess==number:
    guess_time=str(guess_time)
    print("good",name,"you guess the number in",guess_time,"times")
if guess!=number:
    number=str(number)
print("nope,number i was thinking",number)