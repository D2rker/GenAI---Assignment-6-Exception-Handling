prices = [120, 350, 'abc', 500, -200, 800]
total = 0

for price in prices:
    try:
        if isinstance(price, (int, float)) and price < 0:
            raise ValueError("Negative price not allowed")

        total += price

    except TypeError:
        print(f"Skipping invalid item '{price}': Not a number.")

    except ValueError as e:
        print(f"Skipping invalid item '{price}': {e}.")

print(f"Final Total: {total}")