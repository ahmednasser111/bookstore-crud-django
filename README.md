# Bookstore

A simple Django web app for managing a book collection. You can list, view, create, edit, and delete books through a clean browser interface.

## Features

- View all books on the home page
- Add new books with title, author, and price
- View book details
- Edit existing books
- Delete books

## Tech Stack

- Python 3
- Django 5.2
- SQLite (default database)

## Project Structure

```
day-3/
├── bookstore/                  # Django project root
│   ├── manage.py
│   ├── bookstore/              # Project settings
│   └── books/                  # Books app
│       ├── models.py           # Book model
│       ├── views.py              # CRUD views
│       ├── urls.py               # App routes
│       └── templates/books/      # HTML templates
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.10 or newer
- pip

### Installation

1. Clone the repository and go to the project folder:

   ```bash
   cd bookstore
   ```

2. Create and activate a virtual environment (recommended):

   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # macOS / Linux
   source venv/bin/activate
   ```

3. Install Django:

   ```bash
   pip install django
   ```

4. Run migrations:

   ```bash
   python manage.py migrate
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

6. Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Routes

| URL | Description |
|-----|-------------|
| `/` | List all books |
| `/create/` | Add a new book |
| `/show/<id>/` | View a single book |
| `/edit/<id>/` | Edit a book |
| `/delete/<id>/` | Delete a book |

## Book Model

| Field | Type |
|-------|------|
| `title` | CharField (max 200) |
| `author` | CharField (max 100) |
| `price` | DecimalField |

## License

This project is for educational purposes (ITI Open Source Development).
