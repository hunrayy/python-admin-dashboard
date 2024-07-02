from flask import Flask, render_template, request, url_for, redirect, flash, jsonify, sessions
from passlib.hash import sha256_crypt
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "password"
app.config["MYSQL_DB"] = "marvel"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)



@app.route("/register", methods=["GET", "POST"])
def register():
    if(request.method == "POST"):
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]
        passhash = sha256_crypt.encrypt(password)
        dbcon = mysql.connection.cursor()
        if(dbcon):
            sql = f"""
            INSERT INTO user(username, password, email) VALUES(%s, %s, %s)"""
            dbcon.execute(sql, (username, passhash, email))
            mysql.connection.commit()
            return render_template("sign.html")
        return render_template("sign.html")
    return render_template("reg.html")


# login route
@app.route("/login", methods=["GET", "POST"])
def login():
    if(request.method == "POST"):
        email = request.form["email"]
        password = request.form["password"]
        cursor = mysql.connection.cursor()
        if(cursor):
            # return("success")
            sql = f"""
            SELECT * FROM user WHERE email = %s"""
            result = cursor.execute(sql, (email,))
            feedback = cursor.fetchone()
            if(feedback):
                email = feedback["email"]
                passwordDb = feedback["password"]
                if(sha256_crypt.verify(password, passwordDb)):
                    return(render_template("dashboard.html", email=email))
                # return(jsonify(feedback["email"]))
            # cursor.connection.commit()
            # cursor.close()
            # return("hello")
            # return(jsonify(result))
        return(render_template("sign.html"))
if(__name__ == "__main__"):
    app.run(debug=True)