# Advanced API Project

This project is a Django REST Framework (DRF)-based API for managing a collection of books. It includes robust features for performing CRUD operations, applying permissions, and customizing behavior.

---

## **Features**
- **List Books**: Retrieve a list of all books.
- **Retrieve Book Details**: Fetch details of a specific book by ID.
- **Create Book**: Add a new book to the collection (requires authentication).
- **Update Book**: Modify details of an existing book (requires authentication).
- **Delete Book**: Remove a book from the collection (requires authentication).
- **Permission Enforcement**: Protect endpoints based on user roles.

---

## **Endpoints**

### **Books**
| HTTP Method | Endpoint               | Description                                | Authentication |
|-------------|------------------------|--------------------------------------------|----------------|
| **GET**     | `/api/books/`          | Retrieve a list of all books               | ❌ No           |
| **GET**     | `/api/books/<id>/`     | Retrieve details of a specific book        | ❌ No           |
| **POST**    | `/api/books/create/`   | Add a new book to the collection           | ✅ Yes          |
| **PUT**     | `/api/books/<id>/update/` | Update details of an existing book        | ✅ Yes          |
| **DELETE**  | `/api/books/<id>/delete/` | Delete a book from the collection         | ✅ Yes          |

---

## **Permissions**
- **Unauthenticated Users**: Read-only access to view books (`GET` requests).
- **Authenticated Users**: Full access to create, update, and delete books.

---

## **Setup Instructions**
### **1. Clone the Repository**
Clone the project from the GitHub repository:
```bash
git clone <repository-url>
cd advanced-api-project
## Advanced Query Features

### Filtering
- **Filter by title**: `/api/books/?title=Harry`
- **Filter by author**: `/api/books/?author__name=Rowling`
- **Filter by publication year**: `/api/books/?publication_year=1997`

### Searching
- **Search in title and author name**: `/api/books/?search=Harry`

### Ordering
- **Order by title**: `/api/books/?ordering=title`
- **Order by publication year (descending)**: `/api/books/?ordering=-publication_year`
