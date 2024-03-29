import random
from deposit import deposit
from stake import get_stake

MAX_LINES = 3

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, stake, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * stake
            winning_lines.append(line + 1)
    
    
    return winnings, winning_lines

def get_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
             print(column[row], end=" | ")
            else:
                print(column[row],)

    #print()

def get_number_of_lines():
    while True:
        lines = input("enter number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("enter a valid no of lines")
        else:
            print("enter a number")
    return lines



def spinned(balance):
    lines = get_number_of_lines()
    while True:
        stake = get_stake()
        total_bet = stake * lines

        if total_bet > balance:
            print(f"You do not have enough balance, your current balance is {balance}")
        else:
            break

    #stake = get_stake()
    total_bet = stake * lines
    print(balance, lines, stake)
    print(f"you are staking KSH{stake} on {lines} lines. Total bet is {total_bet}")


    slots = get_spin(ROWS, COLS, symbol_count)
    print_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, stake, symbol_value)
    print(f"You won KSH {winnings}.")
    print(f"You won on lines:",*winning_lines)


    return winnings - total_bet

