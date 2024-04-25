arr = []
min_speed = float("inf")
max_speed = 0
count = 0
num_cars = int(input("Enter number of cars: "))
for i in range (num_cars):
	arr.append (int(input("Enter the speed of the car: ")))

for i in arr:
	if i < min_speed:
		min_speed = i

	elif i > max_speed:
		max_speed = i

	elif i < 31:
		count = count + 1

print (min_speed)
print(max_speed)
print(count)
		

	
	