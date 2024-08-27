#   Write a program that asks the user for a number in the range of 1 through 7. 
#   The program should display the corresponding day of the week, where 1 = Monday,
#   2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, & 7 = Sunday.
#   The program should display an error message if the user enters a number that is outside the range of 1 through 7.

# Code :-

def day_of_week():
    day = int(input("Enter a number (1-7): "))
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    if 1 <= day <= 7:
        print(days[day - 1])
    else:
        print("Error: Number out of range.")

day_of_week()
