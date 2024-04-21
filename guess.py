import random
number = random.randint(0 , 100)

guess = -1
while guess != number:
    guess = eval(input("enter the number: "))
    if guess == number:
        print("Your guess is correct")
    elif guess > number:
        print("Your guess is greater than the number")
    else:
        print("Your guess is smaller than the number")