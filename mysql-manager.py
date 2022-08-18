import mysql.connector

class sql_manager:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="12345678",
        database="TESTDB"
    )

    mycursor = mydb.cursor()
    mycursor.execute("SHOW TABLES")

    for tb in mycursor:
        print(tb)


