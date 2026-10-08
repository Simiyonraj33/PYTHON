import random

def display_menu():
    print("\nMenu:")
    print("1. Generate a Random Float between 0 and 1 (random())")
    print("2. Generate a Random Integer (randint())")
    print("3. Generate a Random Float (randfloat())")
    print("4. Generate a Random Float within a Range (uniform())")
    print("5. Generate a Random Integer from a Range (randrange())")
    print("6. Select a Random Item from a List (choice())")
    print("7. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            print(f"Random Float = {random.random()}")

        elif choice == '2':
            low = int(input("Enter the lower bound: "))
            high = int(input("Enter the upper bound: "))
            print(f"Random Integer = {random.randint(low, high)}")

        elif choice == '3':
            low = float(input("Enter the lower bound: "))
            high = float(input("Enter the upper bound: "))
            rand_float = random.uniform(low, high)
            print(f"Random Float = {rand_float}")

        elif choice == '4':
            low = float(input("Enter the lower bound: "))
            high = float(input("Enter the upper bound: "))
            print(f"Random Float (uniform) = {random.uniform(low, high)}")

        elif choice == '5':
            low = int(input("Enter the lower bound: "))
            high = int(input("Enter the upper bound: "))
            step = int(input("Enter the step size: "))
            print(f"Random Integer (randrange) = {random.randrange(low, high, step)}")

        elif choice == '6':
            items = input("Enter a list of items separated by commas: ").split(',')
            items = [item.strip() for item in items]  # Remove extra spaces
            print(f"Random Item = {random.choice(items)}")

        elif choice == '7':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
