# Write A Program To Open A File And Ask The User To Input The Filename.
# If The File Exists, Display The Content Of The File,
# Else Create A File And Write The Line “File Is Opened In Write Mode”.


def file_operations():
    filename = input("Enter filename: ")
    
    try:
        with open(filename, "r") as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        with open(filename, "w") as file:
            file.write("File is opened in write mode.")
            print(f"File {filename} created and written to.")

file_operations()
