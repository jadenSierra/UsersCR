from flask import Flask, redirect, request,session, render_template
from user import User

app = Flask(__name__)
app.secret_key = "shhh"

@app.route('/')
def home_page():
    users = User.get_all()
    return render_template("index.html", users = users)

@app.route('/create')
def create_user():
    return render_template("create.html")

@app.route('/create_user', methods=["POST"])
def create_friend():
    data = {
        "fname": request.form['fname'],
        "lname": request.form['lname'],
        "email": request.form['email']
    }

    User.save(data)

    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)