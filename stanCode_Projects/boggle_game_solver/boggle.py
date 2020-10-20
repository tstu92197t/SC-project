"""
File: boggle.py
Name: Wu Ting
----------------------------------------
TODO:
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
dict_list = []


def main():
	"""
	TODO:
	"""
	read_dictionary()
	s1 = input('1 row of letters: ')
	if len(s1) != 7:
		print('Illegal input')
		return
	s2 = input('2 row of letters: ')
	if len(s1) != 7:
		print('Illegal input')
		return
	s3 = input('3 row of letters: ')
	if len(s1) != 7:
		print('Illegal input')
		return
	s4 = input('4 row of letters: ')
	if len(s1) != 7:
		print('Illegal input')
		return
	lst = (s1 + ' ' + s2 + ' ' + s3 + ' ' + s4).split()

	boggle(lst)


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global dict_list
	with open(FILE, 'r') as f:
		for line in f:
			line_list = line.split('\n')
			first_word = line_list[0]
			dict_list.append(first_word)


def boggle(lst):
	"""
	:param s:
	:return:
	"""
	ans = []
	unused = list(range(len(lst)))
	for curr_y in range(4):
		for curr_x in range(4):
			unused.remove(curr_x + 4*curr_y)
			_ = boggle_helper(lst, curr_x, curr_y, lst[curr_x + 4*curr_y], unused, 4, ans)
			unused.append(curr_x + 4*curr_y)
	print('There are ', len(ans), 'words in total')


def boggle_helper(lst, curr_x, curr_y, curr_str, unused, target_length, ans):
	if len(curr_str) >= target_length and curr_str not in ans:
		for i in range(len(dict_list)):
			comparand = dict_list[i]
			if comparand == curr_str:
				print('Found: ', curr_str)
				ans.append(curr_str)
				return True
		return False
				
	else:
		for y in [-1, 0, 1]:
			for x in [-1, 0, 1]:
				if curr_x + x < 0 or curr_y + y < 0 or curr_x + x > 3 or curr_y + y > 3 or (x == 0 and y == 0):
					pass
				else:
					if curr_x + x + 4*(curr_y + y) in unused:
						curr_str = curr_str + lst[curr_x + x + 4*(curr_y + y)]
						unused.remove(curr_x + x + 4*(curr_y + y))
						if has_prefix(curr_str):
							found_ans = boggle_helper(lst, curr_x + x, curr_y + y, curr_str, unused, target_length, ans)
							if found_ans:
								target_length += 1
								boggle_helper(lst, curr_x + x, curr_y + y, curr_str, unused, target_length, ans)
						target_length = 4
						unused.append(curr_x + x + 4*(curr_y + y))
						curr_str = curr_str[:-1]
		return False


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A sublst that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for i in range(len(dict_list)):
		comparand = dict_list[i]
		if comparand.startswith(sub_s):  #Found-True
			return True
	return False



if __name__ == '__main__':
	main()
