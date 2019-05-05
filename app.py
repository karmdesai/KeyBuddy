from main import Main 
from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, ValidationError, EqualTo
import sqlite3

app = Flask(__name__)
app.config["TESTING"] = True
app.config["SECRET_KEY"] = "HELLO"

conn = sqlite3.connect("sshDatabase.db", check_same_thread=False)
cur = conn.cursor()

def checkPublicKey (className, fieldName):
    userKey = fieldName.data

    cur.execute('SELECT rowid FROM userDatabase WHERE publicKey = (?)', (userKey,))
    data = cur.fetchall()

    # Ensure that the user is registered with info-base
    if len(data) == 0:
        raise ValidationError("Empty")
    
def checkPrivateKey (className, fieldName):
    userKey = fieldName.data

    cur.execute('SELECT privateKey FROM userDatabase WHERE publicKey = (?)', (className.PublicKey.data,))
    data = cur.fetchall()

    # Ensure that the user is registered with info-base
    if data != [(userKey,)]:
        raise ValidationError("Doesn't match")

def test(a, b):
    print('hello?')
    raise ValidationError("test")

class FirstForm(FlaskForm):
    PublicKey = StringField('PublicKey', validators=[DataRequired(), checkPublicKey])
    PrivateKey = StringField('PrivateKey', validators=[DataRequired(), checkPrivateKey])
class SecondForm(FlaskForm):
    wordOne = StringField('Word One', validators =[DataRequired()])
    wordTwo = StringField('Word Two', validators =[DataRequired()])
    wordThree = StringField('Word Three', validators =[DataRequired()])
    wordFour = StringField('Word Four', validators =[DataRequired()])
    wordFive = StringField('Word Five', validators =[DataRequired()])
    wordSix = StringField('Word Six', validators =[DataRequired()])
    wordSeven = StringField('Word Seven', validators =[DataRequired()])

@app.route('/', methods=('GET', 'POST'))
def login():
    form = FirstForm()
    if form.validate_on_submit():        
        return redirect(url_for('submit2'))

    return render_template('login.html', form=form)

@app.route('/submit2', methods=('GET', 'POST'))
def submit2():
    form = SecondForm()
    if form.validate_on_submit():
        #print(form.PublicKey.data)
       # print(form.PrivateKey.data)
        return redirect('/')
    return render_template('7wordsauth.html', form=form)

#rendering the HTML page which has the button
@app.route('/signup')
def signup():
    return render_template('signup.html')

#background process happening without any refreshing
@app.route('/generate')
def generate():
    mainSession = Main()
    return mainSession.generateNewUser()

if __name__ == '__main__':
    app.run(debug=True)