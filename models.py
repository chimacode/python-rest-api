import logging
import sqlite3 as sql


logger = logging.getLogger(__name__)


DATABASE = 'user.db'


def select_all():
    query = "SELECT * FROM user"

    conn = sql.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute(query)

    users = cursor.fetchall()

    conn.close()

    return users


def select_by_username(username):
    query = "SELECT * FROM user WHERE username=?"

    conn = sql.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute(query, (username,))

    user = cursor.fetchone()

    conn.close()

    return user


def insert_user(username, name, email):
    query = "INSERT INTO user (username, name, email) VALUES (?, ?, ?)"

    conn = sql.connect(DATABASE)

    cursor = conn.cursor()

    try:
        cursor.execute(query, (username, name, email))

    except:
        inserted = False

    else:
        inserted = True

    conn.commit()
    conn.close()

    return inserted


def update_user(username, name, email):
    query = """
        UPDATE user
        SET username = ?, name = ?, email = ?
        WHERE username = ?
        """

    conn = sql.connect(DATABASE)

    cursor = conn.cursor()

    try:
        cursor.execute(query, (username, name, email, username))

    except:
        updated = False

    else:
        updated = True

    conn.commit()
    conn.close()

    return updated


def delete_user(username):
    query = """
        DELETE FROM user
        WHERE username = ?
        """

    conn = sql.connect(DATABASE)

    cursor = conn.cursor()

    try:
        logger.debug(cursor.execute(query, (username,)))

    except:
        deleted = False

    else:
        deleted = True

    conn.commit()
    conn.close()

    return deleted
