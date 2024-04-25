# 1. take userinput of n
# 2. for loop starting from n and ending at 999
# 3. check if i's modulus = 0, if so add it to the total

a = 100
divised_num = 0
n = int(input("Enter a number: "))

while a < 1000:
	if a%n == 0:
		divised_num = divised_num + a

	a = a + 1

print(divised_num)
	
