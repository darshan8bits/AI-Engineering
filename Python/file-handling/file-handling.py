# Reading

file = open("text.txt", "r")
content = file.read()

print(content)

file.close()

# Writing / Overwriting

file = open("text.txt", "w")
file.write("hey I am overwriting the entire previous file")
file.close()

# Appending: Adding at the end

file = open("text.txt", "a")
file.write("\nAdded a new line1 \n")
file.write("Added a new line2 \n")

file.close()
