# n = int(input("Enter numbers: "))
# total = 0
# counter = 1
# while n != 0:
# 	total = n + total
# 	n = int(input("Enter numbers: "))

# print(total)

# n = int(input("Enter numbers: "))
# arr = []
# while n != 0:
# 	arr.append(n)


arr = [3, 4, 5, 0]

def numbers (arr):
	total = 0
	for i in arr:
		if i == 0:
			break
		total = i + total


	avg = total/len(arr)+1
	return avg
print(numbers(arr))