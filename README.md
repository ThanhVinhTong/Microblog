# Microblog

A microblogging application built with Flask and SQLAlchemy.

## Database Structure

### Models

#### User
- `id`: Primary key
- `username`: Unique username (64 chars max)
- `email`: Unique email address (120 chars max)
- `password_hash`: Hashed password (256 chars)
- `posts`: Relationship to user's posts

#### Post
- `id`: Primary key
- `body`: Post content (140 chars max)
- `timestamp`: UTC timestamp of post creation
- `user_id`: Foreign key to User
- `author`: Relationship to post author

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Initialize the database:
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

## Dependencies

- Flask
- SQLAlchemy
- Flask-SQLAlchemy
- Flask-Migrate
- Python 3.x

## Development

The project uses SQLAlchemy with type hints for better code completion and type safety.

To create new database migrations:
```bash
flask db migrate -m "Description of changes"
flask db upgrade
```

## Project Structure
```
Microblog/
├── app/
│   ├── __init__.py
│   ├── models.py    # Database models
│   └── routes.py
├── migrations/      # Database migrations
├── config.py       # Configuration
└── requirements.txt
```