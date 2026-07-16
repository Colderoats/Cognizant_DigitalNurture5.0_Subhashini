CREATE DATABASE company;

\c company

CREATE TABLE department(
    dept_id SERIAL PRIMARY KEY,
    dept_name VARCHAR(50)
);

CREATE TABLE employee(
    emp_id SERIAL PRIMARY KEY,
    emp_name VARCHAR(50),
    salary INT,
    dept_id INT REFERENCES department(dept_id)
);

INSERT INTO department(dept_name)
VALUES
('HR'),
('IT'),
('Finance');

INSERT INTO employee(emp_name,salary,dept_id)
VALUES
('Arya',50000,1),
('Balu',70000,2),
('Chandra',65000,2),
('David',60000,3);

SELECT e.emp_name,d.dept_name
FROM employee e
JOIN department d
ON e.dept_id=d.dept_id;