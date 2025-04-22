# Microblog

A Flask-based microblogging platform

## Features
- User authentication
- Blog posting
- User profiles

## Setup
1. Clone the repository
2. Create virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the application:
   ```
   flask run
   ```

## Project Structure
```
microblog/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── forms.py
│   └── templates/
├── venv/
└── config.py
```