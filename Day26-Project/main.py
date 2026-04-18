import pandas as pd
nato_df =pd.read_csv("Day26-Project/nato_phonetic_alphabet.csv")
# Selecting columns via dot notation in the row.
alphabet_dict = {row.letter:row.code for (index,row) in nato_df.iterrows()}

# List of Nato Code from user input
user_name_prompt = input("Enter your name to see it in code!").upper()
name_code = [alphabet_dict[char] for char in user_name_prompt]
print(name_code)