# Module 5 Lab Part 3
# David Vance
# Professor Kevin Chang
# CIS 129 - Programming and Problem Solving 1

'''The Bottle Return Program'''

# This program will calculate the total payout for bottles returned
# over a complete seven-day period.  The user is then prompted
# to start a new seven day period.

# Step 1: Initialize variables
keep_going = 'y'  # Set sentinel value


# Step 2: Loop to run program again
while keep_going == 'y':  # Start a week's worth of bottles
    # Set loop-specific variables
    total_bottles = 0  # Assign 0 to total_bottles
    total_payout = 0  #  Assign 0 to total_payout
    counter = 1  # Initiate loop counter

    for value in range(0,7):  # Avoid off-by-one error 
        # Maintain a cumulative total of bottles, and also increment the counter
        total_bottles += int(input('Enter number of bottles for day #' + str(counter) + ': '))
        counter += 1

    # Code to set value of variable total_payout
    total_payout = total_bottles * .10

    # Display weekly cumulative bottle count and total payout
    print('The total number of bottles collected is', total_bottles)
    print('The total paid out is $', f'{total_payout:.1f}')

    # Prompt user to see if they want to enter another week's worth of data
    print("Do you want to enter another week’s worth of data?")
    keep_going = input('(Enter y or n): ')

# End of the main While loop and end of module    