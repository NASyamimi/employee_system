import psycopg2

print("PostgreSQL connection library berjaya!")


def connect_db():

    connection = psycopg2.connect(
        host="localhost",
        database="db_employee",
        user="postgres",
        password="1234",
        port="5432"
    )

    return connection


try:

    connection = connect_db()

    print("Berjaya connect PostgreSQL!")

    connection.close()

except Exception as e:

    print("Connection error:", e)

def insert_staff(staff):
    connection=connection_db()
    cursor= connection.cursor()

    query="""
        CREATE TABLE staff(
        employee_id VARCHAR (10) PRIMARY KEY,
        nama VARCHAR (100) NOT NULL,
        email VARCHAR (100) NOT NULL,
        phone VARCHAR (100) NOT NULL
        );
        """

    cursor.execute(
        query,
        (
            staff["employee_id"],
            staff["nama"],
            staff["email"],
            staff["phone"]
        )
    )
    connection.commit()

    cursor.close()
    connection.close()