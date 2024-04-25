def sum_factorials (n):

	factorial = 1
	total = 0

	for i in range (1, n+1):
		factorial = factorial * i
		total += factorial


	print(total)

sum_factorials(3)