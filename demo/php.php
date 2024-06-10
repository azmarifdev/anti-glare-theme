<?php
// Define a simple class to manage a collection of books
class Book {
    private $title;
    private $author;

    public function __construct($title, $author) {
        $this->title = $title;
        $this->author = $author;
    }

    public function getTitle() {
        return $this->title;
    }

    public function getAuthor() {
        return $this->author;
    }

    public function toArray() {
        return [
            'title' => $this->title,
            'author' => $this->author,
        ];
    }
}

// Class to manage a library of books
class Library {
    private $books = [];

    public function addBook(Book $book) {
        $this->books[] = $book;
    }

    public function listBooks() {
        foreach ($this->books as $book) {
            echo "Title: " . $book->getTitle() . ", Author: " . $book->getAuthor() . "\n";
        }
    }

    public function saveToFile($filename) {
        $data = [];
        foreach ($this->books as $book) {
            $data[] = $book->toArray();
        }
        file_put_contents($filename, json_encode($data));
    }

    public function loadFromFile($filename) {
        if (!file_exists($filename)) {
            throw new Exception("File not found: $filename");
        }

        $data = json_decode(file_get_contents($filename), true);
        foreach ($data as $bookData) {
            $this->addBook(new Book($bookData['title'], $bookData['author']));
        }
    }
}

// Create a new library and add some books
$library = new Library();
$library->addBook(new Book("1984", "George Orwell"));
$library->addBook(new Book("To Kill a Mockingbird", "Harper Lee"));
$library->addBook(new Book("The Great Gatsby", "F. Scott Fitzgerald"));

// List all books in the library
echo "Listing all books in the library:\n";
$library->listBooks();

// Save the library to a file
$filename = "library.json";
$library->saveToFile($filename);
echo "\nLibrary saved to $filename\n";

// Create a new library instance and load books from the file
$newLibrary = new Library();
try {
    $newLibrary->loadFromFile($filename);
    echo "\nBooks loaded from $filename:\n";
    $newLibrary->listBooks();
} catch (Exception $e) {
    echo "Error: " . $e->getMessage();
}

?>
