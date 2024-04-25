password = ("12345")

user_input = input("Enter password: ")

while password != user_input:
	print("Error")
	user_input = input("Enter password: ")

if password == user_input:
	print("Success")