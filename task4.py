filename = input("Enter the name of the file you want to read: ")

try:
    with open(filename, 'r') as file:

        print(f"--- Contents of {filename} ---")
        for i in range(3):
            line = file.readline()
            if not line:
                break
            print(line.strip())

except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")

except PermissionError:
    print(f"Error: You do not have permission to read '{filename}'.")

finally:
    print("File operation attempted.")