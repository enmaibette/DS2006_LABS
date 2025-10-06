import random

def rollD3():
    return random.randint(1, 3)

def rollD4():
    return random.randint(1, 4)

def rollD5():
    return random.randint(1, 5)

def rollD6():
    return random.randint(1, 6)

def rollD8():
    return random.randint(1, 8)

def rollD12():
    return random.randint(1, 12)

def rollD20():
    return random.randint(1, 20)

def rollD100():
    return random.randint(1, 100)


dice_functions = {
    4: rollD4,
    6: rollD6,
    8: rollD8,
    12: rollD12,
    20: rollD20,
    100: rollD100
}

def choose_dice():
    dices_sides = 0
    while(dices_sides == 0):
        dices_sides_input = input("Enter the number of sides for the dice. Choose between D4, D6, D8, D12, D20 or D100. Enter the number only (4, 6, 8, 12, 20 or 100). :")
        if dices_sides_input.isdigit() is False or int(dices_sides_input) not in dice_functions.keys():
            print("Invalid input. Retry.")
        else: 
            dices_sides = int(dices_sides_input)

    return dices_sides