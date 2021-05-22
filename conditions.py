requested_toppings = ['mushrooms','extra cheese']

if 'mushrooms' in requested_toppings:
	print('Adding mushrooms.')
if 'pepperoni' in requested_toppings:
	print('Adding pepperoni')
if 'extra cheese' in requested_toppings:
	print('Adding extra cheese.')

print("\nFinished making your pizza!")

alien_color='Blue'

if alien_color.lower()=='green':
	print("You have earned 5 points.")
elif alien_color.lower()=='yellow':
	print("You have earned 10 points.")
elif alien_color.lower()=="red":
	print("You have earned 15 points.")
else:
	print("You have chosen some other color hence no points.")

age = 27

if age<2:
	print("The person is a baby")
elif age>=2 and age <4:
	print("The person is a toddler")
elif age>=4 and age<13:
	print("The person is a kid")
elif age>=13 and age<20:
	print("The person is a teenager")
elif age>=20 and age<65:
	print("The person is an adult")
elif age>=65:
	print("The person is an elder")

requested_toppings=['mushrooms','green peppers','extra cheese']

for requested_topping in requested_toppings:
	print(f"Adding {requested_topping}.")
print("\nFinished making your pizza")

requested_toppings=['mushrooms','green peppers','extra cheese']

for requested_topping in requested_toppings:
	if requested_topping=='green peppers':
		print("Sorry we are out of green peppers right now")
	else:
		print(f"Adding {requested_topping}")
print("\nFinished making your pizza")

requested_toppings=[]

if requested_toppings:
	for requested_topping in requested_toppings:
		print(f"Adding {requested_topping}.")
	print("\nFinished making your pizza")
else:
	print("Are you sure you want a plain pizza?")

available_toppings =['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings=['mushrooms','french fries','extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f"Adding {requested_topping}.")
	else:
		print(f"Sorry {requested_topping} is currently not available")

print("\nFinished making your pizza")

usernames = ['admin','Samar','Shashank','Anu','Parul']

if usernames:
	for username in usernames:
		if username=='admin':
			print("Hello admin, would you like to see a status report?")
		else:
			print(f"Hello {username}, thank you for loggin in again.")
else:
	print("We need to find some users.")

numbers=[1,2,3,4,5,6,7,8,9]

for number in numbers:
	if number == 1:
		print("1st\n")
	elif number == 2:
		print("2nd\n")
	elif number == 3:
		print("3rd\n")
	else:
		print(f"{number}th\n")