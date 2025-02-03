from flask import Flask,request,redirect,url_for,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "1234abcd"

db = SQLAlchemy(app)

class User(db.Model):
  id = db.Column(db.Integer,primary_key = True)
  name = db.Column(db.String(100),nullable=False)
  city = db.Column(db.String(120),nullable=False)
  contact = db.Column(db.String(100),nullable=False)

with app.app_context():
  db.create_all()

@app.route("/")
def index():
  users = User.query.all()
  return render_template("index.html",users=users)

@app.route("/add",methods=['GET','POST'])
def add_user():
  if request.method == "POST":
    name = request.form['name']
    city = request.form['city']
    contact = request.form['contact']
    new_user = User(name=name,city=city,contact=contact)
    try:
      db.session.add(new_user)
      db.session.commit()
      return redirect(url_for("index"))
    except:
      return 'Error adding User!'
  return render_template("add_user.html")

@app.route("/edit/<int:id>",methods=['GET','POST'])
def edit_user(id):
  user = User.query.get(id)
  if request.method == "POST":
    user.name = request.form['name']
    user.city = request.form['city']
    user.contact = request.form['contact']
    db.session.commit()
    return redirect(url_for('index'))
  return render_template("edit_user.html",user=user)

@app.route("/delete/<int:id>")
def delete_user(id):
  user = User.query.get(id)
  db.session.delete(user)
  db.session.commit()
  return redirect(url_for('index'))


if __name__ == "__main__":
  app.run(debug = True)