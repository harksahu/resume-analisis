from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:harksahu@localhost/resumeanalisis'
db = SQLAlchemy(app)


class Contactus(db.Model):
    '''
    sno, name phone_num, msg, date, email
    '''
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), primary_key=False)
    phone_no = db.Column(db.String(12), primary_key=False)
    msg = db.Column(db.String(120), primary_key=False)
    date = db.Column(db.String(12), primary_key=False)
    email = db.Column(db.String(20),primary_key=False)


@app.route('/')
def home():
    return render_template('index.html')



@app.route('/login', methods = ['GET', 'POST'])
def login():
    if (request.method == 'POST'):
        username  = request.form['user']
        passward = request.form['pass']
        if(username == "harsh" and passward == "123"):
            return render_template('index.html')
        else:
            return render_template('login.html', msg="!!!!Incorrect user name and passward!!!!!")
    return render_template('login.html')



@app.route('/blogs')
def blogs():
    return render_template('blogs.html')



@app.route('/contact', methods = ['GET', 'POST'])
def contact():
    if (request.method == 'POST'):
        '''Add entry to the database'''
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['msg']
        date = datetime.now()
        print(name ,email,phone,date,message)
        entry = Contactus(name=name, phone_no=phone, msg=message, date=date, email=email)
        # entry = contactus(1,name,email, phone, message, date)
        db.session.add(entry)
        db.session.commit(entry)
    return render_template('contact.html')






app.run(debug = True)