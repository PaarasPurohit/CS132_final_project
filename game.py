import random

num = random.randint(1, 100)

guess = int(input("Guess the number >>"))

while guess != num:
    if guess > num:
        print("Too high")
        guess = int(input("Guess the number >>"))
    if guess < num:
        print("Too low")
        guess = int(input("Guess the number >>"))

