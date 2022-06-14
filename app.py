from flask import Flask , request , jsonify
import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="api")

mycursor = mydb.cursor(buffered=True)

app = Flask(__name__)

@app.route('/insert',methods=['POST'])
def home():
    userName = request.form.get('name')
    userAge = request.form.get('age')

    print(userName)
    print(userAge)
    sql = "Insert into users (user_name,user_age) values (%s,%s)"
    val = (userName, userAge)
    mycursor.execute(sql, val)
    mydb.commit()

    response = jsonify(
        {
            "massage":"sent data into database!"
        }
    )
    return response



@app.route('/collect',methods=['POST'])
def collect():
    userName = request.form.get('name')
    print(userName)
    sql = "SELECT user_name,user_age from users WHERE user_name = %s"
    val=(userName,)
    # Executing the query
    mycursor.execute(sql,val)
    mydb.commit()

    # Fetching 1st row from the table
    result = mycursor.fetchall()
    for row in result:
        return jsonify({'Age': row[1]})



if __name__ == '__main__':
    app.run(debug=True)