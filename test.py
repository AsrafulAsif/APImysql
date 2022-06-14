import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="api")

mycursor = mydb.cursor()

sql="Insert into users (user_name,user_age) values (%s,%s)"

val=("Hemi","24")
mycursor.execute(sql,val)
mydb.commit()
print("Data is saved")