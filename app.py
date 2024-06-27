from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, emit
import sqlite3

app = Flask(__name__)
app.config["SECRET_KEY"] = "kj12h3jhwfikhkkjHFAJKHddsj"
socketio = SocketIO(app, async_mode="gevent")

def search_db(action):
    connect = sqlite3.connect("number.db")
    connect.row_factory = sqlite3.Row
    db = connect.cursor()
    db.execute(action)

    return db.fetchone()["number"]

def update_db(action, tup):
    connect = sqlite3.connect("number.db", check_same_thread=False)
    db = connect.cursor()
    db.execute(action, tup)

    # Needed to make changes permanent after page refresh
    connect.commit()
    connect.close()

    return True


@app.route("/", methods=["GET", "POST"])
def index(): 
    num_from_db = search_db("SELECT * FROM num WHERE id = 1")

    return render_template("index.html", num_from_db=num_from_db)


# This helps prevent "Confirm form resubmission" on index
@app.route('/submit', methods=["POST"])
def submit():
    if request.method == "POST":
        number = request.form.get("number")
        update_db("UPDATE num SET number = ? WHERE id = 1", (number,)) 
    
    return redirect(url_for("index"))


# sockets
@socketio.on("change number")
def change_number(data):
    update_db("UPDATE num SET number = ? WHERE id = 1", (data,))
    emit("update value", data)

if __name__ == '__main__':
    socketio.run(app)
