user_input = int(input("Please enter a number: "))
while user_input != 0:
	if user_input % 2 == 0:
		print(user_input, "is even")
	else:
		print(user_input, "is odd")
	user_input = int(input("Please enter a number: "))
print("Thanks")

