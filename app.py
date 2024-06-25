from flask import Flask, render_template, request
from cs50 import SQL


app = Flask(__name__)

# Connect database
db = SQL("sqlite:///number.db")

@app.route("/", methods=["GET", "POST"])
def index():
    # db.execute("INSERT INTO num (number) VALUES (?)", 122)
    
    if request.method == "POST":
        number = request.form.get("number")
        db.execute("UPDATE num SET number = ? WHERE id = 1", number)

    num_from_db = db.execute("SELECT * FROM num WHERE id = 1")[0]["number"]

    return render_template("index.html", num_from_db=num_from_db)