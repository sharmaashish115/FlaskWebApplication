#from crypt import methods
#from unicodedata import name
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///IOT.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db=SQLAlchemy(app)
 
class iotTable(db.Model):
    sno=db.Column(db.Integer, primary_key=True)
    mail=db.Column(db.String(100),nullable=False)
    name=db.Column(db.String(50),nullable=False)

def __repr__(self) -> str:
        return f'{self.sno}-{self.mail}'

@app.route("/login",methods=['GET','POST'])
def loginPa():
    if (request.method == 'POST'):
        pwdd=request.form['pass']
        if(pwdd=='123'):
            return render_template('home.html')
    return render_template('loginPage.html')

@app.route("/",methods=['GET','POST']) #decorator; to convert python function to https response, also it gives you multiple end points.
def hello_world():
    if (request.method == 'POST'):
        email=request.form['mail01']
        ename=request.form['name']
        dat = iotTable(mail=email,name=ename)
        db.session.add(dat)
        db.session.commit()
    alldat = iotTable.query.all()
    print(alldat)
    return render_template('home.html',alldat=alldat)

@app.route("/delete/<int:sno>") #decorator; to convert python function to https response, also it gives you multiple end points.
def deleteData(sno):
    dat=iotTable.query.filter_by(sno=sno).first()
    db.session.delete(dat)
    db.session.commit()

    return redirect('/')

@app.route("/update/<int:sno>",methods=['GET','POST']) #decorator; to convert python function to https response, also it gives you multiple end points.
def updateData(sno):
    if (request.method == 'POST'):
        email=request.form['mail01']
        ename=request.form['name']
        dat = iotTable.query.filter_by(sno =sno).first()
        dat.mail=email
        dat.name=ename       
        db.session.add(dat)
        db.session.commit()
        return redirect('/')

    alldat = iotTable.query.filter_by(sno =sno).first()
    #print(alldat)
    return render_template('update.html',alldat=alldat)



if(__name__) == "__main__":
    app.run(debug=True) ##show error on run time; if i change something then it will show up on my output
    
