# 30 Days of Code

# Meal Price Calculations 


# Given the meal price (base cost of a meal)

meal_price = 60

# tip percent (the percentage of the meal price being added as tip)

tip_percent = 15 

# and tax percent (the percentage of the meal price being added as tax) for a meal

tax_percent = 8

# find and print the meal's total cost:

# Cost of meal = 60 
# A tip of 15% * 60 = 9
# The taxes are 8% * 60 = 4.80

# Round the result to the nearest integer:

# Reult = 60 + 9 + 4.80 = 73.80 
# Round to 74



# Function Description
# Solve using a function: 

# Use the following parameters:

# int meal_cost: the cost of food before tip and tax
# int tip_percent: the tip percentage
# int tax_percent: the tax percentage

# Returns The function returns nothing. Print the calculated value, rounded to the nearest integer.

# Note: Be sure to use precise values for your calculations, or you may end up with an incorrectly rounded result.

# Input Format

# There are 3 lines of numeric input:
# The first line has a double, meal_cost(the cost of the meal before tax and tip).
# The second line has an integer, tip_percent(the percentage of meal_cost being added as tip).
# The third line has an integer, tax_percent(the percentage of meal_cost being added as tax).

# Sample Input

# 12.00
# 20
# 8

# Sample Output

# 15

# Explanation

# Given:

# meal_cost = 12 
# tip_percent = 20
# tax_percent = 8

# Calculations

# tip = 12 + 0.12 *20 =  2.4
# tax =  8 + 0.08 *12 = 0.96
# total_cost = meal_cost + tip + tax = 12 + 2.4 + 0.96 = 15.36

# round(total_cost) = 15

# We round total_cost to the nearest integer and print the result, 15.