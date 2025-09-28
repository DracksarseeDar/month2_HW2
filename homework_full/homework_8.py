import sqlite3

def crate_tables():

    conn.execute('DROP TABLE IF EXISTS books')


    conn.execute("""
        CREATE TABLE IF NOT EXISTS genres  (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT 
        )    
    """)


    conn.execute("""
        CREATE TABLE IF NOT EXISTS books (           
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            author TEXT,
            publication_year INTEGER,
            genre_id INTEGER,
            number_of_pages INTEGER,
            number_of_copies INTEGER,
            FOREIGN KEY (genre_id) REFERENCES genres(id)
            )
    """)

def add_genre(name: str):
    conn.execute("INSERT INTO genres (name) VALUES (?)", (name,))
    conn.commit()


def insert_book(name: str , author: str , year: int ,  pages: int , copies: int  , genre_id: int):
    conn.execute("INSERT INTO books (name, author , publication_year ,  number_of_pages , number_of_copies ,genre_id )"
                 "VALUES (?, ?, ?, ?, ?, ?)" ,(name, author, year ,  pages, copies , genre_id))
    conn.commit()

def delete_books(book_id: int ):
    conn.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()
def get_all_books():
    results = conn.execute("""
         SELECT b.id, b.name AS book_name, b.author, g.name AS genre_name
        FROM books AS b
        JOIN genres AS g ON b.genre_id = g.id
    """)
    return results.fetchall()


if __name__ == "__main__":
    conn = sqlite3.connect("database.db")

    crate_tables()

    add_genre("Комикс (Marvel)") #1
    add_genre("Комиксы (DC)") #2
    add_genre("Комикс (Image)") #3
    add_genre("Комикс (Wildstorm/Dynamite)") #4


    insert_book("Ultimate Spider-Man", "Brian Michael Bendis", 2000, 11000, 2 , 1)
    insert_book("Invincible", "Robert Kirkman", 2003,  3300, 3 , 3)
    insert_book("Secret Invasion", "Brian Michael Bendis", 2008,  500, 2 ,1)
    insert_book("Secret Wars (2015)", "Jonathan Hickman", 2015,  350, 2, 1)
    insert_book( "House of M", "Brian Michael Bendis", 2005,  400, 2 , 1)
    insert_book("Civil War", "Mark Millar", 2006,  500, 2 , 1)
    insert_book("Dark Reign", "Brian Michael Bendis", 2008,  1200, 2 , 1)
    insert_book("Fear Itself", "Matt Fraction", 2011,  400, 2 ,1)
    insert_book( "Batman: The Killing Joke", "Alan Moore", 1988,  64, 2 , 2)
    insert_book("The Boys", "Garth Ennis", 2006,  6000, 3, 4)

    delete_books(3)
    print(get_all_books())
    conn.close()


