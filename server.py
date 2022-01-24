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

@app.route('/create/user', methods=["POST"])
def create_friend():
    data = {
        "fname": request.form['fname'],
        "lname": request.form['lname'],
        "email": request.form['email']
    }
    User.save(data)
    return redirect('/')

@app.route('/user/destroy/<int:id>')
def destroy(id):
    data = {
        "id" : id
    }
    User.destroy(data)
    return redirect("/")

@app.route('/user/edit/<int:id>')
def edit_user(id):
    data = {
        "id": id
    }
    user = User.get_one(data)
    return render_template("edit.html", user = user)

@app.route('/update/user', methods = ["POST"])
def update_user():
    User.update(request.form)
    return redirect('/')

@app.route("/user/show/<int:id>")
def show(id):
    data = {
        'id': id
    }
    user = User.get_one(data)
    return render_template("show.html", user = user)



if __name__ == "__main__":
    app.run(debug=True)