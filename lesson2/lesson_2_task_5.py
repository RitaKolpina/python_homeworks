month = int(input("Enter a number of a month (in range from 1 to 12): "))

def month_to_season(month):
        if month in [12, 1, 2]:
            print(f"Month number {month} is WINTER season")
        elif month in [3, 4, 5]:
            print(f"Month number {month} is SPRING season")
        elif month in [6, 7, 8]:
             print(f"Month number {month} is SUMMER season")
        elif month in [9, 10, 11]:
             print(f"Month number {month} is AUTUMN season")
        else:
             print("You entered a wrong number. Please try again.")
             month = int(input("Enter a number of a month (in range from 1 to 12): "))
        
month_to_season(month)