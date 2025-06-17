# README.md

# Exam Bank Management System

This project is an Exam Bank Management System designed to facilitate the management of exams, questions, and user roles within an educational institution. The system allows for the creation, updating, and deletion of exams and questions, as well as user management and statistical analysis of exam performance.

## Features

- User authentication and authorization
- Management of departments and subjects
- Creation and management of exams
- Addition and management of questions
- Assignment of tasks to users
- Generation of statistics related to exams and questions
- Exporting exam data to PDF and Word formats

## Project Structure

```
exam-bank-management-backend
├── app
│   ├── __init__.py
│   ├── models.py
│   ├── routes
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── user.py
│   │   ├── department.py
│   │   ├── subject.py
│   │   ├── exam.py
│   │   ├── question.py
│   │   ├── assignment.py
│   │   └── statistics.py
│   ├── services
│   │   ├── __init__.py
│   │   ├── auth_service.py
│   │   ├── user_service.py
│   │   ├── exam_service.py
│   │   ├── question_service.py
│   │   └── statistics_service.py
│   └── utils
│       ├── __init__.py
│       ├── pdf_export.py
│       └── word_export.py
├── migrations
│   └── README.md
├── tests
│   ├── __init__.py
│   ├── test_auth.py
│   ├── test_exam.py
│   └── test_question.py
├── requirements.txt
├── config.py
├── run.py
├── README.md
└── database
    ├── schema.sql
    └── seed.sql
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd exam-bank-management-backend
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

5. Set up the database:
   - Run the SQL commands in `database/schema.sql` to create the necessary tables.
   - Optionally, run `database/seed.sql` to populate the database with initial data.

## Usage

To run the application, execute the following command:
```
python run.py
```

The application will be accessible at `http://127.0.0.1:5000`.

## Testing

To run the tests, use the following command:
```
pytest
```

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.