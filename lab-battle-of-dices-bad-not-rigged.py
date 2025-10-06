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

def throwDice(dices_sides, round_number):
    input("\nPress ENTER to roll the dice...")
    round_number += 1
    player1_roll = random.randint(1, dices_sides)
    player2_roll = random.randint(1, dices_sides)

    print("Player 1 rolled: ", player1_roll)
    print("Player 2 rolled: ", player2_roll)
    return player1_roll, player2_roll, round_number

def which_player_won(player1_roll, player2_roll, player1_wins, player2_wins):
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

    if player1_wins == 3:
        print("Player 1 is the newest Battle of Dices Champion! ")
    elif player2_wins == 3:
        print("Player 2 is the newest Battle of Dices Champion! ")
    else:
        print("This heated Battle of Dices is still going on! Who will win in the end? ")

    return player1_wins, player2_wins

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
round_number = 0

dices_sides = choose_dice()

player1_round1_roll, player2_round1_roll, round_number = throwDice(dices_sides, round_number)
player1_wins, player2_wins = which_player_won(player1_round1_roll, player2_round1_roll, player1_wins, player2_wins)

player1_round2_roll, player2_round2_roll, round_number = throwDice(dices_sides, round_number)
player1_wins, player2_wins = which_player_won(player1_round2_roll, player2_round2_roll, player1_wins, player2_wins)

player1_round3_roll, player2_round3_roll, round_number = throwDice(dices_sides, round_number)
player1_wins, player2_wins = which_player_won(player1_round3_roll, player2_round3_roll, player1_wins, player2_wins)

if player1_wins < 3 and player2_wins < 3:
    player1_round4_roll, player2_round4_roll, round_number = throwDice(dices_sides, round_number)
    player1_wins, player2_wins = which_player_won(player1_round4_roll, player2_round4_roll, player1_wins, player2_wins)

if player1_wins < 3 and player2_wins < 3:
    player1_round5_roll, player2_round5_roll, round_number = throwDice(dices_sides, round_number)
    player1_wins, player2_wins = which_player_won(player1_round5_roll, player2_round5_roll, player1_wins, player2_wins)

if player1_wins < 3 and player2_wins < 3:
    player1_round6_roll, player2_round6_roll, round_number = throwDice(dices_sides, round_number)
    player1_wins, player2_wins = which_player_won(player1_round6_roll, player2_round6_roll, player1_wins, player2_wins)

if player1_wins < 3 and player2_wins < 3:
    player1_round7_roll, player2_round7_roll, round_number = throwDice(dices_sides, round_number)
    player1_wins, player2_wins = which_player_won(player1_round7_roll, player2_round7_roll, player1_wins, player2_wins)

if player1_wins < 3 and player2_wins < 3:
    player1_round8_roll, player2_round8_roll, round_number = throwDice(dices_sides, round_number)
    player1_wins, player2_wins = which_player_won(player1_round8_roll, player2_round8_roll, player1_wins, player2_wins)

if player1_wins < 3 and player2_wins < 3:
    player1_round9_roll, player2_round9_roll, round_number = throwDice(dices_sides, round_number)
    player1_wins, player2_wins = which_player_won(player1_round9_roll, player2_round9_roll, player1_wins, player2_wins)

if player1_wins < 3 and player2_wins < 3:
    player1_round10_roll, player2_round10_roll, round_number = throwDice(dices_sides, round_number)
    player1_wins, player2_wins = which_player_won(player1_round10_roll, player2_round10_roll, player1_wins, player2_wins)

if player1_wins < 3 and player2_wins < 3:
    player1_round11_roll, player2_round11_roll, round_number = throwDice(dices_sides, round_number)
    player1_wins, player2_wins = which_player_won(player1_round11_roll, player2_round11_roll, player1_wins, player2_wins)

if player1_wins < 3 and player2_wins < 3:
    player1_round12_roll, player2_round12_roll, round_number = throwDice(dices_sides, round_number)
    player1_wins, player2_wins = which_player_won(player1_round12_roll, player2_round12_roll, player1_wins, player2_wins)

if player1_wins < 3 and player2_wins < 3:
    player1_round13_roll, player2_round13_roll, round_number = throwDice(dices_sides, round_number)
    player1_wins, player2_wins = which_player_won(player1_round13_roll, player2_round13_roll, player1_wins, player2_wins)

if player1_wins < 3 and player2_wins < 3:
    player1_round14_roll, player2_round14_roll, round_number = throwDice(dices_sides, round_number)
    player1_wins, player2_wins = which_player_won(player1_round14_roll, player2_round14_roll, player1_wins, player2_wins)

if player1_wins < 3 and player2_wins < 3:
    player1_round15_roll, player2_round15_roll, round_number = throwDice(dices_sides, round_number)
    player1_wins, player2_wins = which_player_won(player1_round15_roll, player2_round15_roll, player1_wins, player2_wins)

print_lines = "------------"
print_player1 = '| Player 1 | '
print_player2 = '| Player 2 | '
print_round = '|  Round   | '
for i in range(1, round_number+1):
    print_lines += "----"
    print_player1 += f'{locals().get(f"player1_round{i}_roll")} | '
    print_player2 += f'{locals().get(f"player2_round{i}_roll")} | '
    print_round += f'{i} | '

print(print_lines)
print(print_round)
print(print_lines)
print(print_player1)
print(print_lines)
print(print_player2)
print(print_lines)