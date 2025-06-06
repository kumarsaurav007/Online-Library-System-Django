# Library Management System (Django)

### Features:

- Add authors, books, and borrow records  
- View lists of authors, books, and borrow records with pagination  
- Export all data to Excel file  
- Simple and clean UI  
- Used class-based views  

---

### How to Run This Project:

- Step 1: Go inside the project folder  
- Step 2: Create virtual environment  
  
  python -m venv venv
  
- Step 3: Activate the environment  
  - On Windows:
    
    venv\Scripts\activate
    
    
- Step 4: Install required packages  
  
  pip install -r requirements.txt
  
- Step 5: Run migrations  
  
  python manage.py makemigrations
  python manage.py migrate
  
  
- Step 6: Start the server  
  
  python manage.py runserver
  

### Web Pages:

- Homepage: /  
- View Authors: /authors/  
- Add Author: /authors/add/  
- View Books: /books/  
- Add Book: /books/add/  
- View Borrow Records: /borrow/  
- Add Borrow Record: /borrow/add/  
- Export to Excel: /export/