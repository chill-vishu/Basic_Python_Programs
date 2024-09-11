# Write A Program That Writes Three Lines Of Data To A File.

def write_to_file():
    with open("data.txt", "w") as file:
        file.write("Line 1: Hello, World!\n")
        file.write("Line 2: Python is great!\n")
        file.write("Line 3: Let's code!\n")
    print("Data written to file 'data.txt'.")

# Calling Function
write_to_file()
