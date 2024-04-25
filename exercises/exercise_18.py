def total_errors(days, num_errors):
	counter = 0
	num_errors = 0
	
	while counter != days:
		num_errors =  num_errors + int(input("Enter number of errors"))
		
		counter = counter + 1

	print (num_errors)

total_errors(5, 2)