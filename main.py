import random



MAX_LINES = 3
MAX_STAKE = 1000
MIN_STAKE = 50

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

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

def deposit():
    while True:
        amount = input("what would you like to deposit? KSH ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("amount greater than 0")
        else:
            print("please enter a number")
    return amount


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

def get_stake():
    while True:
        stake = input("enter stake amount ")
        if stake.isdigit():
            stake = int(stake)
            if MIN_STAKE <= stake <= MAX_STAKE:
                break
            else:
                print(f"amount must be between {MIN_STAKE} - {MAX_STAKE}")
        else:
                print("enter stake")
    return stake



def main():
    balance = deposit()
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

main()
