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
import os, sys
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)
import Labs.Lab2.dice as dice

def roll_dice(player1_wins, player2_wins, dices_sides):
    nobody_won = True
    round_number = 0
    player1_list = []
    player2_list = []
    while(nobody_won):
        input("\nPress ENTER to roll the dice...")

        if dices_sides in dice.dice_functions:
            print(f"Rolling a D{dices_sides}...")
            player1_roll = dice.dice_functions[dices_sides]()
            player2_roll = dice.dice_functions[dices_sides]()

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
                nobody_won = False
            elif player2_wins == 3:
                print("Player 2 is the newest Battle of Dices Champion! ")
                nobody_won = False
            else:
                print("This heated Battle of Dices is still going on! Who will win in the end? ")
            
            player1_list.append(player1_roll)
            player2_list.append(player2_roll)
            round_number += 1
            print("Round number: ", round_number)
        
    return player1_list, player2_list, round_number

def results_of_all_rounds(player1_list, player2_list, round_number, dices_sides):
    print_lines = "------------"
    used_dice = f'Here are the results of the Battle of Dices using D{dices_sides}'
    player1_result = '| Player 1 | '
    player2_result = '| Player 2 | '
    rounds = '|  Round   | '
    for i in range(1, round_number+1):
        print_lines += "----"
        player1_result += f'{player1_list[i-1]} | '
        player2_result += f'{player2_list[i-1]} | '
        rounds += f'{i} | '

    results_of_all_rounds = used_dice + "\n" + print_lines + "\n" + rounds + "\n" + print_lines + "\n" + player1_result + "\n" + print_lines + "\n" + player2_result + "\n" + print_lines
    print('\n' + results_of_all_rounds)
    return results_of_all_rounds

def choose_dice():
    dices_sides = 0
    while(dices_sides == 0):
        dices_sides_input = input("Enter the number of sides for the dice. Choose between D4, D8, D12, D20 or D100. Enter the number only (4, 8, 12, 20 or 100). :")
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

dices_sides = choose_dice()

player1_list, player2_list, round_number = roll_dice(player1_wins, player2_wins, dices_sides)
results_of_all_rounds = results_of_all_rounds(player1_list, player2_list, round_number, dices_sides)

filename = input("\nIn wich file do you want to save the results? On Enter it saves it automatically in result.txt: ")
if filename == '':
    filename = 'result.txt'
with open(filename, 'w') as f:
    f.write(results_of_all_rounds)
    f.write('\n')
    print(f'Results saved in {filename}')
