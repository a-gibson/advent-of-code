#!/usr/bin/env python3

import pandas as pd

report = []

with open('input.txt') as input:
    for line in input:
        # For each line in the report, the characters are split into individual list elements
        report.append(list(line.rstrip()))

# Store in a Data Frame for easier manipulation in columns
df = pd.DataFrame.from_records(report)

gamma_rate = ""
epsilon_rate = ""

# Find the number of 1's and 0's in each column
# Calculate the gamma_rate / epsilon_rate from the relative frequencies of 1's and 0's
for column in df:
    zeros = df[column].value_counts()["0"]
    ones = df[column].value_counts()["1"]

    if zeros > ones:
        gamma_rate += "0"
        epsilon_rate += "1"
    else:
        gamma_rate += "1"
        epsilon_rate += "0"

# Provide answer in decimal
power_consumption = int(gamma_rate, 2) * int(epsilon_rate, 2)

print("Power consumption: {}".format(power_consumption))
