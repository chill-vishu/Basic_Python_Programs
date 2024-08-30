# Program demonstrates create list, append, insert, remove, sort, copy, how to get the index of an item in a list and then replace that item with a new item.


def list_operations():
    # Create a list
    fruits = ["apple", "banana", "cherry"]
    print("Initial list:", fruits)
    
    # Append item to the list
    fruits.append("date")
    print("After appending 'date':", fruits)
    
    # Insert item at a specific position
    fruits.insert(1, "blueberry")
    print("After inserting 'blueberry' at index 1:", fruits)
    
    # Remove item from the list
    fruits.remove("banana")
    print("After removing 'banana':", fruits)
    
    # Sort list
    fruits.sort()
    print("After sorting:", fruits)
    
    # Copy list
    fruits_copy = fruits.copy()
    print("Copied list:", fruits_copy)
    
    # Get index of an item
    index_of_cherry = fruits.index("cherry")
    print("Index of 'cherry':", index_of_cherry)
    
    # Replace item at a specific index with a new item
    fruits[index_of_cherry] = "cranberry"
    print("After replacing 'cherry' with 'cranberry':", fruits)

# Calling Function
list_operations()
