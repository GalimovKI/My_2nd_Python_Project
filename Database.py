import sqlite3


async def conn_start():
    global conn, cur
    conn = sqlite3.connect('Database/unreal_kirill.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users("
            "id INTEGER PRIMARY KEY AUTOINCREMENT,"
            " phone_number TEXT, "
            "email TEXT, "
            "in_payload TEXT)")
    conn.commit()


async def add_user(phone_number, email, in_payload):
    cur.execute("INSERT INTO users (phone_number, email, in_payload) "
                "VALUES ('%s','%s','%s')" % (phone_number, email, in_payload))
    conn.commit()