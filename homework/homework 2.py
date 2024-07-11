import random

val = int(input("Please enter a random number between 1-100:\n"))

numb = random.randint(1, 101)

if abs(numb - 21) > abs(val - 21):
    print("player wins")
else:
    print("dealer wins")



