import math

def display_menu():
    print("\nMenu:")
    print("1. Calculate Square Root")
    print("2. Calculate Floor")
    print("3. Calculate Ceiling")
    print("4. Calculate Exponential")
    print("5. Calculate Logarithm")
    print("6. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            num = float(input("Enter a number: "))
            print(f"Square Root = {math.sqrt(num)}")

        elif choice == '2':
            num = float(input("Enter a number: "))
            print(f"Floor = {math.floor(num)}")

        elif choice == '3':
            num = float(input("Enter a number: "))
            print(f"Ceiling = {math.ceil(num)}")

        elif choice == '4':
            num = float(input("Enter a number: "))
            print(f"Exponential = {math.exp(num)}")

        elif choice == '5':
            num = float(input("Enter a positive number: "))
            if num <= 0:
                print("Logarithm is not defined for non-positive numbers.")
            else:
                print(f"Log(x) = {math.log(num)}")

        elif choice == '6':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
