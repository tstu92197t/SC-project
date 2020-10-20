"""
File: rocket.py
name: Wu Ting
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

SIZE = 5  # the size of rocket


def main():
	"""
	This program should implement a console program that draws ASCII art - a rocket.
	Pre-condition: The user can determine the size of rocket.
	Post-condition: The user will get the ASCII art - a rocket according to the given size.
	"""
	head()
	belt()
	upper()
	lower()
	belt()
	head()


def head():
	"""
	This function determines the head part (the upper part) of the the rocket
	"""
	for i in range(SIZE):
		for j in range(SIZE*2+2):
			if j == (SIZE-i):
				for k in range(i+1):
					print('/', end='')
				for k in range(i+1):
					print('\\', end='')
			print(' ', end='')
		print('')


def belt():
	"""
	This function determines the belt part (the second part) of the the rocket
	"""
	for i in range(SIZE*2+2):
		if i == 0 or i == SIZE*2+1:
			print('+', end='')
		else:
			print('=', end='')
	print('')


def upper():
	"""
	This function determines the third part of the the rocket
	"""
	for i in range(SIZE):
		for j in range(SIZE*2+2):
			if j == 0 or j == SIZE*2+1:
				print('|', end='')
			elif (i+j) == SIZE:
				print('/', end='')
			elif j == SIZE+i+1:
				print('\\', end='')
			elif (SIZE-i) < j < (SIZE+i+1):
				if (i+j) % 2 == 1:
					print('\\', end='')
				else:
					print('/', end='')
			else:
				print('.', end='')
		print('')


def lower():
	"""
	This function determines the forth part of the the rocket
	"""
	for i in range(SIZE):
		for j in range(SIZE*2+2):
			if j == 0 or j == SIZE*2+1:
				print('|', end='')
			elif (i+j) == SIZE*2:
				print('/', end='')
			elif j-i == 1:
				print('\\', end='')
			elif 1+i < j < SIZE*2-i:
				if (i+j) % 2 == 1:
					print('\\', end='')
				else:
					print('/', end='')
			else:
				print('.', end='')
		print('')






###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()