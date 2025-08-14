# A simple program to calculate age in dog years with validation
def get_valid_age():
    while True:
        try:
            age = int(input("How old are you? "))
            if age < 0:
                print("Age cannot be negative. Please try again.")
                continue
            return age
        except ValueError:
            print("Please enter a valid number.")

name = input("What is your name? ")
age = get_valid_age()

# Calculate dog years (1 human year = 7 dog years)
dog_years = age * 7

# Print the results
print(f"Hi {name}!")
print(f"You are {age} years old in human years.")
print(f"In dog years, you would be {dog_years} years old!")
