import mysql.connector


query = "CREATE TABLE IF NOT EXISTS customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))"

try:
    connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="connector"
    )

    cursor = connection.cursor()
    cursor.execute(query)

    result = cursor.fetchall()
    print(result) 

    connection.commit() # commit the changes to the database
except mysql.connector.Error as err:
    print("Error: {}".format(err))

finally:    
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")

