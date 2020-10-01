# Author: Christine Okubo
# Outputs stops of MTA Train Line inputted by user.
# Dec 6, 2019

import csv

def get_stop_id(data):
    stop_id_lst = []
    for i in data:
        stop = i[0][0]
        if stop not in stop_id_lst:
            stop_id_lst.append(stop)
    return stop_id_lst

def add_line(data, stop_id_lst):
    stops_dict = {}
    for stop in stop_id_lst:
        stops_lst = []
        for i in data:
            line = i[0][0]
            name = i[2]
            if line == stop and name not in stops_lst:
                stops_lst.append(name)
            else:
                continue
            stops_dict[stop] = stops_lst

    return stops_dict

def main():
    input_file = open('mta train stop data.csv', 'r')
    csv_reader = csv.reader(input_file)
    data = list(csv_reader)
    del data[0]

    stop_id_lst = get_stop_id(data)
    stops_dict = add_line(data, stop_id_lst)

    isTrue = True
    while isTrue:
        line = input('Please enter a train line or \'done\' to stop: ')
        if line in stop_id_lst:
            print(line, 'line:', ', '.join(stops_dict[line]))
        elif line == 'done':
            isTrue = False
        else:
            print('Please enter a valid input/train line.')

main()
