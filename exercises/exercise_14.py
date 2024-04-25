n = [4, 0, 23, 11, 0]
zeroes = 0

def count_zeroes (n):
	counter = 0
	for i in n:
		if i == 0:
			counter = counter + 1

	return counter

print (count_zeroes(n))
