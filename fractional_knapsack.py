class Item:
	def __init__(self, profit, weight):
		self.profit = profit
		self.weight = weight
def fractionalKnapsack(W, arr):

	# Sorting Item on basis of ratio
	arr.sort(key=lambda x: (x.profit/x.weight), reverse=True) 
	finalvalue = 0.0
	for item in arr:
		if item.weight <= W:
			W -= item.weight
			finalvalue += item.profit
		else:
			finalvalue += item.profit * W / item.weight
			break
	return finalvalue

if __name__ == "__main__":
	W = int(input("Enter the maximum weight of the knapsack: "))
	n = int(input("Enter the number of items: "))
	arr = []
	for i in range(n):
		profit = float(input(f"Enter the profit of item {i+1}: "))
		weight = float(input(f"Enter the weight of item {i+1}: "))
		arr.append(Item(profit, weight))
	max_val = fractionalKnapsack(W, arr)
	print("The maximum value of the knapsack is:", max_val)
