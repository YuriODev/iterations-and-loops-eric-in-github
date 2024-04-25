arr = []
count = 0
days = int(input("Enter number of days: "))
for i in range (days):
	temp = int(input("Enter the temperature:"))
	arr.append(temp)

for i in arr:
	if i < count:
		count = i

	if i < -15:
		print ("Yes")
	
print(count)

	