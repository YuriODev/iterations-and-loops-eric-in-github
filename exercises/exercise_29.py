inputs = [5,5,-10]
def sum_of_squares (inputs):

	arr = []
	total = 0
	ans = 0
	
	for x in inputs:
		arr.append (x)
		total = total + x
		if total == 0:
			for i in arr:
				ans = ans + i**2
			return ans

print(sum_of_squares(inputs))
			