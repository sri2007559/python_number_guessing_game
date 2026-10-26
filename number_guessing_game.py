import random

print("WELCOME TO NUMBER GUESSING GAME!")

secret_number = random.randint(1, 100)
attempts = 0

while True:
    guess = input("Guess a number between 1 and 100: ")

    if not guess.isdigit():
        print("Please enter a valid positive number.")
        continue

    guess = int(guess)

    if guess < 1 or guess > 100:
        print("Enter a number between 1 and 100.")
        continue

    attempts += 1

    if guess < secret_number:
        print("Too low! Try a bigger number.")
    elif guess > secret_number:
        print("Too high! Try a smaller number.")
    else:
        print("Congratulations! You guessed correctly!")
        print("Number of attempts:", attempts)
        break
