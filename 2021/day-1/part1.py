#!/usr/bin/env python3

deeper = 0
previous = 0

with open('input.txt') as input:
    for line in input:
        current = int(line)

        # Don't try to compare when there is only one measurement (i.e. previous = 0)
        if previous != 0 and current > previous:
            deeper += 1

        previous = current

print (deeper)
