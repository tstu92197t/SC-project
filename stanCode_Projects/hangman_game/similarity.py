"""
File: similarity.py
name: Wu Ting
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    This program compares short dna sequence, s2, with sub sequences of a long dna sequence, s1
    and will output the most similar part of the s2.
    Pre-condition: The user provides s2, s1
    Post-condition: This program will output the most similar part of the s2.
    """
    long_sequence = input('Please give me a DNA sequence to search: ')
    short_sequence = input('What DNA sequence would you like to match: ')
    long_sequence = long_sequence.upper()
    short_sequence = short_sequence.upper()
    s = best_match(long_sequence, short_sequence)
    print(s)


def best_match(ref, read):
    """
    param ref: str, the long sequence provided by the user
    param read: str, the short sequence provided by the user
    param similarity: integer, the similar degree (if match, similarity will plus one)
    param max: integer, the maximum
    param index: integer
    return str
    """
    similarity = 0
    max_value = 0
    index = 0
    for i in range(len(ref)-len(read)+1):  # the comparison between ref and read has len(ref)-len(read)+1 times
        for j in range(len(read)):  # at a time, the sub sequence of the ref will compares with read for len(read) times
            if ref[j+i] == read[j]:
                similarity += 1
                if similarity > max_value:
                    max_value = similarity
                    index = i
        similarity = 0  # before another comparision between ref and read, we will initialize the similarity
    ans = ''
    for base in ref[index:(index+len(read))]:
        if base == 'A':
            ans += 'A'
        elif base == 'T':
            ans += 'T'
        elif base == 'C':
            ans += 'C'
        else:
            ans += 'G'
    return ans






###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
