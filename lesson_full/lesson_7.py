import sqlite3


def crate_tables():
    """Функция для создания таблиц"""

    # удаление таблицы
    conn.execute("DROP TABLE IF EXISTS students")

    # создание таблицы students с колонками
    conn.execute("""
         CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            city TEXT
        )
    """)


def add_student(name, age, city):
    """Функция для добавления студента в базу данных"""

    # внесение новых данных в таблицу students
    conn.execute(
        "INSERT INTO students (name, age, city) VALUES (?, ?, ?)", (name, age, city)
    )
    conn.commit()


def delete_student(student_id):
    """Функция для удаления студента из базы данных по id"""

    conn.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()


if __name__ == "__main__":
    conn = sqlite3.connect("database.db")

    crate_tables()

    add_student("Aibek", 23, "Bishkek")
    add_student("Aisulu", 19, "Karakol")
    add_student("Nursultan", 21, "Osh")
    add_student("Maksat", 22, "Bishkek")
    add_student("Aidana", 20, "Karakol")
    add_student("Bakyt", 24, "Osh")
    add_student("Gulnara", 18, "Bishkek")
    add_student("Tilek", 23, "Karakol")

    delete_student(1)

    conn.close()