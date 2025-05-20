import psycopg2


def write_data(data):
    with psycopg2.connect(
        dbname="myapp_db",
        user="myapp_user",
        password="mypassword",
        host="localhost",
        port="5432"
    ) as connect:
        with connect.cursor() as cursor:
            print("Data to be inserted:", data)
            cursor.executemany('''INSERT INTO watches (watch_code, watch_name, watch_old_price, watch_new_price) VALUES (%s, %s, %s, %s)''', data)
            connect.commit()

def read_data():
    with psycopg2.connect(
            dbname="myapp_db",
            user="myapp_user",
            password="mypassword",
            host="localhost",
            port="5432"
    ) as connect:
        with connect.cursor() as cursor:
            cursor.execute("SELECT * FROM watches")
            data = cursor.fetchall()
    return data