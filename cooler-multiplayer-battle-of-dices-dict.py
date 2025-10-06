import sys, os
import copy

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)
from Labs.Lab2 import dice

# Variables to keep track of the score:
rounds = 0
gameover = False
#Number of wins needed to win the game
winning_score = 3

# Dictionary to store player information
player_info = {
    "name:": "",
    "email": "",
    "country": "",
    "wins": 0,
    "rolls": []
}

# List to store the dicts for each player
players = []

#Obtain the number of players:
num_players = int(input("Enter the number of players "))

# Array for storing the used dices
dices = []

# For loop to obtain player names:
for i in range(num_players):
    player = copy.deepcopy(player_info)

    player["name"] = input(f"Enter the name of player {i+1}: ")
    player["email"] = input(f"Enter the email of player {i+1}: ")
    player["country"] = input(f"Enter the country of player {i+1}: ")

    players.append(player)

for i in range(2):
    dices.append(dice.choose_dice())

# Repeats until the game is over. As many rounds as necessary:
while gameover is False:
    print(f"Round {rounds+1}:")
    
    #Dice roll for each player in the current round:
    current_rolls = []

    # We need to roll the dice for each player
    for each_player in players:
        roll = 0
        for d in dices:
            roll += dice.dice_functions[d]()

        each_player["rolls"].append(roll)
        current_rolls.append(roll)
        print(f"Player {each_player['name']} rolled: {roll}")
        
    max_roll = max(current_rolls)
    # Find winners of this round
    winners = []

    #Search for all players that rolled the max_roll
    for each_player in players:
        if each_player["rolls"][-1] == max_roll:
            winners.append(each_player["name"])
            each_player["wins"] += 1
            print(f"Player {each_player['name']} won in round {rounds+1}!")

            winners.append(each_player["name"])
    print(f"Winner(s) of this round: {winners}")
    
    for each_player in players:
        if each_player["wins"] >= winning_score:
            print(f"Player {each_player['name']} is the overall winner!")
            gameover = True
        
    if gameover is False:
        print("The heated Battle of Dices is still going on! Who will win in the end?")

    rounds += 1
        
# Save the results to a file
filename = input("Enter the filename to save the results: ")
if filename is None or filename.strip() == "":
    filename = "multiplayer_results_dict.txt"

with open(filename, 'w') as file:
    # Player information
    file.write("Player Information:\n")

    # Saves each player's info using python automatically string conversion of adjacent strings
    for each_player in players:
        file.write(
            f"Name: {each_player['name']}\n"
            f"Email: {each_player['email']}\n"
            f"Country: {each_player['country']}\n"
            f"Wins: {each_player['wins']}\n"
        )
    file.write("\nUsed Dices:\n")
    for d in dices:
        file.write(f"D{d}\n")
    file.write("\nGame rounds: \n")
    #Round history
    for r in range(rounds):
        rolls_str = ""
        for i, each_player in enumerate(players):
            rolls_str += f"{each_player['name']} rolled {each_player['rolls'][r]}"
            # Add a comma and space unless it's the last player
            if i < len(players) - 1:
                rolls_str += ", "
        # Now write the full round info to the file
        file.write(f"Round {r + 1}: {rolls_str}\n")
    
    print(f"Gameover! Results saved to {filename}")