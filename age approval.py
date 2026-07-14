age = int(input("Enter your age: "))

if age < 0:
    print("Age cannot be negative.")
elif age > 100:
    print("Age entered is unrealistic. Please enter a valid age.")
elif age >= 18:
    print("You are approved for driving.")
else:
    print("You are not approved for driving.")

