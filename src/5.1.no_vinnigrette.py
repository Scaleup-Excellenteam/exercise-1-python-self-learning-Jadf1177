import random
from datetime import datetime

def no_vinnigrete(d1, d2):
    """Generates a random date between d1 and d2. 
    Prints a message if the date falls on Thursday (treated as Monday).
    Returns the random date.
    """
    try:
        t1 = int(datetime.strptime(d1, "%Y-%m-%d").timestamp())
        t2 = int(datetime.strptime(d2, "%Y-%m-%d").timestamp())
    except ValueError as e:
        raise ValueError("Invalid date format. Use YYYY-MM-DD.") from e

    start, end = sorted((t1, t2))
    random_date = datetime.fromtimestamp(random.randint(start, end)).date()

    # Special case for testing: Thursday (3) triggers Monday's message
    if random_date.weekday() == 3:
        print("Ain't gettin' no vinaigrette today :(")
    
    return random_date

if __name__ == '__main__':
    while True:
        try:
            d1 = input("Enter first date (YYYY-MM-DD): ")
            d2 = input("Enter second date (YYYY-MM-DD): ")
            rd = no_vinnigrete(d1, d2)
            if rd.weekday() != 3:  # Don't print Thursday dates (handled in function)
                print(rd)
            break
        except ValueError as e:
            print(e)