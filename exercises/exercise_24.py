arr = [3, 4, 5, 6, 8, 0]

def numbers (arr):
	total = 0
	for i in arr:
		if i == 0:
			break
		elif i % 2 == 0:
			total = total +1

	return total

print(numbers(arr))