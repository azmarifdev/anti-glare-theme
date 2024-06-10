import requests
import pandas as pd
import json

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def to_dict(self):
        return {'title': self.title, 'author': self.author}

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}")

    def save_to_file(self, filename):
        data = [book.to_dict() for book in self.books]
        with open(filename, 'w') as file:
            json.dump(data, file)

    def load_from_file(self, filename):
        if not os.path.exists(filename):
            raise FileNotFoundError(f"File not found: {filename}")
        with open(filename, 'r') as file:
            data = json.load(file)
            self.books = [Book(d['title'], d['author']) for d in data]

    def fetch_books(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            books_data = response.json()
            for book_data in books_data:
                self.add_book(Book(book_data['title'], book_data['author']))
        else:
            print(f"Failed to fetch books from {url}")

def main():
    # Create a new library instance
    library = Library()

    # Add books to the library
    library.add_book(Book("1984", "George Orwell"))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald"))

    # List all books in the library
    print("Listing all books in the library:")
    library.list_books()

    # Save the library to a file
    filename = 'library.json'
    library.save_to_file(filename)
    print(f"\nLibrary saved to {filename}")

    # Load books from the file into a new library instance
    new_library = Library()
    try:
        new_library.load_from_file(filename)
        print(f"\nBooks loaded from {filename}:")
        new_library.list_books()
    except FileNotFoundError as e:
        print(e)

    # Fetch additional books from an API
    api_url = 'https://api.example.com/books'
    library.fetch_books(api_url)

    # Display all books in the library as a DataFrame
    print("\nBooks in the library:")
    df = pd.DataFrame([book.to_dict() for book in library.books])
    print(df)

if __name__ == "__main__":
    main()
