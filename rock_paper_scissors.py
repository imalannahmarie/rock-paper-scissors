"""
rock_paper_scissors.py

Play rock, paper, scissors with a computer!
"""
# To randomize computer's choice
import random

# To exit if user enters something other than rock, paper or scissors
import sys

print("Let's play Rock, Paper, Scissors!")


def playGame():
    # Convert userChoice to lowercap to simplify comparisons
    userChoice = input("It's your turn! Type: rock, paper or scissors: ").lower()

    if userChoice == "rock":
        print("You chose rock")
    elif userChoice == "paper":
        print("You chose paper")
    elif userChoice == "scissors":
        print("You chose scissors")
    else:
        # Ends game
        sys.exit("I'm sorry, please choose rock, paper or scissors.")

    # Computer "picks" from outcomes list
    outcomes = ["rock", "paper", "scissors"]
    compChoice = random.choice(outcomes)
    print("Computer chooses", compChoice)

    # Asks user to play again
    def playAgain():
        askToPlay = input("Want to play again? Y/N\n").lower()
        if askToPlay == "y":
            playGame()
        elif askToPlay == "n":
            print("Bye!")
        else:
            print("Please type Y or N to play again.")
            playAgain()

    # Game Outcomes
    if userChoice == compChoice:
        print("You both chose the same thing. Play again!")
        playGame()
    # User Wins
    elif userChoice == "rock" and compChoice == "scissors":
        print("Congrats, you win!")
        playAgain()
    elif userChoice == "paper" and compChoice == "rock":
        print("Congrats, you win!")
        playAgain()
    elif userChoice == "scissors" and compChoice == "paper":
        print("Congrats, you win!")
        playAgain()
    # Computer Wins
    elif userChoice == "rock" and compChoice == "paper":
        print("Sorry, computer wins.")
        playAgain()
    elif userChoice == "paper" and compChoice == "scissors":
        print("Sorry, computer wins.")
        playAgain()
    elif userChoice == "scissors" and compChoice == "rock":
        print("Sorry, computer wins.")
        playAgain()


playGame()
