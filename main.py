import random

option=["rock","paper","scissors"]
computer_option=0
user_enter=input("Enter option (rock,paper or scissors)").lower()
if user_enter in option:
	print("Yes")
	ramdom_number=random.randint(0,2)
	computer_option=option[ramdom_number]
	print(computer_option)
	if computer_option==user_enter:
		print("Draw")
	elif user_enter=='rock' and computer_option=='paper':
		print("computer win")
	elif user_enter=='paper' and computer_option=='rock':
		print("user win")
	elif user_enter=='rock' and computer_option=='scissors':
		print("user win")
	elif user_enter=='scissors' and computer_option=='rock':
		print("Computer win")
	elif user_enter=='scissors' and computer_option=='paper':
		print("user win")
	elif user_enter=='paper' and computer_option=='scissors':
		print("Computer win")

	

else:
	print("Invalid option")