# n = int(input("Enter a number: "))
# a = n+1
# output = 0.5 + 2/3 + 0.75 + 4/5 + n/a
# print(output)


n = int(input("Enter a number: "))

numerator=0
denominator=0
total = 0

for i in range (n):
	numerator = numerator+1
	denominator = numerator+1
	print(numerator/denominator)
	total = total + numerator/denominator
	print(total)
	