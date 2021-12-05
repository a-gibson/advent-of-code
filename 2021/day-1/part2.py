#!/usr/bin/env python3

with open('input.txt') as input:
    lines = input.read().splitlines()

deeper = 0
new_window = 0
previous_window = 0
window_size = 3

for idx, _ in enumerate(lines):
    new_window = int(lines[idx]) + int(lines[idx + 1]) + int(lines[idx + 2])

    if idx != 0 and new_window > previous_window:
        deeper += 1

    if len(lines) - idx <= window_size:
        # There's not enough data to calculate the next full window
        break

    previous_window = new_window

print (deeper)
