import sqlite3

def open_connection():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()

    return (conn, cur)

def close_connection(conn):
    conn.commit()
    conn.close()

def connect():
    (conn, cur) = open_connection()

    cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    close_connection(conn)

def insert(title, author, year, isbn):
    (conn, cur) = open_connection()
    cur.execute("INSERT INTO books VALUES (NULL, ?, ?, ?, ?)", (title, author,
        year, isbn))
    close_connection(conn)

def view():
    (conn, cur) = open_connection()

    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()

    close_connection(conn)

    return rows

def search(title = "", author = "", year = "", isbn = ""):
    (conn, cur) = open_connection()
    cur.execute("SELECT * FROM books WHERE title = ? OR author = ? OR year = ? OR isbn = ?", (title, author, year, isbn))
    
    rows = cur.fetchall()
    close_connection(conn)

    return rows

def delete(id):
    (conn, cur) = open_connection()
    cur.execute("DELETE FROM books WHERE id = ?", (id,))
    close_connection(conn)

def update(id, title, author, year, isbn):
    (conn, cur) = open_connection()
    cur.execute("UPDATE books SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?", ( title, author, year, isbn, id))
    close_connection(conn)

connect()
