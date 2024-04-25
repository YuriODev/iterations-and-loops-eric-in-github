# def odd_nums (final_num):
# 	counter = 0
# 	n = 0
	
# 	while counter != final_num:
# 		n = n + 1 
# 		if n % 2 != 0:
# 			print (n)
# 		counter = counter + 1

# odd_nums(15)


def odd_nums (final_num):
	counter = 0
	odd_list = []
	while counter != final_num:
		counter = counter + 1
		if counter % 2 != 0:
			odd_list.append (counter)
		return odd_list

print (odd_nums(15))