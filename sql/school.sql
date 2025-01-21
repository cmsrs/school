-- 
-- Utwórz bazę danych i przełącz się na nią
--

DROP DATABASE IF EXISTS school;
CREATE DATABASE school  CHARACTER SET utf8mb4  COLLATE utf8mb4_unicode_ci;
USE school;

--
-- Tabela przechowuje dane o klasach.
--
CREATE TABLE classes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(10) NOT NULL
);

--
-- Tabela przechowuje dane o uczniach, z relacją do tabeli classes.
--
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    class_id INT NULL,
    FOREIGN KEY (class_id) REFERENCES classes(id) ON DELETE CASCADE
);

--
-- Tabela przechowuje możliwe wartości ocen.
--
CREATE TABLE grades_dictionary (
    id INT AUTO_INCREMENT PRIMARY KEY,
    grade_value DECIMAL(3, 1) NOT NULL UNIQUE,
    description VARCHAR(100) DEFAULT NULL
);

--
-- Tabela wiąże uczniów z ocenami z tabeli słownikowej.
--
CREATE TABLE student_grades (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    grade_id INT NOT NULL,
    grade_date DATE NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
    FOREIGN KEY (grade_id) REFERENCES grades_dictionary(id) ON DELETE CASCADE
);

--
-- dodanie przykladowych danych
--

INSERT INTO classes (name) VALUES 
('7a'), 
('5b');

INSERT INTO students (first_name, last_name, class_id) 
VALUES 
('John', 'Smith', 1), 
('Anna', 'Brown', 1), 
('Peter', 'Johnson', 2), 
('Mary', 'Williams', 2),
('John', 'Doe', null),  -- brak klasy
('Kristen', 'Bell', 2); -- brak ocen 
 

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

