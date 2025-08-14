import mysql.connector

connection = None
cursor = None

try:
    connection = mysql.connector.connect(host="localhost", user="root", passwd="")
    query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
    cursor = connection.cursor()
    cursor.execute(query)
    print("Database 'alx_book_store' created successfully!")
    connection.commit()

except mysql.connector.Error as err:
    print(err)

finally:
    connection.close()
    cursor.close()
