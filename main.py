

def Setbudget():
    budget = input("Please enter your desired budget: ")
    location = input("Enter the location you are interested in (city, state): ")
    confirm = input(f"You entered a budget of ${budget} and location of {location}. Is this correct? (yes/no): ")
    if confirm.lower() == 'yes':
        print(f"Budget is set to {budget}\nLocation is set to {location}")
    elif confirm.lower() == 'no':
        print("Try again later")
    else:
        print("Invalid input")
    return budget, location
        


Setbudget()
    



















