from random import choice
options = ("ROCK","PAPER","SCISSORS")

player = input("Please insert your choice: ROCK, PAPER or SCISSORS:\n").upper()
computer = choice(options)
print (f"Computer plays {computer}")

if player == "ROCK":
    if computer == "SCISSORS":
        print("Player wins!")
    elif computer == "PAPER":
        print("Computer wins!")
    else:
        print("It's a tie!")
elif player == "PAPER":
    if computer == "ROCK":
        print("Player wins!")
    elif computer == "SCISSORS":
        print("Computer wins!")
    else:
        print("It's a tie!")
elif player == "SCISSORS":
    if computer == "PAPER":
        print("Player wins!")
    elif computer == "ROCK":
        print("Computer wins!")
    else:
        print("It's a tie!")
