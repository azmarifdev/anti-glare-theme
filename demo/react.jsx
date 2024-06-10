import React, { useState, useEffect } from "react";
import "./App.css";
import BookList from "./components/BookList";
import AddBookForm from "./components/AddBookForm";
import fetchBooks from "./api/fetchBooks";

function App() {
  const [books, setBooks] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function loadBooks() {
      try {
        const fetchedBooks = await fetchBooks();
        setBooks(fetchedBooks);
        setLoading(false);
      } catch (error) {
        console.error("Error fetching books:", error);
        setLoading(false);
      }
    }
    loadBooks();
  }, []);

  const addBook = (title, author) => {
    setBooks([...books, { title, author }]);
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>My Book Library</h1>
      </header>
      {loading ? (
        <p>Loading books...</p>
      ) : (
        <div>
          <BookList books={books} />
          <AddBookForm addBook={addBook} />
        </div>
      )}
    </div>
  );
}

export default App;
