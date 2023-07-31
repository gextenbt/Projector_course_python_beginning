from sqlalchemy import (Column, 
                        Integer, 
                        String, 
                        ForeignKey, 
                        create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.exc import ProgrammingError

'''
Create connection url
'''
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

'''
Create tables objects
'''
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

"""
Insert data
"""

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
