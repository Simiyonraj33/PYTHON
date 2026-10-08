class Item:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.publication_year}"

# Derived class for Books
class Book(Item):
    def __init__(self, title, author, publication_year, isbn):
        super().__init__(title, author, publication_year)
        self.isbn = isbn

    def display_info(self):
        return f"{super().display_info()}, ISBN: {self.isbn}"

# Derived class for Magazines
class Magazine(Item):
    def __init__(self, title, author, publication_year, issue_number):
        super().__init__(title, author, publication_year)
        self.issue_number = issue_number

    def display_info(self):
        return f"{super().display_info()}, Issue Number: {self.issue_number}"

# Function to get user input for a book
def create_book():
    title = input("Enter the book title: ")
    author = input("Enter the author's name: ")
    publication_year = input("Enter the publication year: ")
    isbn = input("Enter the ISBN: ")
    return Book(title, author, publication_year, isbn)

# Function to get user input for a magazine
def create_magazine():
    title = input("Enter the magazine title: ")
    author = input("Enter the author's name: ")
    publication_year = input("Enter the publication year: ")
    issue_number = input("Enter the issue number: ")
    return Magazine(title, author, publication_year, issue_number)

# Main function to run the library system
if __name__ == "__main__":
    items = []

    while True:
        print("\nLibrary System")
        print("1. Add a Book")
        print("2. Add a Magazine")
        print("3. Display All Items")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            book = create_book()
            items.append(book)
            print("Book added successfully!")
        elif choice == '2':
            magazine = create_magazine()
            items.append(magazine)
            print("Magazine added successfully!")
        elif choice == '3':
            print("\nLibrary Items:")
            for item in items:
                print(item.display_info())
        elif choice == '4':
            print("Exiting the library system.")
            break
        else:
            print("Invalid choice. Please try again.")
