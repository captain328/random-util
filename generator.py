from randomutil import *

DUMMY_USER_COUNT = 100
IMAGE_COUNT = 5

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
    img_datas = []
    for i in range(IMAGE_COUNT):
        f = open(f"f:/images/avatars/img{i+1}.png", "rb")
        img_datas.append(f.read())
        f.close()
    for i in range(DUMMY_USER_COUNT):
        cursor.execute('insert into ChatUsers (email, displayName, avatar) values (?, ?, ?)', (emails[i], users[i], pyodbc.Binary(img_datas[i % IMAGE_COUNT])))
    conn.commit()
    conn.close()