import random

print("🎮 Rock Paper Scissors Game")

choice = ["rock","paper","scissors"]

player = input("Choose rock, paper, or scissors").lower()

computer = random.choice(choice)

print("Computer chose:", computer)

if player == computer:

    print("It's a tie! 🤝")

elif player == "rock" and computer == "scissors":
    print("You win! 🎉")

elif player == "paper" and computer == "rock":
    print("You win!🎉")

elif player == "scissors" and computer == "paper":    
    print("You win! 🎉")

elif player in choice:
    print("Computer wins! 🤖")

else:    
    print("Invalid choice! Please choose rock, paper, or scissors")