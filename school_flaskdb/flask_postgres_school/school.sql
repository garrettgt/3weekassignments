-- databse schema

DROP TABLE IF EXISTS student;
CREATE TABLE student(
    id serial PRIMARY KEY,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    age INT,
    subject INT
);

CREATE TABLE subjects(
    id serial PRIMARY KEY,
    subject VARCHAR(50)
);

CREATE TABLE teachers(
    id serial PRIMARY KEY,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    age INT,
    subject INT
);