#Importing random to make the program choose randomly values later
import random

#Assignning the gameMenu a value zero to let the program know that the user still now choose any Menu
gameMenu = 0

#Making a while loop that stop if the user input 2 in the gameMenu
while gameMenu != 2:
    #Asking the user what process they want to run in the program
    print("Welcome to Rock, Paper, Scissor Game!")
    gameMenu = int(input("Press [1] to play! and press [2] to End the Game"))

    #Making an if-statement that check if the user input are either 1 or 2
    if gameMenu > 0 and gameMenu < 3:

        #Making a match-case statement to make the program run depends on the user input in the gameMenu
        match gameMenu:
            #The case 1: will run if the user choose 1 in the gameMenu
            case 1:
                #Asking the user what he want to choose between Rock, Paper, and Scissor
                userChoose = input("Please Choose between this: [Rock], [Paper], or [Scissor]")

                #Checking is the user input is match accourding to the userChoose. If it match it will run the program below.
                if userChoose == "Rock" or userChoose == "Paper" or userChoose == "Scissor":
                    #Making the computer choose between Rock, Paper, Scissor. By using the random that import ealier - the computer will choose randomly
                    computerChoice = ["Rock","Paper", "Scissor"]
                    computerChoose = random.choice(computerChoice)

                    #Making an if-statement to check if the use choice and the computer choice are the same.
                    if userChoose == computerChoose:
                        print(f"\n\nYou Choose {userChoose} and the computer choose {computerChoose}. \nSo it is a Draw! Try Again\n")

                    #Making an elif statement to check if the user choice and the computer choice.
                    #This time it check if the computer choice is supperior to the user choice.
                    elif userChoose == "Rock" and computerChoose == "Paper":
                        print(f"\nYou Choose {userChoose} and the computer choose {computerChoose}.\nSo you lose! Better luck next time\n")
                    elif userChoose == "Paper" and computerChoose == "Scissor":
                        print(f"\nYou Choose {userChoose} and the computer choose {computerChoose}.\nSo you lose! Better luck next time\n")
                    elif userChoose == "Scissor" and computerChoose == "Rock":
                        print(f"\nYou Choose {userChoose} and the computer choose {computerChoose}.\nSo you lose! Better luck next time\n")

                    #The else statement will be executed if niether of the following above meets the requirements to run the program
                    #This is means that the user win in the Rock, Paper, Scissor game againts the computer.
                    else:
                        print("You Win! Congratulations!\n\nExiting Game")
                        gameMenu = 2

                #The else sattement will be printed an error message if the user misspells or input different input againts the gameMenu
                else:
                    print("\n\nInvalid input!\nPlease choose between this: [Rock], [Paper], or [Scissor]\n\n")

            #The case 2: will run if the user choose 2 in the gameMenu. This make the program STOP
            case 2:
                print("Exiting the game!")
                
    #An error massage if the user input niether 1 or 2.
    else:
        print("Invalid Input! Please Try Again\n")
    
