from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///villain.db"
db = SQLAlchemy(app)


class Villain(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120), nullable=False)
    interests = db.Column(db.String(250), nullable=False)
    url = db.Column(db.String(250), nullable=False)
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return "<Villain "+ self.name + ">"

with app.app_context():
	db.create_all()
	db.session.commit()

#### Serving Static Files
@app.route("/")
def villain_cards():
  return app.send_static_file("villain.html")

@app.route("/add")
def add():
  return app.send_static_file("addvillain.html")

@app.route("/delete")
def delete():
  return app.send_static_file("deletevillain.html")

app.route("/api/villains/", methods=["GET"])
def get_villains():
  villains=Villain.query.all()
  data = []
  return

@app.route("/api/villains/add", methods=["POST"])
def add_villain():
  errors = []
  name = request.form.get("name")

  if not name:
    errors.append("Oops! Looks like you forgot a name!")

  description = request.form.get("description")
  if not description:
    errors.append("Oops! Looks like you forgot a description!")
  
  interests = request.form.get("interests")
  if not interests:
    errors.append("Oops! Looks like you forgot some interests!")
  
  url = request.form.get("url")
  if not url:
    errors.append("Oops! Looks like you forgot an image!")
  
  villain = Villain.query.filter_by(name=name).first()
  if villain:
    errors.append("Oops! A villain with that name already exists!")
  
  if errors:
    return jsonify({"errors": errors})
  else:
    new_villain = Villain(name=name,description=description, interests=interests, url=url)
    db.session.add(new_villain)
    db.session.commit()
    return 

@app.route("/api/villains/delete", methods=["POST"])
def delete_villain():
  name = request.form.get("name", "")
  villain = Villain.query.filter_by(name=name).first()
  if villain:
    db.session.delete(villain)
    db.session.commit()
    return 
  else:
    return jsonify({"errors": ["Oops! A villain with that name doesn't exist!"]})


# Run the flask server
if __name__ == "__main__":
    app.run()