#!/usr/bin/env python3

import pandas as pd

report = []

with open('input.txt') as input:
    for line in input:
        # For each line in the report, the characters are split into individual list elements
        report.append(list(line.rstrip()))

# Store in a Data Frame for easier manipulation in columns
df = pd.DataFrame.from_records(report)

filter = df

# Gradually filter out rows based on highest frequency of values in the columns
for column in df:
    zeros = filter[column].value_counts()["0"]
    ones = filter[column].value_counts()["1"]

    if zeros > ones:
        filter = filter.loc[filter[column] == "0"]
    else:
        filter = filter.loc[filter[column] == "1"]

    # Stop filtering if only one value left
    if len(filter.index) == 1:
        break

# Convert the remaining data frame row to a string
o_binary = ''.join(filter.values.tolist()[0])

filter = df

# Gradually filter out rows based on lowest frequency of values in the columns
for column in df:
    zeros = filter[column].value_counts()["0"]
    ones = filter[column].value_counts()["1"]

    if zeros > ones:
        filter = filter.loc[filter[column] == "1"]
    else:
        filter = filter.loc[filter[column] == "0"]

    # Stop filtering if only one value left
    if len(filter.index) == 1:
        break

# Convert the remaining data frame row to a string
co2_binary = ''.join(filter.values.tolist()[0])

# Provide answer in decimal
life_support_rating = int(o_binary, 2) * int(co2_binary, 2)

print("Life support rating: {}".format(life_support_rating))
