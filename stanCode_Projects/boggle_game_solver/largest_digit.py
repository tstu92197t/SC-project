"""
File: largest_digit.py
Name: Wu Ting
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n:an integer, the initial value
	:return: an integer, the maximum value
	"""
	if n < 0:
		n -= 2*n
	if (n // 10) == 0:
		return n % 10
	else:
		one = n % 10
		a = find_largest_digit(n//10)
		if a > one:
			return a
		else:
			return one


if __name__ == '__main__':
	main()

