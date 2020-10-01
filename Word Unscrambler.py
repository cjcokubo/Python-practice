# Author: Christine Okubo
# Unscrambles words from a scrambled word bank.
# Nov 22, 2019

import random

def create_permutation(n):
    lst = []
    for num in range(n):
        lst.append(num)
    random.shuffle(lst)
    return lst

def scramble_word(word):
    n = len(word)
    lst = create_permutation(n)
    word_lst = []
    for num in lst:
        word_lst.append(word[num])
    new_word = ''.join(word_lst)
    return new_word

def main():
    file = open("word bank.txt", "r")

    lst = []
    num_words = 0
    for word in file:
        word = word.rstrip('\n')
        lst.append(word)
        num_words += 1
    word_num = random.randrange(num_words)

    i = 0
    for word in lst:
        if i == word_num:
            unscrambled = word
            break
        else:
            i += 1

    scrambled = scramble_word(unscrambled)
    print('Unscramble the word: ', scrambled)

    try_num = 1
    isTrue = True
    while isTrue:
        user_input = input('Try #{}: '.format(try_num))
        if user_input != unscrambled:
            print('Wrong!')
            try_num += 1
        else:
            print('Yay you got it!')
            isTrue = False

    file.close()

main()