
- Links:
	- Databases:
		- [[Database management systems (DBMS)]]
		- [[Databases. Introduction]]
	- SQL
		- [[SQL. Introduction]]
			- [[SQL constraints]] - *
			- [[SQL commands]]
	- Graphs:
		- [[Mermaid. Graphs. Introduction]]
	- Virtual:
		- [[Lecture 9. Venv. Projector]]

- Sources:
	- Mermaid editor: 
		- https://mermaid.live/edit
	- PostgreSQL
		- [PostgreSQL: Documentation: 8.1: Constraints](https://www.postgresql.org/docs/8.1/ddl-constraints.html)
	- Stack Overflow:
		- [sql - Postgresql foreign key -- no unique constraint](https://stackoverflow.com/questions/20120239/postgresql-foreign-key-no-unique-constraint)
		- [Postgres - foreign key on not unique column](https://stackoverflow.com/questions/69673728/postgres-foreign-key-on-not-unique-column)



# DB in Python

```python
'''
1. Add models for student, subject and student_subject from previous lessons in SQLAlchemy.
2. Find all students` name that visited 'English' classes.
3. (Optional): Rewrite queries from the previous lesson using SQLAlchemy.
'''
```

# Set environment
```shell
pip install SQLAlchemy
```

```python
# Import
from sqlalchemy import (Column, 
                        Integer, 
                        String, 
                        ForeignKey, 
                        create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.exc import ProgrammingError


# Create connection url
DATABASE_URI = 'postgresql://{user}:{password}@{host}:{port}/{database}'

engine = create_engine(
    DATABASE_URI.format(
        host='localhost',
        database='db_prjctr_assignment_17',
        user='user',
        password='password',
        port=5432,
    )
)
```


# Create tables

```python
Base = declarative_base()


class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)

    # Define a one-to-many relationship with student_subject
    subjects = relationship("StudentSubject", back_populates="student")


class Subject(Base):
    __tablename__ = 'subject'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    # Define a one-to-many relationship with student_subject
    students = relationship("StudentSubject", back_populates="subject")


class StudentSubject(Base):
    __tablename__ = 'student_subject'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('student.id'), nullable=False)
    subject_id = Column(Integer, ForeignKey('subject.id'), nullable=False)

    # Define many-to-one relationships with student and subject
    student = relationship("Student", back_populates="subjects")
    subject = relationship("Subject", back_populates="students")

# Create the tables in the database if they don't exist
try:
    Base.metadata.create_all(engine)
except ProgrammingError:
    pass
```


## SQL
```sql
CREATE TABLE student (
    id serial PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INT NOT NULL
);

CREATE TABLE subject (
    id serial PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE student_subject (
    id serial PRIMARY KEY,
    student_id INT NOT NULL,
    subject_id INT NOT NULL,

    FOREIGN KEY (student_id)
        REFERENCES student (id),
    FOREIGN KEY (subject_id)
        REFERENCES subject (id)
);
```

# Insert into

```python
# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Check if data is already inserted
if not session.query(Student).first():  # TRUE, If there is no data
    # Insert data into student table
    students_data = [
        {'name': 'Bae', 'age': 18},
        {'name': 'Eddy', 'age': 21},
        {'name': 'Lily', 'age': 22},
        {'name': 'Jenny', 'age': 19}
    ]

    for data in students_data:
        student = Student(**data)
        session.add(student)

    # Insert data into subject table
    subjects_data = [
        {'name': 'English'},
        {'name': 'Math'},
        {'name': 'Spanish'},
        {'name': 'Ukrainian'}
    ]

    for data in subjects_data:
        subject = Subject(**data)
        session.add(subject)

    # Insert data into student_subject table
    student_subject_data = [
        {'student_id': 1, 'subject_id': 1},
        {'student_id': 2, 'subject_id': 2},
        {'student_id': 3, 'subject_id': 3},
        {'student_id': 4, 'subject_id': 4},
        {'student_id': 1, 'subject_id': 3}
    ]

    for data in student_subject_data:
        student_subject = StudentSubject(**data)
        session.add(student_subject)

    # Commit the changes
    session.commit()

# Close the session
session.close()

```

## SQL

```sql
INSERT INTO student (name, age) VALUES ('Bae', 18), ('Eddy', 21), ('Lily', 22), ('Jenny', 19);

INSERT INTO subject (name) VALUES ('English'), ('Math'), ('Spanish'), ('Ukrainian');

INSERT INTO student_subject (student_id, subject_id) VALUES (1, 1), (2, 2), (3, 3), (4, 4), (1, 3);
```

# Truncate

## SQL

```sql
TRUNCATE TABLE student CASCADE;

TRUNCATE TABLE subject CASCADE;

TRUNCATE TABLE student_subject CASCADE;
```


# Analytical queries

```python
# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Find all students' name that visited 'English' classes
english_subject = session.query(Subject).filter_by(name='English').first()

students_attended_english = (
    session.query(Student.name)
    .join(StudentSubject, StudentSubject.student_id == Student.id)
    .filter(StudentSubject.subject_id == english_subject.id)
    .all()
)

# Extract student names from the result
student_names_attended_english = [student[0]
                                  for student in students_attended_english]

print("Students who visited 'English' classes:")
print(student_names_attended_english)

# Close the session
session.close()
```