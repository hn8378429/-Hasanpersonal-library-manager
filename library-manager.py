import json

# Load existing library data from file
try:
    with open("library.txt", "r") as file:
        library = json.load(file)
except FileNotFoundError:
    library = []

# Save library to file
def save_library():
    with open("library.txt", "w") as file:
        json.dump(library, file, indent=4)

# Add a book
def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ")
    read = input("Have you read this book? (yes/no): ").strip().lower() == "yes"
    
    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }
    library.append(book)
    save_library()
    print("✅ Book added successfully!\n")

# Remove a book
def remove_book():
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            save_library()
            print("✅ Book removed successfully!\n")
            return
    print("❌ Book not found.\n")

# Search for a book
def search_book():
    print("Search by:\n1. Title\n2. Author")
    choice = input("Enter your choice (1 or 2): ")
    query = input("Enter the search term: ")
    results = []

    if choice == "1":
        results = [book for book in library if query.lower() in book["title"].lower()]
    elif choice == "2":
        results = [book for book in library if query.lower() in book["author"].lower()]
    else:
        print("❌ Invalid choice.")
        return

    if results:
        print("\n📚 Search Results:")
        for book in results:
            print_book(book)
    else:
        print("❌ No matching books found.\n")

# List all books
def list_books():
    if not library:
        print("📭 No books in the library.\n")
        return
    print("\n📚 Library Books:")
    for book in library:
        print_book(book)

# Helper: Print book nicely
def print_book(book):
    print(f"Title: {book['title']}")
    print(f"Author: {book['author']}")
    print(f"Year: {book['year']}")
    print(f"Genre: {book['genre']}")
    print(f"Read: {'Yes' if book['read'] else 'No'}")
    print("-" * 30)

# Main menu loop
def main():
    while True:
        print("\n📘 Library Menu:")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. List all books")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            search_book()
        elif choice == "4":
            list_books()
        elif choice == "5":
            print("👋 Exiting the library. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.\n")

# Start the program
if __name__ == "__main__":
    main()
