#!/usr/bin/env python3

import pandas as pd

# The first line of the file contains the sequence of called numbers
# Subsequent lines contain the boards of number (5x5 squares) to match against called numbers
# Store the boards in an array of data frames
with open('input.txt') as input:
    board = []
    boards = []
    first = True
    second = False

    for line in input:
        if first:
            first = False
            second = True
            draw_sequence = list(line.rstrip().split(","))
            continue

        # Skip the first blank line (subsequent blank lines are board separators)
        if second:
            second = False
            continue

        if not line.strip():
            boards.append(pd.DataFrame.from_records(board))
            board.clear()
            continue
    
        board.append(list(line.rstrip().split()))

# print(draw_sequence)
# print(boards)

# Work through the draw sequence and match the draw within each board
win_line = pd.Series(["*", "*", "*", "*", "*"])
won = False

for draw in draw_sequence:
    for idx, b in enumerate(boards):
        # The result of replace() is returned rather than completed in place
        boards[idx] = b.replace(draw, "*")

        # Search rows for winning line
        for _, row in boards[idx].iterrows():
            if row.compare(win_line).empty:
                winning_board = idx
                winning_draw = draw
                won = True
            
            if won:
                break

        # Search columns for winning line
        for _, data in boards[idx].iteritems():
            if data.compare(win_line).empty:
                winning_board = idx
                winning_draw = draw
                won = True

            if won:
                break

        if won:
            print("Found winning board: #{}\n{}".format(winning_board, boards[idx]))
            break

    if won:
        print("With draw: {}".format(winning_draw))
        break

# Replace all '*' values with '0' to make the card easier to score
winner = boards[winning_board].replace("*", "0")

# Convert to number type to make scoring easier
for idx, row in winner.iterrows():
    winner[idx] = pd.to_numeric(row)

# Add all non-matching values in the board
total = winner.to_numpy().sum()

final_score = int(total) * int(winning_draw)

print("Final score: {}".format(final_score))
