-- Tabela przechowuje dane o uczniach
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    sex TEXT NOT NULL
);


-- Dodanie przykladowych danych do tabeli students
INSERT INTO students (first_name, last_name, sex) 
VALUES 
('John', 'Smith', 'M'), 
('Anna', 'Brown', 'F'), 
('Peter', 'Johnson', 'M'), 
('Mary', 'Williams', 'F'),
('John', 'Doe', 'M'), 
('Kristen', 'Bell', 'F' ); 


-- wybierz wszystkich studentow
select * from students;


-- wybierz wszystkie studentki
select * from students WHERE student.sex = 'F';


-- koniec pliku