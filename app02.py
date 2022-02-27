from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///IOTtest01.db" #usinf SQLITE and define the name of the database.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False # Stop warnings while generating the daatbase.
db=SQLAlchemy(app)

class iotTable(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    mail=db.Column(db.String(100),nullable=False)
    name=db.Column(db.String(50),nullable=False)

@app.route("/")
def hello_world():
    return render_template('webApp01.html')

if(__name__)=="__main__": #main fxn
    app.run(debug=True)