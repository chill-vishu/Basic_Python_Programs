# The area of a rectangle is the rectangle’s length times its width.
# Write a program that asksfor the length and width of two rectangles.
# The program should tell the user which rectanglehas the greater area, or if the areas are the same.

def area_of_rectangles():
    # Input dimensions of both rectangles
    length1 = float(input("Enter the length of the first rectangle: "))
    width1 = float(input("Enter the width of the first rectangle: "))
    length2 = float(input("Enter the length of the second rectangle: "))
    width2 = float(input("Enter the width of the second rectangle: "))
    
    # Calculating Areas
    area1 = length1 * width1
    area2 = length2 * width2
    
    # Comparing Areas & Printing Result
    if area1 > area2:
        print("The first rectangle has a greater area.")
    elif area2 > area1:
        print("The second rectangle has a greater area.")
    else:
        print("Both rectangles have the same area.")

# Calling Function
area_of_rectangles()