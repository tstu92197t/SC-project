"""
File: caesar.py
name: Wu Ting
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    Users will be asked to input a number to produce shifted
    ALPHABET as the cipher table. After that, any strings typed
    in will be encrypted.
    Pre-condition: Users will input a number and a ciphered string
    Post-condition: This program will output the decipher string of
    the given ciphered string.
    """
    secret_number = int(input('Secret number: '))
    ciphered_string = input("What's the ciphered string?")
    ciphered_string = ciphered_string.upper()
    s = decipher(ciphered_string, secret_number, ALPHABET)
    print('The deciphered string is: '+s)


def decipher(ciphered, number, alphabet):
    """
    :param ciphered: str, the ciphered string given by the user
    :param number: int, a number to produce shifted ALPHABET as the cipher table
    :param alphabet: str, the string 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    :return: str, the deciphered string of the given ciphered string
    """
    ans = ''
    deciphered = ''
    ans += alphabet[len(alphabet)-number:]
    ans += alphabet[:len(alphabet)-number]  # ans is the string ALPHABET that shift "number" times
    for base in ciphered:
        i = ans.find(base)
        if i != -1:
            deciphered = deciphered + alphabet[i]
        else:
            if base == ' ':
                deciphered = deciphered + ' '
            else:
                j = ciphered.find(base)
                deciphered = deciphered + ciphered[j]
    return deciphered



#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
