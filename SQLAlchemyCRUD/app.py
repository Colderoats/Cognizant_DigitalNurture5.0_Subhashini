from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
engine = create_engine("sqlite:///students.db")
Base = declarative_base()
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    department = Column(String)
    marks = Column(Integer)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
print("Database and table created successfully!")

student1 = Student(
    name="Alice",
    department="CSE",
    marks=91
)

student2 = Student(
    name="Bob",
    department="IT",
    marks=85
)

student3 = Student(
    name="Charlie",
    department="ECE",
    marks=88
)

session.add(student1)
session.add(student2)
session.add(student3)

session.commit()

print("Records inserted successfully!")

students = session.query(Student).all()

print("\nStudent Records")

for student in students:
    print(student.id, student.name, student.department, student.marks)
    student = session.query(Student).filter_by(name="Bob").first()

student.marks = 95

session.commit()

print("\nRecord Updated")
students = session.query(Student).all()

for student in students:
    print(student.id, student.name, student.department, student.marks)
    student = session.query(Student).filter_by(name="Charlie").first()

session.delete(student)

session.commit()

print("\nRecord Deleted")
students = session.query(Student).all()

for student in students:
    print(student.id, student.name, student.department, student.marks)