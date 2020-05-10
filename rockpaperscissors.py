from random import choice
options_comp = ("ROCK","PAPER","SCISSORS")
options_player = ("ROCK","PAPER","SCISSORS","QUIT")
while True: ##repeats the game until user wishes to quit
    player = input("\nPlease insert your choice: ROCK, PAPER or SCISSORS. Input QUIT to terminate.\n\n").upper() ##gets user choice
    while player not in options_player: ##checks if user choice is valid
        player = input("\nPlease insert a valid choice: ROCK, PAPER or SCISSORS. Input QUIT to terminate.\n\n").upper()
    if player =="QUIT": ##terminates the game when user inputs QUIT
        break

    computer = choice(options_comp) ##generates random computer choice
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
