# Create A Program That Demonstrates The Following Tasks: Creating A List, Appending, Inserting, Removing, Sorting, And Copying Elements Within The List, Accessing Elements In A Dictionary, And Working With Strings.

def list_and_dict_operations():
    # List Operations
    fruits = ["apple", "banana", "cherry"]
    fruits.append("date")
    fruits.insert(1, "blueberry")
    fruits.remove("banana")
    fruits.sort()
    fruits_copy = fruits.copy()
    
    print("List after operations:", fruits)
    print("Copied list:", fruits_copy)
    
    # Dictionary Operations
    fruits_dict = {"apple": 1, "banana": 2, "cherry": 3}
    fruits_dict["date"] = 4
    fruits_dict["blueberry"] = 5
    del fruits_dict["banana"]
    
    print("Dictionary after operations:", fruits_dict)
    
    # Accessing Elements
    for key, value in fruits_dict.items():
        print(f"Fruit: {key}, Value: {value}")

# Calling Function
list_and_dict_operations()
