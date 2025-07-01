# Python3 program to implement
# above approach

# Function to find the maximum profit
def maxProfit(prices, n):

	profit = 0
	currentDay = n - 1

	# Start from the last day
	while (currentDay > 0):
		day = currentDay - 1

		# Traverse and keep adding the
		# profit until a day with
		# price of stock higher
		# than currentDay is obtained
		while (day >= 0 and
			(prices[currentDay] >
			prices[day])):
			profit += (prices[currentDay] -
					prices[day])
						
			day -= 1
		
		# Set this day as currentDay
		# with maximum cost of stock
		# currently
		currentDay = day;
	
	# Return the profit
	return profit;

# Driver Code

# Given array of prices
prices = [ 2, 3, 5, 7 ]

N = len(prices)

# Function call
print(maxProfit(prices, N))

# This code is contributed by sanjoy_62
