# Created by Mike Morey, originally created for Java.
# Figured I would build into a Python program for practice.
# Just a concept not a complete program by any means.

petType = input("cat / dog: ")
currentDogSpaces = 0
assignedDogSpace = ''
currentCatSpaces = 0
assignedCatSpaces = ''

#DOG

if petType == 'dog':
	print("okay its a dog checking availability...")
	if currentDogSpaces >= 30:
		 print("Sorry there are not enough spaces")
	else:
		 print('Okay updating space numbers. \n')
		 currentDogSpaces = currentDogSpaces + 1

	print("okay just need some more information... \n")
	print('Is this a returning pet or a new pet?')

	returningDog = input('Y or N: ')

	if returningDog == 'Y':
		print('Okay great a new pet! Please answer the following: \n')
		dogName = input('What is the pets name: ')
		dogWeight = int(input('What is the pets weight: '))
		dogAge = int(input("What is the pets age: "))
	elif returningDog == 'N':
		print('Okay great a returning doggo!')
		dogName = input('What is the returning pets name: ')
		dogAge = int(input('What is the dogs new age: '))
		dogWeight = int(input('What is the dogs new weight: '))
	else:
		while returningDog != 'N' or returningDog != 'Y':
			print('Invalid entry, try again')

	print('Alright, almost done. Just need a few more things... \n')
	print('How long is the pet staying for: ')
	dogStay = int(input('Enter number of days: '))

	if dogStay >= 2:
		print('Okay, are you looking to have the dog groomed?')
		dogGroom = input('Yes or No: ')
		if dogGroom == 'Yes':
			print('Okay great we will get the dog groomed during his stay!')
		else:
			dogGroom == 'No'
			print('Okay great another time then. \n')
	else:
		dogStay < 2
		print('Alright your pet is all set and booked for', petStay)

#CAT

if petType == 'cat':
	print("okay its a cat checking availability...")
	if currentCatSpaces >= 12:
		 print("Sorry there are not enough spaces")
	else:
		 print('Okay updating space numbers. \n')
		 currentCatSpaces = currentCatSpaces + 1

	print("okay just need some more information... \n")
	print('Is this a returning cat?')

	returningCat = input('Y or N: ')

	if returningCat == 'Y':
		print('Okay great a new kitty! Please answer the following: \n')
		catName = input('What is the cats name: ')
		catWeight = int(input('What is the cats weight: '))
		catAge = int(input("What is the cats age: "))
	elif returningCat == 'N':
		print('Okay great a returning kitty!')
		catName = input('What is the returning cats name: ')
		catAge = int(input('What is the cats new age: '))
		catWeight = int(input('What is the cats new weight: '))
	else:
		while returningCat != 'N' or returningCat != 'Y':
			print('Invalid entry, try again')

	print('Alright, almost done. Just need a few more things... \n')
	print('How long is the cat staying for: ')
	catStay = int(input('Enter number of days: '))

	print('Alright your cat is all set and booked for', petStay)
else:
	while petType != 'dog' or petType != 'cat':
		print('Invalid entry, try again...')