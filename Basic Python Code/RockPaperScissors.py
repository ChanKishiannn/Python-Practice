import random

gameMenu = 0

while gameMenu != 2:
    print("Welcome to Rock, Paper, Scissor Game!")
    gameMenu = int(input("Press [1] to play! and press [2] to End the Game"))

    if gameMenu > 0 and gameMenu < 3:
        match gameMenu:
            case 1:
                userChoose = input("Please Choose between this: [Rock], [Paper], or [Scissor]")

                if userChoose == "Rock" or userChoose == "Paper" or userChoose == "Scissor":
                    computerChoice = ["Rock","Paper", "Scissor"]
                    computerChoose = random.choice(computerChoice)
                
                    if userChoose == computerChoose:
                        print(f"\n\nYou Choose {userChoose} and the computer choose {computerChoose}. \nSo it is a Draw! Try Again\n")
                    
                    elif userChoose == "Rock" and computerChoose == "Paper":
                        print(f"\nYou Choose {userChoose} and the computer choose {computerChoose}.\nSo you lose! Better luck next time\n")
                    elif userChoose == "Paper" and computerChoose == "Scissor":
                        print(f"\nYou Choose {userChoose} and the computer choose {computerChoose}.\nSo you lose! Better luck next time\n")
                    elif userChoose == "Scissor" and computerChoose == "Rock":
                        print(f"\nYou Choose {userChoose} and the computer choose {computerChoose}.\nSo you lose! Better luck next time\n")
                    else:
                        print("You Win! Congratulations!\n\nExiting Game")
                        gameMenu = 2

                else:
                    print("\n\nInvalid input!\nPlease choose between this: [Rock], [Paper], or [Scissor]\n\n")
            case 2:
                print("Exiting the game!")
    else:
        print("Invalid Input! Please Try Again\n")
    
