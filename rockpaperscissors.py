from random import choice
options_comp = ("ROCK","PAPER","SCISSORS")
options_player = ("ROCK","PAPER","SCISSORS","QUIT")
while True:
    player = input("\nPlease insert your choice: ROCK, PAPER or SCISSORS. Input QUIT to terminate.\n\n").upper()
    while player not in options_player:
        player = input("\nPlease insert a valid choice: ROCK, PAPER or SCISSORS. Input QUIT to terminate.\n\n").upper()
    if player =="QUIT":
        break

    computer = choice(options_comp)
    print (f"\nComputer plays {computer}\n")

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

print("\nThanks for playing!\n")
