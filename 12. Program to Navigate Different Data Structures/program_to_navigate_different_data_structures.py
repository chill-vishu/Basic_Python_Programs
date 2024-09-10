# Create A Program To Navigate In Different Data Structures.

def navigate_data_structures():
    # List
    fruits = ["apple", "banana", "cherry"]
    print("List:", fruits)
    print("First element in list:", fruits[0])

    # Tuple
    fruits_tuple = ("apple", "banana", "cherry")
    print("Tuple:", fruits_tuple)
    print("First element in tuple:", fruits_tuple[0])

    # Dictionary
    fruits_dict = {"apple": 1, "banana": 2, "cherry": 3}
    print("Dictionary:", fruits_dict)
    print("Value for key 'apple':", fruits_dict["apple"])

    # Set
    fruits_set = {"apple", "banana", "cherry"}
    print("Set:", fruits_set)
    print("Is 'apple' in set?", "apple" in fruits_set)

# Calling Function
navigate_data_structures()
