from randomutil import *

DUMMY_USER_COUNT = 100

if __name__ == '__main__':
    conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                        'Server=DESKTOP-DK513L4;'
                        'Database=chat;'
                        'Uid=bruce;'
                        'Pwd=bruce123;'
                        'Trusted_Connection=yes;')

    cursor = conn.cursor()

    users = get_random_users(DUMMY_USER_COUNT)
    emails = get_random_emails(DUMMY_USER_COUNT)
    for i in range(DUMMY_USER_COUNT):
        cursor.execute('insert into ChatUsers (email, displayName) values (?, ?)', (emails[i], users[i]))
    conn.commit()
    conn.close()