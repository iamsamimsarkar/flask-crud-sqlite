# Flask CRUD Application with SQLite  

This is a simple **Flask CRUD (Create, Read, Update, Delete) application** that uses **SQLite3** as the database. It allows users to add, edit, delete, and view user records.  

## Features  
- Add new users  
- View all users  
- Edit user details  
- Delete users  
- Uses **Flask-SQLAlchemy** for database management  
- **Custom CSS** for a modern UI  

## Technologies Used  
- Python (Flask)  
- SQLite3  
- Flask-SQLAlchemy  
- HTML, CSS (Custom), JavaScript  

## Installation & Setup  

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/iamsamimsarkar/flask-crud-sqlite.git
   cd flask-crud-sqlite
   ```

2. **Create a Virtual Environment (Optional but Recommended)**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**  
   ```bash
   python app.py
   ```

5. **Open in Browser**  
   Open `http://127.0.0.1:5000/` in your browser.  

## Project Structure  
```
flask-crud-sqlite/
│── static/
│   ├── styles.css  # Custom CSS file
│── templates/
│   ├── index.html
│   ├── add_user.html
│   ├── edit_user.html
│── app.py
│── database.db
│── requirements.txt
│── README.md
```

## Custom Styling  
- All styles are written in `static/styles.css`.  
- If you want to modify the UI, edit this file.  

## API Endpoints  
| Route          | Method | Description |
|---------------|--------|-------------|
| `/`           | GET    | View all users |
| `/add`        | GET/POST | Add a new user |
| `/edit/<id>`  | GET/POST | Edit user details |
| `/delete/<id>` | GET    | Delete a user |

## License  
This project is open-source and available under the **MIT License**.
