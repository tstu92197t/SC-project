"""
File: complement.py
name: Wu Ting
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    Through this program, after the user gives a DNA strand, the user will get
    the complement strand of that DNA sequence
    Pre-condition: the user gives a DNA strand
    Post-condition: the user will get the complement strand of that DNA sequence
    """
    dna = input("Please give me a DNA strand and I'll find the complement: ")
    dna = dna.upper()  # case-insensitive
    print('The complement of '+dna+' is '+build_complement(dna))


def build_complement(dna):
    """
    :param dna: str, a string that the user gives, which is all capital
    :return: str, a string that is the complement of the given string, which is all capital
    """
    ans = ''
    for base in dna:
        if base == 'A':
            ans += 'T'
        elif base == 'T':
            ans += 'A'
        elif base == 'C':
            ans += 'G'
        elif base == 'G':
            ans += 'C'
    return ans


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
