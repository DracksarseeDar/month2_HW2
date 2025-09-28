import sqlite3

def crate_tables():

    conn.execute('DROP TABLE IF EXISTS books')

    conn.execute("""
        CREATE TABLE IF NOT EXISTS books (           
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            author TEXT,
            publication_year INTEGER,
            genre TEXT,
            number_of_pages INTEGER,
            number_of_copies INTEGER
            )
    """)

def insert_book(name , author , year , genre , pages , copies):
    conn.execute("INSERT INTO books (name, author , publication_year , genre , number_of_pages , number_of_copies )"
                 "VALUES (?, ?, ?, ?, ?, ?)" ,(name, author, year , genre, pages, copies))
    conn.commit()

def delete_books(book_id):
    conn.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()

if __name__ == "__main__":
    conn = sqlite3.connect("database.db")

    crate_tables()


    insert_book("Ultimate Spider-Man", "Brian Michael Bendis", 2000, "Комикс (Marvel)", 11000, 2 )
    insert_book("Invincible", "Robert Kirkman", 2003, "Комикс (Image)", 3300, 3)
    insert_book("Secret Invasion", "Brian Michael Bendis", 2008, "Комикс (Marvel)", 500, 2)
    insert_book("Secret Wars (2015)", "Jonathan Hickman", 2015, "Комикс (Marvel)", 350, 2)
    insert_book( "House of M", "Brian Michael Bendis", 2005, "Комикс (Marvel)", 400, 2)
    insert_book("Civil War", "Mark Millar", 2006, "Комикс (Marvel)", 500, 2)
    insert_book("Dark Reign", "Brian Michael Bendis", 2008, "Комикс (Marvel)", 1200, 2)
    insert_book("Fear Itself", "Matt Fraction", 2011, "Комикс (Marvel)", 400, 2)
    insert_book( "Batman: The Killing Joke", "Alan Moore", 1988, "Графический роман (DC)", 64, 2)
    insert_book("The Boys", "Garth Ennis", 2006, "Комикс (Wildstorm/Dynamite)", 6000, 3)

    delete_books(3)

    conn.close()


