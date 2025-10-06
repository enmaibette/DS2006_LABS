# Battle of Dices is going to be an amazing 2 player game, 
# where two players face each other using only their sheer luck! 
# 
# The rules are:
# 
# Each player throws one D6.
# The player with the highest roll wins the round.  
# The first player to win 3 times is the winner.
#
# Our main task today is to implement the code necessary to bring this
# amazing game alive!
import random

def throwDice(player1_wins, player2_wins, dices_sides):
    input("\nPress ENTER to roll the dice...")
    player1_roll = random.randint(1, dices_sides)
    player2_roll = random.randint(1, dices_sides)

    print("Player 1 rolled: ", player1_roll)
    print("Player 2 rolled: ", player2_roll)


    input("\nPress ENTER to continue...")

    # So far so good right? But how to check who got the highest roll?

    if player1_roll > player2_roll:
        player1_wins += 1
        print("Player 1 wins this round!")
        print("Because ", player1_roll," is greater than ", player2_roll)
    elif player1_roll == player2_roll:
        print("Amaaazzinng! This round has a tie!")
    else:
        player2_wins += 1
        print("Player 2 wins this round!")
        print("Because ", player2_roll," is greater than ", player1_roll)

    # We can print the game score:
    print("The game score is Player1: ", player1_wins, " vs. Player2: ", player2_wins)

    # Now we need to check if either player won.
    if player1_wins == 3:
        print("Player 1 is the newest Battle of Dices Champion! ")
    elif player2_wins == 3:
        print("Player 2 is the newest Battle of Dices Champion! ")
    else:
        print("This heated Battle of Dices is still going on! Who will win in the end? ")

    return player1_wins, player2_wins, dices_sides


def choose_dice():
    dices_sides = input("Enter the number of sides for the dice. Choose between D4, D8, D12, D20 or D100. Enter the number only (4, 8, 12, 20 or 100). : \n")
    if(dices_sides not in ['4', '8', '12', '20', '100']):
        print("Invalid input. Retry.")
        choose_dice()
    dices_sides = int(dices_sides)
    return dices_sides


print("🎲 Welcome to Battle of Dices! 🎲")

# Variables to keep track of the score:
player1_wins = 0
player2_wins = 0

dices_sides = choose_dice()

player1_wins, player2_wins, dices_sides = throwDice(player1_wins, player2_wins, dices_sides)

player1_wins, player2_wins, dices_sides = throwDice(player1_wins, player2_wins, dices_sides)

player1_wins, player2_wins, dices_sides = throwDice(player1_wins, player2_wins, dices_sides)

if(player1_wins < 3 and player2_wins < 3):
    player1_wins, player2_wins, dices_sides = throwDice(player1_wins, player2_wins, dices_sides)
else:
    exit(0)

if(player1_wins < 3 and player2_wins < 3):
    player1_wins, player2_wins, dices_sides = throwDice(player1_wins, player2_wins, dices_sides)
else:
    exit(0)

if(player1_wins < 3 and player2_wins < 3):
    player1_wins, player2_wins, dices_sides = throwDice(player1_wins, player2_wins, dices_sides)
else:
    exit(0)

if(player1_wins < 3 and player2_wins < 3):
    player1_wins, player2_wins, dices_sides = throwDice(player1_wins, player2_wins, dices_sides)
else:
    exit(0)

if(player1_wins < 3 and player2_wins < 3):
    player1_wins, player2_wins, dices_sides = throwDice(player1_wins, player2_wins, dices_sides)
else:
    exit(0)

if(player1_wins < 3 and player2_wins < 3):
    player1_wins, player2_wins, dices_sides = throwDice(player1_wins, player2_wins, dices_sides)
else:
    exit(0)

if(player1_wins < 3 and player2_wins < 3):
    player1_wins, player2_wins, dices_sides = throwDice(player1_wins, player2_wins, dices_sides)
else:
    exit(0)

if(player1_wins < 3 and player2_wins < 3):
    player1_wins, player2_wins, dices_sides = throwDice(player1_wins, player2_wins, dices_sides)
else:
    exit(0)

if(player1_wins < 3 and player2_wins < 3):
    player1_wins, player2_wins, dices_sides = throwDice(player1_wins, player2_wins, dices_sides)
else:
    exit(0)

if(player1_wins < 3 and player2_wins < 3):
    player1_wins, player2_wins, dices_sides = throwDice(player1_wins, player2_wins, dices_sides)
else:
    exit(0)

if(player1_wins < 3 and player2_wins < 3):
    player1_wins, player2_wins, dices_sides = throwDice(player1_wins, player2_wins, dices_sides)
else:
    exit(0)

if(player1_wins < 3 and player2_wins < 3):
    player1_wins, player2_wins, dices_sides = throwDice(player1_wins, player2_wins, dices_sides)
else:
    exit(0)

if(player1_wins < 3 and player2_wins < 3):
    player1_wins, player2_wins, dices_sides = throwDice(player1_wins, player2_wins, dices_sides)
else:
    exit(0)