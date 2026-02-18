board = [
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
]

letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
}


def ask_position():
    column = input("column (A to E): ").upper()
    while column not in "ABCDE":
        print("That column is wrong! It should be A, B, C, D or E")
        column = input("column (A to E): ").upper()

    row = input("row (1 to 5): ")
    while row not in "12345":
        print("That row is wrong! it should be 1, 2, 3, 4 or 5")
        row = input("row (1 to 5): ")

    return int(row) - 1, letters_to_numbers[column]


def print_board(board):
    print("  A B C D E")
    print(" +-+-+-+-+-+")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        print(" +-+-+-+-+-+")
        row_number += 1


ships_placed = 0

while ships_placed < 5:
    print(f"Where do you want ship {ships_placed + 1}?")
    row_number, column_number = ask_position()

    # Унікальність кораблів
    if board[row_number][column_number] == 'X':
        print("That spot already has a battleship in it! Choose another position.")
        continue

    board[row_number][column_number] = 'X'
    ships_placed += 1
    print_board(board)


print("\n" * 50)


guesses_board = [
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
]


hits = 0
misses_left = 5  

while hits < 5 and misses_left > 0:
    print("\nGuess a battleship location")
    print(f"Misses remaining (in a row): {misses_left}")

    row_number, column_number = ask_position()

    # я вже це пробувала
    if guesses_board[row_number][column_number] != ' ':
        print("You have already guessed that place!")
        continue

    # перевірка попадання
    if board[row_number][column_number] == 'X':
        print("HIT!")
        guesses_board[row_number][column_number] = 'X'
        hits += 1
        misses_left = 5  #тут я скидаю лічильник
        print("Your miss counter has been reset to 5!")
    else:
        print("MISS!")
        guesses_board[row_number][column_number] = '.'
        misses_left -= 1

    print_board(guesses_board)


if hits == 5:
    print("\n YOU WIN! You found all battleships!")
else:
    print("\n GAME OVER! You missed 5 times in a row.")
