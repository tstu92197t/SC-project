"""
File: hangman.py
name: Wu Ting
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
to try in order to win this game.
"""


import random


# This constant controls the number of guess the player has
N_TURNS = 7


def main():
    """
    Through this program, users can play a hangman game.
    Users sees a dashed word, trying to correctly figure the un-dashed word out
    by inputting one character each round.
    Pre-condition: Users sees a dashed word, and input one character
    Post-condition: If the user input is correct, show the updated word on console,
    or else shows that the user was wrong
    """
    s = random_word()
    dashed = ''
    for i in range(len(s)):  # forming the dashed at the beginning
        dashed += '-'
    print('The word looks like: '+dashed)
    count = N_TURNS
    print('You have '+str(count)+' guesses left.')
    input_all = ''  # input_all includes all the input in each round
    while True:
        input_ch = input('Your guess: ')
        check_alpha = input_ch.isalpha()
        # check whether the input is an alphabet or string that its length is over 1
        if check_alpha == False or len(input_ch) != 1:
            print('illegal format.')
        else:
            input_ch = input_ch.upper()  # case-insensitive
            input_all = input_ch + input_all
            j = s.find(input_all[:1])  # check if we can find the input at this round in s
            if j != -1:  # your guess is right (found)
                dashed = ''
                for base in s:
                    ans = '-'  # the default output is a dash
                    for k in range(len(input_all)):
                        if base == input_all[k]:
                            ans = input_all[k]
                    dashed += ans
                print('You are correct!')
                i = dashed.find('-')
                if i != -1:  # found '-' in dashed string
                    print('The word looks like: ' + dashed)
                    print('You have ' + str(count) + ' guesses left.')
                else:  # does not find '-' in dashed string
                    print('You win!!')
                    print('The word was: '+str(s))
                    return
            else:  # the case that the user guess wrong
                print('There is no '+str(input_ch)+"'s in the word.")
                count -= 1  # the number of guess the player has minus one
                if count == 0:
                    print('You are completely hung : (')
                    print('The word was: '+str(s))
                    return
                else:
                    print('The word looks like: ' + dashed)
                    print('You have ' + str(count) + ' guesses left.')


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
