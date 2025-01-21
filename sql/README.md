# school - sql


--
-- dane w postaci płaskiej tabeli
--

mysql> SELECT 
    ->     s.id AS student_id,
    ->     s.first_name AS first_name,
    ->     s.last_name AS last_name,
    ->     c.name AS class_name,
    ->     GROUP_CONCAT(gd.grade_value ORDER BY sg.grade_date SEPARATOR ', ') AS grades
    -> FROM students s
    -> LEFT JOIN classes c ON s.class_id = c.id
    -> LEFT JOIN student_grades sg ON s.id = sg.student_id
    -> LEFT JOIN grades_dictionary gd ON sg.grade_id = gd.id
    -> GROUP BY s.id
    -> ORDER BY c.name, s.id;
+------------+------------+-----------+------------+-------------------------+
| student_id | first_name | last_name | class_name | grades                  |
+------------+------------+-----------+------------+-------------------------+
|          5 | John       | Doe       | NULL       | 1.5                     |
|          3 | Peter      | Johnson   | 5b         | 6.0                     |
|          4 | Mary       | Williams  | 5b         | 1.5, 3.5                |
|          6 | Kristen    | Bell      | 5b         | NULL                    |
|          1 | John       | Smith     | 7a         | 6.0, 1.0, 1.5, 5.0, 4.5 |
|          2 | Anna       | Brown     | 7a         | 3.0                     |
+------------+------------+-----------+------------+-------------------------+
6 rows in set (0.00 sec)

mysql> 

-- zrzut tabeli students
mysql> SELECT * FROM students;
+----+------------+-----------+----------+
| id | first_name | last_name | class_id |
+----+------------+-----------+----------+
|  1 | John       | Smith     |        1 |
|  2 | Anna       | Brown     |        1 |
|  3 | Peter      | Johnson   |        2 |
|  4 | Mary       | Williams  |        2 |
|  5 | John       | Doe       |     NULL |
|  6 | Kristen    | Bell      |        2 |
+----+------------+-----------+----------+
6 rows in set (0.00 sec)

mysql> 

-- zrzut tabeli classes
mysql> SELECT * FROM classes;
+----+------+
| id | name |
+----+------+
|  1 | 7a   |
|  2 | 5b   |
+----+------+
2 rows in set (0.00 sec)

mysql> 

-- zrzut tabeli grades_dictionary (wszystkioe dostepne oceny)
mysql> SELECT * FROM grades_dictionary;
+----+-------------+---------------------+
| id | grade_value | description         |
+----+-------------+---------------------+
|  1 |         1.0 | Very Poor           |
|  2 |         1.5 | Poor                |
|  3 |         2.0 | Unsatisfactory      |
|  4 |         2.5 | Almost Satisfactory |
|  5 |         3.0 | Satisfactory        |
|  6 |         3.5 | Good                |
|  7 |         4.0 | Very Good           |
|  8 |         4.5 | Almost Excellent    |
|  9 |         5.0 | Excellent           |
| 10 |         6.0 | Outstanding         |
+----+-------------+---------------------+
10 rows in set (0.00 sec)

-- Zrzut tabeli student_grades: oceny studentów - tabela łącząca (many-to-many)
mysql> SELECT * FROM `student_grades`;
+----+------------+----------+------------+
| id | student_id | grade_id | grade_date |
+----+------------+----------+------------+
|  1 |          1 |        9 | 2025-01-15 |
|  2 |          1 |        8 | 2025-01-16 |
|  3 |          1 |       10 | 2025-01-06 |
|  4 |          1 |        1 | 2025-01-07 |
|  5 |          1 |        2 | 2025-01-08 |
|  6 |          2 |        5 | 2025-01-15 |
|  7 |          3 |       10 | 2025-01-17 |
|  8 |          4 |        6 | 2025-01-18 |
|  9 |          4 |        2 | 2025-01-18 |
| 10 |          5 |        2 | 2025-01-18 |
+----+------------+----------+------------+
10 rows in set (0.00 sec)

mysql> 

-- Wyświetlenie wszystkich uczniów z ich klasami (w tym tych bez klasy):

mysql> SELECT 
    ->     s.first_name, 
    ->     s.last_name, 
    ->     c.name AS class
    -> FROM students s
    -> LEFT JOIN classes c ON s.class_id = c.id;
+------------+-----------+-------+
| first_name | last_name | class |
+------------+-----------+-------+
| John       | Smith     | 7a    |
| Anna       | Brown     | 7a    |
| Peter      | Johnson   | 5b    |
| Mary       | Williams  | 5b    |
| John       | Doe       | NULL  |
| Kristen    | Bell      | 5b    |
+------------+-----------+-------+
6 rows in set (0.00 sec)

mysql> 

-- Wyświetlenie wszystkich uczniów z ich klasami (tylko tych ktorzy posiadaja klase)

mysql> SELECT  s.first_name, s.last_name, c.name AS class FROM students s  JOIN classes c ON s.class_id = c.id;
+------------+-----------+-------+
| first_name | last_name | class |
+------------+-----------+-------+
| John       | Smith     | 7a    |
| Anna       | Brown     | 7a    |
| Peter      | Johnson   | 5b    |
| Mary       | Williams  | 5b    |
| Kristen    | Bell      | 5b    |
+------------+-----------+-------+
5 rows in set (0.00 sec)

-- Wyświetlenie uczniów z ich ocenami (w tym tych bez ocen):

mysql>  SELECT 
    ->       c.name,
    ->               s.first_name, 
    ->               s.last_name, 
    ->               gd.grade_value, 
    ->               gd.description, 
    ->               sg.grade_date
    ->           FROM students s
    ->           LEFT JOIN classes c ON s.class_id = c.id
    ->           LEFT JOIN student_grades sg ON s.id = sg.student_id
    ->           LEFT JOIN grades_dictionary gd ON sg.grade_id = gd.id;
+------+------------+-----------+-------------+------------------+------------+
| name | first_name | last_name | grade_value | description      | grade_date |
+------+------------+-----------+-------------+------------------+------------+
| 7a   | John       | Smith     |         5.0 | Excellent        | 2025-01-15 |
| 7a   | John       | Smith     |         4.5 | Almost Excellent | 2025-01-16 |
| 7a   | John       | Smith     |         6.0 | Outstanding      | 2025-01-06 |
| 7a   | John       | Smith     |         1.0 | Very Poor        | 2025-01-07 |
| 7a   | John       | Smith     |         1.5 | Poor             | 2025-01-08 |
| 7a   | Anna       | Brown     |         3.0 | Satisfactory     | 2025-01-15 |
| 5b   | Peter      | Johnson   |         6.0 | Outstanding      | 2025-01-17 |
| 5b   | Mary       | Williams  |         3.5 | Good             | 2025-01-18 |
| 5b   | Mary       | Williams  |         1.5 | Poor             | 2025-01-18 |
| NULL | John       | Doe       |         1.5 | Poor             | 2025-01-18 |
| 5b   | Kristen    | Bell      |        NULL | NULL             | NULL       |
+------+------------+-----------+-------------+------------------+------------+
11 rows in set (0.01 sec)

mysql> 


mysql> 


mysql> 
-- 
-- Utwórz bazę danych i przełącz się na nia, graj tabele i przykladowe dane
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
('Kristen' 'bell', 2); -- brak ocen 
 

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
(2, 5, '2025-01-15'), -- Anna Brown, grade 3.0
(3, 10, '2025-01-17'), -- Peter Johnson, grade 6.0
(4, 6, '2025-01-18'); -- Mary Williams, grade 3.5
(5, 2, '2025-01-18'); -- John Doe, grade 1.5

