# Initialize an integer for list size here.

list_size = 8
print(f"You will be asked to enter {list_size} batting averages.")

# Initialize list here.

averages = []

# Write a loop to get batting averages from user and add to list.

for i in range(list_size):

    # String version of batting average input by user.

    averageString = input("Enter a batting average: ")

    # Use this variable to store the batting average input by user.

    battingAverage = float(averageString)

    # add value to list.

    averages.append(battingAverage)

# Use these variables to store the minimim and maximum batting averages.
# Assign the first element in the list to be the minimum and the maximum.

min = averages[0]

max = averages[0]


# Start out your total initialized to 0.

total = 0


# Write a loop here to access list values starting with averages[1]

for average in averages[1:]:

    # Within the loop test for minimum and maximum batting averages.

    if average < min:
        min = average
    if average > max:
        max = average

    # Also accumulate a total of all batting averages.

    total += average

total += averages[0]

# Calculate the average of the 8 averages.

average_of_averages = total / list_size

# Print the averages stored in the averages list.

print("Batting averages entered:", averages)

# Print the maximum batting average, minimum batting average, and average batting average.
print("Minimum batting average:", min)
print("Maximum batting average:", max)
print("Average of batting averages:", average_of_averages)