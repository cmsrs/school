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
('John', 'Doe', NULL), 
('Kristen', 'Bell', 2);


-- wybierz wszystkich studentow
select * from students;


-- wybierz wszystkie studentki
select * from  classes;


-- wyswietlanie wszystkich studentow wraz z klasami, ktory maja na imie 'John'
select * from students
left join classes on 
( students.class_id  =  classes.id )
where students.first_name = 'John';


-- wyswietlanie wszystkich studentow, ktory maja na imie 'John' i mają przypisaną klasę
select * from students
join classes on 
( students.class_id  =  classes.id )
where students.first_name = 'John';


-- koniec pliku