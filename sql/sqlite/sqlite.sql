-- Tabela przechowuje dane o klasach
CREATE TABLE classes (
    id INTEGER PRIMARY KEY, -- SQLite automatycznie ustawia AUTO_INCREMENT
    name TEXT NOT NULL
);

-- Tabela przechowuje dane o uczniach, z relacja do tabeli classes
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    class_id INTEGER,
    FOREIGN KEY (class_id) REFERENCES classes(id) ON DELETE CASCADE
);

-- Tabela przechowuje  wartości ocen
CREATE TABLE grades_dictionary (
    id INTEGER PRIMARY KEY,
    grade_value REAL NOT NULL UNIQUE,
    description TEXT DEFAULT NULL
);

-- Tabela wiąze uczniow z ocenami z tabeli słownikowej
CREATE TABLE student_grades (
    id INTEGER PRIMARY KEY,
    student_id INTEGER NOT NULL,
    grade_id INTEGER NOT NULL,
    grade_date TEXT NOT NULL, -- SQLite przechowuje daty jako tekst w formacie 'YYYY-MM-DD'
    FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
    FOREIGN KEY (grade_id) REFERENCES grades_dictionary(id) ON DELETE CASCADE
);

-- Dodanie przykładowych danych do tabeli classes
INSERT INTO classes (name) VALUES 
('7a'), 
('5b');

-- Dodanie przykladowych danych do tabeli students
INSERT INTO students (first_name, last_name, class_id) 
VALUES 
('John', 'Smith', 1), 
('Anna', 'Brown', 1), 
('Peter', 'Johnson', 2), 
('Mary', 'Williams', 2),
('John', 'Doe', NULL),  -- brak klasy
('Kristen', 'Bell', 2); -- brak ocen 

-- Dodanie przykladowych danych do tabeli grades_dictionary
INSERT INTO grades_dictionary (grade_value, description) 
VALUES 
(1.0, 'Very Poor'),
(1.5, 'Poor'),
(2.0, 'Unsatisfactory'),
(2.5, 'Almost Satisfactory'),
(3.0, 'Satisfactory'),
(3.5, 'Good'),
(4.0, 'Very Good'),
(4.5, 'Almost Excellent'),
(5.0, 'Excellent'),
(6.0, 'Outstanding');

-- Dodanie przykladowych danych do tabeli student_grades
INSERT INTO student_grades (student_id, grade_id, grade_date) 
VALUES 
(1, 9, '2025-01-15'), -- John Smith, grade 5.0
(1, 8, '2025-01-16'), -- John Smith, grade 4.5
(1, 10, '2025-01-06'), -- John Smith, grade 6 
(1, 1, '2025-01-07'), -- John Smith, grade 1 
(1, 2, '2025-01-08'), -- John Smith, grade 1.5 
(2, 5, '2025-01-15'), -- Anna Brown, grade 3.0
(3, 10, '2025-01-17'), -- Peter Johnson, grade 6.0
(4, 6, '2025-01-18'), -- Mary Williams, grade 3.5
(4, 2, '2025-01-18'), -- Mary Williams, grade 3.5
(5, 2, '2025-01-18'); -- John Doe, grade 1.5


-- wyswietlanie wszystkich studentow
-- select * from students;


-- wyswietlanie wszystkich studentow wraz z klasami, ktory maja na imie 'John'
select * from students
left join classes on 
( students.class_id  =  classes.id )
where students.first_name = 'John';

-- nie zapomnij o wstawieniu srednika koncu kazdego polecenia SQL, oraz przejscia do nowej linji