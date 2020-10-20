"""
File: anagram.py
Name: Wu Ting
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

dict_list = []
sub_s = ''


def main():
    read_dictionary()
    print('Welcome to stanCode "Anagram Generator"( or', EXIT, 'to quit)')
    while True:
        s = input('Find anagram for: ')
        if s == EXIT:
            return
        else:
            find_anagrams(s)


def read_dictionary():
    global dict_list
    with open(FILE, 'r') as f:
        for line in f:
            line_list = line.split('\n')
            first_word = line_list[0]
            dict_list.append(first_word)


def find_anagrams(s):
    """
    :param s: a string, the input word
    :return: doesn't return anything
    """
    ans = []
    print('Searching...')
    find_anagrams_helper(s, '', len(s), list(s), ans)
    print(len(ans), 'anagrams: ', ans)


def find_anagrams_helper(string, current_str, target_length, unused, ans):
    """
    :param string: a string, the input word
    :param current_str: a string, which is initially ''
    :param target_length: an integer, the length of s
    :param unused: a list, contained by the letter in s
    :param ans: a list, storing the anagrams
    :return: doesn't return anything
    """
    if len(current_str) == target_length and current_str not in ans:
        if has_prefix(current_str) and len(has_prefix(current_str)) == len(current_str):
            print('Found: ', current_str)
            ans.append(current_str)
            print('Searching...')
    else:
        for ele in string:
            if ele in unused:  # I store all the letters in s in unused, which is a list
                # Choose
                current_str = current_str + ele
                unused.remove(ele)
                # Explore
                if has_prefix(current_str):
                    find_anagrams_helper(string, current_str, target_length, unused, ans)
                # Un-choose
                unused.append(current_str[-1])
                current_str = current_str[:-1]


def has_prefix(sub):
    """
    :param sub: a string, the substring of s
    :return: a string, the ith string in the dict_list
    """
    for i in range(len(dict_list)):
        comparand = dict_list[i]
        if comparand.startswith(sub):
            return comparand


if __name__ == '__main__':
    main()
