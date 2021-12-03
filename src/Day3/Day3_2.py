# -*- coding: utf-8 -*-
"""
@author Jegan Karunakaran
--- Part Two ---
Next, you should verify the life support rating, which can be determined by multiplying the oxygen generator rating by the CO2 scrubber rating.

Both the oxygen generator rating and the CO2 scrubber rating are values that can be found in your diagnostic report - finding them is the tricky part. Both values are located using a similar process that involves filtering out values until only one remains. Before searching for either rating value, start with the full list of binary numbers from your diagnostic report and consider just the first bit of those numbers. Then:

Keep only numbers selected by the bit criteria for the type of rating value for which you are searching. Discard numbers which do not match the bit criteria.
If you only have one number left, stop; this is the rating value for which you are searching.
Otherwise, repeat the process, considering the next bit to the right.
The bit criteria depends on which type of rating value you want to find:

To find oxygen generator rating, determine the most common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position. If 0 and 1 are equally common, keep values with a 1 in the position being considered.
To find CO2 scrubber rating, determine the least common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position. If 0 and 1 are equally common, keep values with a 0 in the position being considered.
For example, to determine the oxygen generator rating value using the same example diagnostic report from above:

Start with all 12 numbers and consider only the first bit of each number. There are more 1 bits (7) than 0 bits (5), so keep only the 7 numbers with a 1 in the first position: 11110, 10110, 10111, 10101, 11100, 10000, and 11001.
Then, consider the second bit of the 7 remaining numbers: there are more 0 bits (4) than 1 bits (3), so keep only the 4 numbers with a 0 in the second position: 10110, 10111, 10101, and 10000.
In the third position, three of the four numbers have a 1, so keep those three: 10110, 10111, and 10101.
In the fourth position, two of the three numbers have a 1, so keep those two: 10110 and 10111.
In the fifth position, there are an equal number of 0 bits and 1 bits (one each). So, to find the oxygen generator rating, keep the number with a 1 in that position: 10111.
As there is only one number left, stop; the oxygen generator rating is 10111, or 23 in decimal.
Then, to determine the CO2 scrubber rating value from the same example above:

Start again with all 12 numbers and consider only the first bit of each number. There are fewer 0 bits (5) than 1 bits (7), so keep only the 5 numbers with a 0 in the first position: 00100, 01111, 00111, 00010, and 01010.
Then, consider the second bit of the 5 remaining numbers: there are fewer 1 bits (2) than 0 bits (3), so keep only the 2 numbers with a 1 in the second position: 01111 and 01010.
In the third position, there are an equal number of 0 bits and 1 bits (one each). So, to find the CO2 scrubber rating, keep the number with a 0 in that position: 01010.
As there is only one number left, stop; the CO2 scrubber rating is 01010, or 10 in decimal.
Finally, to find the life support rating, multiply the oxygen generator rating (23) by the CO2 scrubber rating (10) to get 230.

Use the binary numbers in your diagnostic report to calculate the oxygen generator rating and CO2 scrubber rating, then multiply them together. What is the life support rating of the submarine? (Be sure to represent your answer in decimal, not binary.)

Your puzzle answer was 2845944.


"""


import pandas as pd


def split(word):
    return [char for char in word]

data = {}
key = 0
oxygen = []
co2 = []
with open("input.txt") as f:
    for line in f:
        l = split(line)
        #remove \n
        l.pop()
        data[key] = l
        key = key + 1

#print(data)
df = pd.DataFrame(data)
df = df.transpose()
#print(df)

print(df.describe())
df_oxy = df.copy()


def binaryToDecimal(binary):
     
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal

for i in range (0, len(df_oxy.columns)):
    most_sig_bit = df_oxy[i].value_counts().idxmax()
    most_sig_count =  df_oxy[i].value_counts().max()
    total_count = df_oxy[i].count()

    if total_count/2 == most_sig_count:
        df_oxy = df_oxy.loc[df_oxy[i] == '1']
    else:
        df_oxy = df_oxy.loc[df_oxy[i] == most_sig_bit]
    if len(df_oxy.index) < 2:
        break



df_co2= df.copy()

for i in range (0, len(df_co2.columns)):
    min_sig_bit = df_co2[i].value_counts().idxmin()
    min_sig_count =  df_co2[i].value_counts().min()
    total_count = df_co2[i].count()

    if total_count/2 == min_sig_bit:
        df_co2 = df_co2.loc[df_co2[i] == '0']
    else:
        df_co2 = df_co2.loc[df_co2[i] == min_sig_bit]
    if len(df_co2.index) < 2:
        break



print(df_oxy.iloc[0].values.tolist())
print(df_co2.iloc[0].values.tolist())

oxy_str = ''.join(df_oxy.iloc[0].values.tolist())
oxy_dec = binaryToDecimal(int(oxy_str))
print(oxy_dec)
co2_str = ''.join(df_co2.iloc[0].values.tolist())
print(co2_str)
co2_dec = binaryToDecimal(int(co2_str))
print(oxy_dec, co2_dec, oxy_dec * co2_dec)

