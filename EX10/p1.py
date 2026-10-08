import os
FILE_NAME = "book-data.txt"
def write_file():
    with open(FILE_NAME, "w") as f:
        f.write("Book ID,Title, Author, price\n")
        f.write("101,Python,Vijay,250\n")
        f.write("102,Java,Ajay,300\n")
    print("Books written successfully to file.")
def read_file():
    if not os.path.isfile(FILE_NAME):
        print("File does not exist.")
        return
    with open(FILE_NAME, "r") as f:
        print("Current file position:", f.tell())
        print("Reading file...")
        data = f.read()
        print(data)
        print("Current file position:", f.tell())
def test_file():
    if not os.path.isfile(FILE_NAME):
        print("File does not exist.")
        return
    with open(FILE_NAME, "r") as f:
        print("seek()")
        f.seek(0)
        print("First line:", f.readline().strip())
        f.seek(10)
        print("From 10th position:", f.readline().strip())
def check_file():
    if os.path.isfile(FILE_NAME):
        print("File exists.")
    else:
        print("File does not exist.")
def main():
    while True:
        print("1. Write to file")
        print("2. Read from file")
        print("3. Test file")
        print("4. Check file")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            write_file()
        elif choice == '2':
            read_file()
        elif choice == '3':
            test_file()
        elif choice == '4':
            check_file()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")
main()
