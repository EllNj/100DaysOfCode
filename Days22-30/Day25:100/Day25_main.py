import csv

# with open("weather_data.csv") as data_file:
#     data  = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv('weather_data.csv')
# print(type(data))
# print(data['temp'])

# temp_list = data['temp'].to_list()
# print(temp_list)
#
# print(sum(temp_list) / len(temp_list))
# # or
# print(data['temp'].mean())
# print(data['temp'].max())

# get data in specific columns
data.condition
data.day

# what about to obtain rows
# print(data[data.day == 'Monday'])

# getting the day with the max temp
print(data[data.temp == data['temp'].max()])

monday = data[data.day == 'Monday']
monday_temp = (monday.temp * (9/5)) + 32
print(monday_temp)

# creating a data frame from scratch
