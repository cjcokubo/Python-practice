# Author: Christine Okubo
# Design and implement encoder and decoder functions that perform run length compression of strings
# Nov 15, 2019

def rlsencoder(string):
    temp = string[0]
    counter = 0
    final_list = []

    if len(string) == 0:
        return []

    for i in string:
        if temp == i:
            counter += 1
        else:
            final_list.append((temp, counter))
            temp = i
            counter = 1
    final_list.append((temp, counter))
    return final_list


def rlsdecoder(lst):
    final_string = ""
    for i in lst:
        final_string += i[0] * i[1]
    return final_string

print(rlsencoder('aadccccaa'))
print(rlsdecoder([['a',2], ['d',1], ['c',4], ['a',2]]))

