import pandas as pd

"""
Pandas is king for CSV files rather than manually opening normal .txt files.
"""

# # with open("Day25-Lesson/weather_data.csv") as data_file:
# #     data = data_file.readlines()
# # print(data)
# # temperatures = []
# # with open("Day25-Lesson/weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# # print(temperatures)

# data = pd.read_csv("Day25-Lesson/weather_data.csv")

# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# temp_series = data["temp"].to_list()

# print(data_dict)
# print(temp_series)

# # Basic Data Summaries
# print(data["temp"].mean())
# print(data["temp"].max())

# # Extracting columns using dictionary key extraction or as a class attribute where the column
# # is an attribute
# print(data["condition"])
# print(data.condition)

# # Extracting rows by filtering
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)

# monday_temp = monday.temp[0]
# monday_temp_fahrenheit = (monday_temp *(9/5)) + 32
# print(monday_temp_fahrenheit)

# data_dictionary = {
#     "students": ["Amy","James","Angela"],
#     "scores":[76,56,65]
# }
# new_data = pd.DataFrame(data_dictionary)
# print(new_data)
# new_data.to_csv("Day25-Lesson/new_data.csv")

data = pd.read_csv("Day25-Lesson/squirrel_data.csv")
# print(data["Primary Fur Color"])

grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

dict_data = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Counts": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df= pd.DataFrame(dict_data)
df.to_csv("Day25-Lesson/squirrel_counts.csv")
