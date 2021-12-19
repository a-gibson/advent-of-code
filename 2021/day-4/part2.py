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
board_tracker = list(range(len(boards)))
board_win = False
winning_indices = []
win_line = pd.Series(["*", "*", "*", "*", "*"])
won = False

for draw in draw_sequence:
    for idx, b in enumerate(boards):
        if idx in winning_indices:
            # Don't waste time by re-checking a board that's already won
            continue

        # The result of replace() is returned rather than completed in place
        boards[idx] = b.replace(draw, "*")

        # Search rows for winning line
        for _, row in boards[idx].iterrows():
            if board_win:
                break
            elif row.compare(win_line).empty:
                board_win = True

        # Search columns for winning line
        for _, data in boards[idx].iteritems():
            if board_win:
                break
            elif data.compare(win_line).empty:
                board_win = True

        # Allow multiple boards that have won with the same draw to be identified at the same time
        if board_win:
            board_tracker.remove(idx)
            board_win = False
            winning_indices.append(idx)
            won = True

    # When all boards have won, we will know which was the last winner
    if won:
        if len(board_tracker) == 0:
            winning_draw = draw
            break
        else:
            # Not the last board, keep going
            won = False

winning_idx = winning_indices[-1]

print("Found last winning board: #{}\n{}".format(winning_idx, boards[winning_idx]))
print("With draw: {}".format(winning_draw))

# Replace all '*' values with '0' to make the card easier to score
winner = boards[winning_idx].replace("*", "0")

# Convert to number type to make scoring easier
for idx, row in winner.iterrows():
    winner[idx] = pd.to_numeric(row)

# Add all non-matching values in the board
total = winner.to_numpy().sum()
print("Sum of remaining numbers on final board: {}".format(total))

final_score = int(total) * int(winning_draw)
print("Final score: {}".format(final_score))
