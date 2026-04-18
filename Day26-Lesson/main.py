import random 
import pandas as pd
numbers =[1,2,3,4]
## For loop list method of updating an existing list.
new_numbers = []
for n in numbers:
    new_num= n + 1
    new_numbers.append(new_num)

print(new_numbers)

## List Comprehension
new_numbers = [n+1 for n in numbers]
print(new_numbers)

double_list = [2*num for num in range(1,5)]
print(double_list)

## Conditional List Comprehensions
names = ["Alex", 'Beth', 'Caroline','Dave','Eleanor','Freddie']
short_names = [name for name in names if len(name) < 5]
long_names_uppercase = [name.upper() for name in names if len(name)> 4]
print(short_names)
print(long_names_uppercase)

## Dictionary Comprehensions (iterating through exising list.)
scores = {name:random.randint(0,100) for name in names}
print(scores)

# (Iterating through existing dictionary)
passed_students = {name:score for (name,score) in scores.items() if score >= 40}
print(passed_students)

student_dict = {
    "student": ["Angela","James", 'Lily'],
    'score': [56,76,98]
}
student_dataframe = pd.DataFrame(student_dict)
print(student_dataframe)

## Looping through dataframes columns. Not really useful we want to iterate through rows.
for key, value in student_dataframe.items():
    print(value)

for (index, row) in student_dataframe.iterrows():
    print(row.student)