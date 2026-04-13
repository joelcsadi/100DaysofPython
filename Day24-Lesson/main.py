# Write Mode in relative Path
with open("Day24-Lesson/new_file.txt", mode= "w") as file:
    file.write("This is also cool!")

# Append Move with new line each append
with open("Day24-Lesson/my_file.txt", mode ="a") as file:
    file.write("\nThis is cool!")

# Reading the contents of the file
with open("Day24-Lesson/my_file.txt") as file:
    contents = file.read()
    print(contents)


