import sqlite3 as sql

with sql.connect('saper.db') as con:
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    hobby VARCHAR(50),
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    birth_year INTEGER,
    homework_score INTEGER
       )''')
    cur.execute('''INSERT INTO student (hobby, first_name, last_name, birth_year, homework_score)
VALUES ('Футбол', 'Петр', 'Иванов', 1995, 8),
       ('Рисование', 'Анна', 'Ивлеева', 1998, 12),
       ('Теннис', 'Антон', 'Сидоров', 1996, 15),
       ('Плавание', 'Реана', 'Смирнова', 1997, 9),
       ('Музыка', 'Алексей', 'Конев', 1999, 10),
       ('Кино', 'Мария', 'Давыдова', 1996, 18),
       ('Компьютерные игры', 'Сергей', 'Пчелкин', 1997, 5),
       ('Футбол', 'Елена', 'Сметанина', 1998, 14),
       ('Рисование', 'Ильяз', 'Беков', 1999, 7),
       ('Теннис', 'Даниель', 'Нурматов', 1997, 11);''')
    cur.execute('''SELECT * FROM student WHERE LENGTH(last_name) > 10''')
    cur.execute('''UPDATE student SET first_name = 'genius' WHERE homework_score > 10''')
    cur.execute('''SELECT * FROM student WHERE first_name = "genius"''')
    cur.execute('''DELETE FROM student WHERE id % 2 = 0''')
