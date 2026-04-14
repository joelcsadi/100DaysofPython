PLACEHOLDER = "[name]"

# Extracting names from files into a list.
with open("Day24-Project/Input/Names/invited_names.txt") as names_file:
    invited_names = names_file.readlines()

# Extract the letter template
with open("Day24-Project/Input/Letters/starting_letter.txt") as letter_file:
    letter_template= letter_file.read()
    for name in invited_names:
        stripped_name = name.strip()
        new_letter =letter_template.replace(PLACEHOLDER, stripped_name)
        # Write the new letter in files for every name
        with open(f"Day24-Project/Output/ReadyToSend/letter_for_{stripped_name}.txt", mode = "w") as completed_letter:
            completed_letter.write(new_letter)