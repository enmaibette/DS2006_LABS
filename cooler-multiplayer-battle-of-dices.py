import os, sys
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)
import Labs.Lab2.dice as dice

# Number of wins needed to win the game
winning_score = 3

# Array for storing the names of the players:
player_names = []

# Array for storing the number of wins of each player:
player_wins = []

# Array for storing the used dices
dices = []

# Initialize player rolls as empty lists for each player:
player_rolls_history = []

gameover = False
rounds = 0
#Obtain the number of players:
num_players = int(input("Enter the number of players "))

for i in range(num_players):
    name = input(f"Enter the name of player {i+1}: ")
    player_names.append(name)
    player_wins.append(0)
    player_rolls_history.append([])

#Add the dices to be used in the game:
for i in range(2):
    dices.append(dice.choose_dice())

# Repeats until the game is over. As many rounds as necessary:
while gameover is False:
    print(f"Round {rounds+1}:")
    current_rolls = []
    for i in range(num_players):
        roll = 0
        for d in dices:
            r = dice.dice_functions[d]()
            roll += r
            print(f"    Dice D{d} rolled a {r}")
        current_rolls.append(roll)
        player_rolls_history[i].append(roll)
        print(f"Player {player_names[i]} rolled a {roll}")
    
    input("\nPress ENTER to continue...")

    #Obtain the highest roll this round
    max_roll = max(current_rolls)

    #Winners will store information about who won this round
    winners = []
    for j in range(len(current_rolls)):
        if current_rolls[j] == max_roll:
            winners.append(player_names[j])
            player_wins[j] += 1
    
    print(f"Winner of this round are: {winners}")

    # Check if someone reached the winning score
    for z in range(num_players):
        if player_wins[z] >= winning_score:
            print(f"Player {player_names[z]} is the overall winner!")
            gameover = True
    
    if gameover is False:
        print("The heated Battle of Dices is still going on! Who will win in the end?")
    
    rounds += 1

# Save the results to a file
filename = input("Enter the filename to save the results (e.g., multiplayer_results.txt): ")
if filename is None or filename.strip() == "":
    filename = "multiplayer_results.txt"

with open(filename, 'w') as file:
    file.write(f"Game Results - Total Rounds: {rounds}\n")
    file.write(f"Dices used: {[dice.dice_functions[d].__name__ for d in dices]}\n\n")
    for round_number in range(rounds):
        file.write(f"Round {round_number + 1}:\n")
        rolls_str = ""
        for i in range(num_players):
            rolls_str += f"{player_names[i]} rolled {player_rolls_history[i][round_number]}"
            if i < num_players - 1:
                rolls_str += ", "
        print(f'Saving {rolls_str}')

        file.write(rolls_str + "\n")