# Import the random variable
import random

# Make a varible and assign it to generete from 1 to 10
number_to_guess = random.randint(1, 10)
guess = None
tries = 0;

#Printing a statement that the computer is thinking a random number
print("Im thinking of a number between 1 to 10")

#Creating a while loop where it loops until the user guess is correct
while guess != number_to_guess:
    try:
        guess = int(input("Guess the Number: "))
        tries += 1
        
        if guess < 0 or guess > 10:
            print("Invalid Guest out of bounce! Please Try Again!")
            print(f"Your Tries {tries}")
        elif guess < number_to_guess:
            print("Your guess number is Low!: ")
            print(f"Your Tries {tries}")
        elif guess > number_to_guess:
            print("Your guess number is High!: ")
            print(f"Your Tries {tries}")
        else:
            print(f"Congratulation you Guess the number: {number_to_guess}")
            print(f"Your Tries {tries}")

#Printing an error message if the user input is out of bounces
    except ValueError:
        print("Invalid Number")
