import random

number = random.randint(1, 1000)
attempts = 0
low = 1
high = 1000

while True:
    print("Guess the number (between 1 and 1000):")
    inputnumber = (low + high) // 2 # only integer division
    print("My guess is", inputnumber)
    attempts += 1

    if inputnumber == number:
        print("Yes, your guess is correct!")
        break
    if inputnumber > number:
        print("Incorrect! Please try to guess a smaller number.")
        high = inputnumber - 1
    else:
        print("Incorrect! Please try to guess a larger number.")
        low = inputnumber + 1

print("You tried", attempts, "times to find the correct number.")

