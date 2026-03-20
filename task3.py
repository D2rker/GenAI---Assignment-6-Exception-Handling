def check_age(age):
    if age < 1 or age > 120:
        raise ValueError("Age must be between 1 and 120")
    return age


try:
    user_input = input("Please enter your age: ")

    age_to_check = int(user_input)

    check_age(age_to_check)

    print(f"Age {age_to_check} is valid and has been recorded.")

except ValueError as e:
    print(f"Invalid input: {e}")