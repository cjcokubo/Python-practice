# Christine Okubo
# What’s the weather like? - Data Cleaning and Management
# Nov 22, 2019

import csv

# Part A - data	massaging
def clean_data(complete_weather_filename, cleaned_weather_filename):
    input_file = open(complete_weather_filename, 'r')
    csv_reader = csv.reader(input_file)
    data = list(csv_reader)
    header = data[0]

    IndexC = header.index('City')
    IndexD = header.index('Date')
    IndexH = header.index('High')
    IndexL = header.index('Low')
    IndexP = header.index('Precipitation')

    del data[0]

    data_lst = []
    for line in data:
        line_lst = []
        line_lst.append(line[IndexC])
        line_lst.append(line[IndexD])
        line_lst.append(line[IndexH])
        line_lst.append(line[IndexL])
        try:
            float(line[IndexP])
            line_lst.append(line[IndexP])
        except ValueError:
            line_lst.append(0)
        data_lst.append(line_lst)

    output_file = open(cleaned_weather_filename, 'w', newline='')
    writer = csv.writer(output_file)
    writer.writerows(data_lst)

    return output_file

def f_to_c(f_temp):
    c_temp = (f_temp - 32) * 5/9
    return int(c_temp)

def in_to_cm(inch):
    cm = inch * 2.54
    return int(cm)

def convert_data_to_metric(imperial_weather_filename, metric_weather_filename):
    input_file = open(imperial_weather_filename, 'r')
    csv_reader = csv.reader(input_file)
    data = list(csv_reader)
    header = data[0]

    IndexC = header.index('City')
    IndexD = header.index('Date')
    IndexH = header.index('High')
    IndexL = header.index('Low')
    IndexP = header.index('Precipitation')

    del data[0]

    data_lst = []
    for line in data:
        line_lst = []
        line_lst.append(line[IndexC])
        line_lst.append(line[IndexD])
        line_lst.append(f_to_c(int(line[IndexH])))
        line_lst.append(f_to_c(int(line[IndexL])))
        try:
            float(line[IndexP])
            line_lst.append(in_to_cm(int(line[IndexP])))
        except ValueError:
            line_lst.append(0)
        data_lst.append(line_lst)

    output_file = open(metric_weather_filename, 'w', newline='')
    writer = csv.writer(output_file)
    writer.writerows(data_lst)

    return output_file

def print_averages_per_month(city, weather_filename, unit_type):
    # prints average highs and lows in each month for the given city

    print('Average temperatures for', city)

    month_lst = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                 'November', 'December']

    if unit_type == 'imperial':
        clean_data('weather.csv', weather_filename)
        input_file = open(weather_filename, 'r')
        csv_reader = csv.reader(input_file)
        data = list(csv_reader)

    elif unit_type == 'metric':
        convert_data_to_metric('weather.csv', weather_filename)
        input_file = open(weather_filename, 'r')
        csv_reader = csv.reader(input_file)
        data = list(csv_reader)
    else:
        print('Invalid unit type.')

    city_lst = []
    for lst in data:
        if lst[0] == city:
            city_lst.append(lst)

    high_sums = []
    high_ave = []
    low_sums = []
    low_ave = []
    for i in range(1, 13):
        counter = 0
        hsum = 0
        lsum = 0
        for j in city_lst:
            date_lst = j[1].split('/')
            if int(date_lst[0]) == i:
                hsum += int(j[2])
                lsum += int(j[3])
                counter += 1
            else:
                continue
        high_sums.append(hsum)
        high_ave.append(int(hsum/counter))
        low_sums.append(lsum)
        low_ave.append(int(lsum/counter))

    k = 0
    if unit_type == 'imperial':
        for month in month_lst:
            print(month, ': ', high_ave[k], 'F High, ', high_ave[k], 'F Low')
            k += 1
    elif unit_type == 'metric':
        for month in month_lst:
            print(month, ': ', high_ave[k], 'C High, ', high_ave[k], 'C Low')
            k += 1
    else:
        print('Invalid unit type.')

# Part D
# Finding the difference in average temperature of two cities during a certain month
def diff_ave_temp(city1, city2, month, unit_type, weather_filename):
    if unit_type == 'imperial':
        clean_data('weather.csv', weather_filename)
        input_file = open(weather_filename, 'r')
        csv_reader = csv.reader(input_file)
        data = list(csv_reader)

    elif unit_type == 'metric':
        convert_data_to_metric('hw8 - weather.csv', weather_filename)
        input_file = open(weather_filename, 'r')
        csv_reader = csv.reader(input_file)
        data = list(csv_reader)
    else:
        print('Invalid unit type.')

    month_lst = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                 'November', 'December']
    month_index = month_lst.index(month)

    city1_lst = []
    for lst in data:
        if lst[0] == city1:
            city1_lst.append(lst)

    city2_lst = []
    for lst in data:
        if lst[0] == city2:
            city2_lst.append(lst)

    counter1 = 0
    h1sum = 0
    l1sum = 0
    for j in city1_lst:
        date_lst = j[1].split('/')
        if int(date_lst[0]) == month_index + 1:
            h1sum += int(j[2])
            l1sum += int(j[3])
            counter1 += 1
        else:
            continue
        high1_ave = int(h1sum / counter1)
        low1_ave = int(l1sum / counter1)


    counter2 = 0
    h2sum = 0
    l2sum = 0
    for j in city2_lst:
        date_lst = j[1].split('/')
        if int(date_lst[0]) == month_index + 1:
            h2sum += int(j[2])
            l2sum += int(j[3])
            counter2 += 1
        else:
            continue
    high2_ave = int(h2sum / counter2)
    low2_ave = int(l2sum / counter2)

    if unit_type == 'imperial':
        print('The difference in average temperatures between', city1, 'and', city2, 'during', month, 'is', high1_ave-high2_ave, 'F High and', low1_ave-low2_ave, 'F Low.')
    elif unit_type == 'metric':
        print('The difference in average temperatures between', city1, 'and', city2, 'during', month, 'is', high1_ave-high2_ave, 'C High and', low1_ave-low2_ave, 'C Low.')
    else:
        print('Invalid unit type.')


def main():
    print ("Running Part A")
    clean_data("weather.csv", "weather in imperial.csv")
    
    print ("Running Part B")
    convert_data_to_metric("weather.csv", "weather in metric.csv")
    
    print ("Running Part C")
    print_averages_per_month("San Francisco", "weather in imperial.csv", "imperial")
    print_averages_per_month("New York", "weather in metric.csv", "metric")
    print_averages_per_month("San Jose", "weather in imperial.csv", "imperial")

    print ("Running Part D")
    print('This program finds the difference in average temperature of two cities during a certain month (ave. temp of city1 - ave. temp of city2)')
    city1 = input('Enter the first city: ')
    city2 = input('Enter the second city: ')
    month = input('Enter a month: ')
    unit_type = input('What unit do you want the values in?:  ')
    diff_ave_temp(city1, city2, month, unit_type, 'partd.csv')

main()