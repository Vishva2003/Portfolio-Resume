import os
from flask import Flask, render_template,request
import mysql.connector

app = Flask(__name__)
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Vishva2003',
    database='portfolio'
)
cursor = conn.cursor()

@app.route("/", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        USERNAME = request.form['username']
        EMAIL = request.form['email']
        SUBJECT = request.form['subject']
        MESSAGE = request.form['message']

    
        # Account doesnt exists and the form data is valid, now insert new account into accounts table
        query =("INSERT INTO contact (USERNAME ,EMAIL ,MESSAGE) VALUES (%s, %s, %s)")  
        cursor.execute(query, (USERNAME ,EMAIL ,MESSAGE, SUBJECT))
        contact=conn.commit()
    

    # Show registration form with message (if any)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True , port=5000,host= "0.0.0.0")