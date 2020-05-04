import random

number = random.randint(1, 10)
steps = 1
hints = 1
name = input("What is your name? ")
print("Hi "+name+".")
ask = input("Would you like to play a game? [y/n] ")
if ask == 'n':
    print("Get out from here")
if ask == 'y':
    print('''Game's Rules:
    1. 3 chances
    2. only 1 hints can be chosen''')
    print("I am guessing a number from 1 to 10")
    guess = int(input("What do you think the number is? "))
    while guess != number:
        guess1 = input("Try again! [press 'h' for hints]")
        if guess1 != 'h':
            steps += 1
            if steps == 3:
                if int(guess1) == number:
                    print("\nHurray! You win. ")
                    print("The guessed number is", number, ".")
                    print("And you did it in", steps, "tries")
                else:
                    print("\nSorry! You loss your all 3 chances.")
                    print("The number was", number)
                    break
        if guess1 == 'h':
            if hints < 2:
                if guess < number:
                    print("Guess Higher!")
                if guess > number:
                    print("Guess Lower!")
                hints += 1
        else:
            guess = int(guess1)
    if guess == number:
        print("\nHurray! You win. ")
        print("The guessed number is", number, ".")
        print("And you did it in", steps, "tries")
