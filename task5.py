cart = []

print("Enter item prices. Type 'q' to finish and see your bill.")

while True:
    user_input = input("Enter price: ").lower()

    if user_input == 'q':
        break

    try:
        # Convert input to a float
        price = float(user_input)

        if price < 0:
            raise ValueError("Price cannot be negative.")

        cart.append(price)

    except ValueError as e:
        if "could not convert string to float" in str(e):
            print("Invalid input: Please enter a numeric price or 'q' to quit.")
        else:
            print(f"Invalid input: {e}")

print("\nFinal Receipt")
print(f"Total items: {len(cart)}")
print(f"Total bill:  ${sum(cart):.2f}")