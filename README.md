
---

# Library Management System (CLI & ORM-Based)

This is a **CLI-based Library Management System** built using Python, SQLAlchemy ORM, and SQLite. It allows users to register as members, search for books, borrow and return them, while librarians can add new books and track borrowing records efficiently.  

The project follows best practices, including structured package organization, virtual environment management with Pipenv, and usage of lists, dictionaries, and tuples for data handling.

---

## Features

- **User Registration** – Members can register and borrow books.  
- **Book Search** – Users can search for books by title or author.  
- **Borrow & Return Books** – Members can borrow available books and return them when done.  
- **Librarian Functions** – Add new books, track borrowed books, and manage inventory.  
- **Persistent Storage** – Data is stored in an SQLite database using SQLAlchemy ORM.  
- **Interactive CLI** – The system is accessed via command-line commands using `Click`.  

---

## Project Structure  

```
library_management_system/
│── migrations/          # Alembic migration scripts
│── models.py            # Database models using SQLAlchemy
│── cli.py               # Main CLI script for user interaction
│── database.py          # Database connection setup
│── Pipfile              # Pipenv dependency management
│── Pipfile.lock         # Locked dependencies
│── README.md            # Documentation
│── .gitignore           # Ignoring unnecessary files
└── config.py            # Configuration settings
```

---

## Installation & Setup  

### Clone the Repository  

```sh
git clone https://github.com/yourusername/library_management_system.git
cd library_management_system
```

### Set Up a Virtual Environment  

Ensure you have **Python 3.12** installed. Then, create and activate the virtual environment:

```sh
pipenv shell
```

### Install Dependencies  

```sh
pipenv install
```

This installs required packages like `SQLAlchemy`, `Alembic`, `Click`, and `sqlite3`.

---

## Database Setup  

### Initialize Alembic for Migrations  

Run this command to initialize Alembic:

```sh
alembic init migrations
```

### Generate the First Migration  

```sh
alembic revision --autogenerate -m "Initial migration"
```

### Apply Migrations to Create the Database  

```sh
alembic upgrade head
```

This creates the **SQLite database (`library.db`)** and applies the migrations.

---

## Running the Application  

### Start the CLI  

Run the following command:

```sh
python cli.py
```

### Available CLI Commands  

#### Register a New Member  

```sh
python cli.py register-member --name "John Doe"
```

#### Search for a Book  

```sh
python cli.py search-book --title "The Great Gatsby"
```

#### Borrow a Book  

```sh
python cli.py borrow-book --member-id 1 --book-id 2
```

#### Return a Book  

```sh
python cli.py return-book --member-id 1 --book-id 2
```

#### Add a New Book (Librarian)  

```sh
python cli.py add-book --title "New Book" --author "Jane Doe"
```

---

## Technologies Used  

- **Python 3.12** – Programming language  
- **SQLAlchemy** – Object-Relational Mapping (ORM)  
- **SQLite** – Lightweight database  
- **Alembic** – Database migrations  
- **Click** – Building CLI commands  
- **Pipenv** – Virtual environment and dependency management  

---

## Contributing  

Feel free to fork this repository and submit pull requests for improvements! 🚀  

---

## License  

This project is open-source and available under the **MIT License**.

---
