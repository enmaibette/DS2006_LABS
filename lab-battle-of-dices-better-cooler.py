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

def roll_dice(player1_wins, player2_wins, dice_1, dice_2):
  nobody_won = True
  round_number = 0
  print("The value which will be printed is the sum of two dice rolls per player.")
  while(nobody_won):
        input("\nPress ENTER to roll the dice...")
        player1_roll_sum = random.randint(1, dice_1) + random.randint(1, dice_2)
        player2_roll_sum = random.randint(1, dice_1) + random.randint(1, dice_2)

        print("Player 1 rolled: ", player1_roll_sum)
        print("Player 2 rolled: ", player2_roll_sum)
        
        input("\nPress ENTER to continue...")

        # So far so good right? But how to check who got the highest roll?

        if player1_roll_sum > player2_roll_sum:
            player1_wins += 1
            print("Player 1 wins this round!")
            print("Because ", player1_roll_sum," is greater than ", player2_roll_sum)
        elif player1_roll_sum == player2_roll_sum:
            print("Amaaazzinng! This round has a tie!")
        else:
            player2_wins += 1
            print("Player 2 wins this round!")
            print("Because ", player2_roll_sum," is greater than ", player1_roll_sum)

        # We can print the game score:
        print("The game score is Player1: ", player1_wins, " vs. Player2: ", player2_wins)

        # Now we need to check if either player won.
        if player1_wins == 3:
            print("Player 1 is the newest Battle of Dices Champion! ")
            nobody_won = False
        elif player2_wins == 3:
            print("Player 2 is the newest Battle of Dices Champion! ")
            nobody_won = False
        else:
            print("This heated Battle of Dices is still going on! Who will win in the end? ")
        round_number += 1
        print("Round number: ", round_number)

def choose_dice():
    dices_sides = 0
    while(dices_sides == 0):
        dices_sides_input = input("Enter the number of sides for the dice. Choose between D4, D8, D12, D20 or D100. Enter the number only (4, 8, 12, 20 or 100). : \n")
        if(dices_sides_input not in ['4', '8', '12', '20', '100']):
            print("Invalid input. Retry.")
        else: 
            dices_sides = int(dices_sides_input)
    return dices_sides


print("🎲 Welcome to Battle of Dices! 🎲")
2
# Variables to keep track of the score:
player1_wins = 0
player2_wins = 0

print("You need to choose two dices for this game.")
dice_1 = choose_dice()
dice_2 = choose_dice()

roll_dice(player1_wins, player2_wins, dice_1, dice_2)