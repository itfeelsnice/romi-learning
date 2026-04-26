
from flask import Flask, session, render_template, redirect, request
from werkzeug.security import generate_password_hash, check_password_hash
import psycopg2
import os
from dotenv import load_dotenv

start1 = Flask(__name__)
start1.secret_key = "hello152carbaro"

load_dotenv("secret.env") 

connect1 = psycopg2.connect(host = os.getenv("host1"),
                            database = os.getenv("database1"),
                            user = os.getenv("user1"),
                            password = os.getenv("password1"),
                            port = os.getenv("port1")
                            )

execute1 = connect1.cursor()

@start1.route("/", methods = ["GET", "POST"])
def first1():
    if request.method == "POST":
        username1 = request.form["input1"]
        password1 = request.form["input2"]
        execute1.execute("""CREATE TABLE IF NOT EXISTS users1(
                            id1 SERIAL PRIMARY KEY,
                            username1 TEXT,
                            password TEXT
                         )""")

        execute1.execute("SELECT password FROM users1 WHERE username1 = (%s)", (username1,))
        check1 = execute1.fetchone()
        
        if check1 and check_password_hash(check1[0], password1):
            return redirect("/romi")
        else: 
            pass
    return render_template("login.html")

@start1.route("/singup", methods = ["GET", "POST"])
def second2():
    if request.method == "POST":
        username2 = request.form["input3"]
        password2 = request.form["input4"]
        if len(username2.strip()) >= 4 and len(password2.strip()) >= 4:
            session["name"] = username2
            secure_pass = generate_password_hash(password2)

            execute1.execute("INSERT INTO users1 (username1, password) VALUES (%s, %s)", (username2, secure_pass,))
            connect1.commit()
            return redirect("/")
        else: 
            pass
    return render_template("singup.html")

@start1.route("/romi")
def third3():
    return render_template("romi.html")


start1.run(debug=True)
connect1.close()












