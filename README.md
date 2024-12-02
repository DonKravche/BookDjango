# Book Django Project

A web application for managing and organizing books built with Django. This project allows users to manage their book collection, including adding, updating, and tracking books.

## Features

- Book management system
- User authentication
- Book categorization
- Search functionality
- Responsive design

## Technologies Used

- Python 3.x
- Django 4.x
- HTML/CSS
- SQLite (default database)
- Bootstrap (optional)

## Prerequisites

Before you begin, ensure you have the following installed:
- Python (3.8 or higher)
- pip (Python package manager)
- Virtual environment (recommended)

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd BookDjangoProject
```

2. Create and activate virtual environment:
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Unix/MacOS
python3 -m venv .venv
source .venv/bin/activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Apply database migrations:
```bash
python manage.py migrate
```

5. Create a superuser (admin):
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

## Project Structure

```
BookDjangoProject/
├── manage.py
├── books/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
├── static/
│   ├── css/
│   └── js/
└── templates/
```

## Usage

1. Access the application at `http://localhost:8000`
2. Log in with your superuser credentials
3. Start managing your book collection

## Configuration

To configure the project:
1. Update `settings.py` with your specific settings
2. Set up your environment variables in `.env` file
3. Configure your database settings if needed

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

Your Name - your.email@example.com
Project Link: [https://github.com/yourusername/BookDjangoProject](https://github.com/yourusername/BookDjangoProject)

## Acknowledgments

- Django documentation
- Python community
- Your additional references

---
*Note: Remember to update this README with your specific project details, requirements, and instructions.*


## Updates

### Update 1 - Added Book Form and Filtering (13/11/2024)
Added new features to enhance book management functionality:

#### What's New:
1. Book Addition Form:
   - Created a new form for adding books to the system
   - Added validation for book details
   - Integrated category selection

2. Advanced Filtering System:
   - Implemented category-based filtering
   - Added title search functionality
   - Created a side-by-side layout for filters and book list
   - Book cards now display in a responsive grid layout

3. Visual Improvements:
   - Redesigned book display using Bootstrap cards
   - Added responsive grid system for book layout
   - Improved filter sidebar design

#### Technical Updates:
- Added new view logic for handling filters
- Implemented category grouping by type
- Enhanced template structure with separate filter components
- Added Bootstrap styling for better responsive design

### Update 2 - Added Pagination and Book Details
Enhanced user experience with new navigation and detailed book information features:

#### What's New:
1. Pagination System:
   - Implemented page-based navigation for the book list
   - Added clear page indicators
   - Improved performance for large book collections
2. Detailed Book Pages:
   - Created individual detail pages for each book
   - Comprehensive display of book information including:
     - Title and author
     - Language and ISBN
     - Page count
     - Publication date
     - Category
     - Price
   - Added navigation between book list and detail views
   - 
#### Technical Updates:
- Implemented Django pagination
- Created new book detail view and template
- Enhanced URL routing for book details
- Added detailed page styling and layout

### Update 3/4 - Added Pagination and Book Details
Enhanced user experience with new navigation and detailed book information features:

#### What's New:
1. -Implemented cart naviagtion for ordered book
2. -added to clear cart after order
3. -also added my previous order page (Not Working Very well but Will be Updated Soon)
4. -Added update book qunatity in cart, also delete method
5. Fixed Some bugs.
6. improved code quality.
