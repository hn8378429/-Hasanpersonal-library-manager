import json

# Load existing data from file
try:
    with open("my_library.json", "r") as file:
        book_collection = json.load(file)
except FileNotFoundError:
    book_collection = []

# Save library to file
def save_collection():
    with open("my_library.json", "w") as file:
        json.dump(book_collection, file, indent=4)

# Add a new book
def add_new_book():
    title = input("📖 Book title: ")
    author = input("✍️ Author's name: ")
    try:
        year = int(input("📅 Publication year: "))
    except ValueError:
        print("Invalid year. Please enter a number.")
        return
    genre = input("🏷️ Genre: ")
    read = input("📚 Have you read it? (yes/no): ").strip().lower() == "yes"

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }
    book_collection.append(book)
    print("✅ Book added!\n")

# Remove a book
def delete_book():
    title = input("Enter the exact title of the book to delete: ")
    for book in book_collection:
        if book["title"].lower() == title.lower():
            book_collection.remove(book)
            print("🗑️ Book deleted!\n")
            return
    print("⚠️ Book not found.\n")

# Search by title or author
def find_book():
    print("🔍 Search by:\n1. Title\n2. Author")
    choice = input("Your choice: ")
    term = input("Enter search keyword: ")
    results = []

    if choice == "1":
        results = [b for b in book_collection if term.lower() in b["title"].lower()]
    elif choice == "2":
        results = [b for b in book_collection if term.lower() in b["author"].lower()]

    if results:
        print(f"\n📚 Found {len(results)} matching book(s):")
        for i, b in enumerate(results, 1):
            status = "✅ Read" if b["read"] else "⏳ Unread"
            print(f"{i}. {b['title']} by {b['author']} ({b['year']}) - {b['genre']} - {status}")
    else:
        print("😕 No books matched your search.")
    print()

# Show all books
def list_books():
    if not book_collection:
        print("📂 Your library is empty.\n")
        return
    print("📚 Your Book Collection:")
    for i, b in enumerate(book_collection, 1):
        status = "✅ Read" if b["read"] else "⏳ Unread"
        print(f"{i}. {b['title']} by {b['author']} ({b['year']}) - {b['genre']} - {status}")
    print()

# Show library stats
def library_stats():
    total = len(book_collection)
    if total == 0:
        print("📝 No books in your collection.\n")
        return
    read_count = len([b for b in book_collection if b["read"]])
    print(f"📊 Total books: {total}")
    print(f"📖 Books read: {read_count}")
    print(f"📈 Reading completion: {(read_count / total) * 100:.1f}%\n")

# Filter books by genre
def filter_by_genre():
    genre = input("🎯 Enter genre to filter: ").strip().lower()
    filtered = [b for b in book_collection if genre in b["genre"].lower()]
    if filtered:
        print(f"\n🎨 Books in genre '{genre}':")
        for i, b in enumerate(filtered, 1):
            status = "✅ Read" if b["read"] else "⏳ Unread"
            print(f"{i}. {b['title']} by {b['author']} ({b['year']}) - {status}")
    else:
        print("⚠️ No books found for that genre.\n")

# Menu system
def main_menu():
    while True:
        print("📚 Welcome to My Unique Library Manager")
        print("1. ➕ Add a new book")
        print("2. ❌ Delete a book")
        print("3. 🔍 Search book")
        print("4. 📋 Show all books")
        print("5. 📊 Library stats")
        print("6. 🎯 Filter by genre")
        print("7. 💾 Exit & Save")
        choice = input("Choose an option: ")

        if choice == "1":
            add_new_book()
        elif choice == "2":
            delete_book()
        elif choice == "3":
            find_book()
        elif choice == "4":
            list_books()
        elif choice == "5":
            library_stats()
        elif choice == "6":
            filter_by_genre()
        elif choice == "7":
            save_collection()
            print("💾 Library saved. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.\n")

# Start program
if __name__ == "__main__":
    main_menu()
