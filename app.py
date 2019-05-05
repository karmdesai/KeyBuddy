from main import Main 
from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, ValidationError, EqualTo
import sqlite3
import hashlib

app = Flask(__name__)
app.config["TESTING"] = True
app.config["SECRET_KEY"] = "HELLO"

conn = sqlite3.connect("sshDatabase.db", check_same_thread=False)
cur = conn.cursor()
global userKey

def hash (wordToHash):
    wordToHashByte = str.encode(wordToHash)
    hashObject = hashlib.sha256(wordToHashByte).hexdigest()

    return hashObject

def checkPublicKey (className, fieldName):
    userKey = fieldName.data

    cur.execute('SELECT rowid FROM userDatabase WHERE publicKey = (?)', (userKey,))
    data = cur.fetchall()

    # Ensure that the user is registered with info-base
    if len(data) == 0:
        raise ValidationError("Couldn't find the public key!")
    
def checkPrivateKey (className, fieldName):
    userKey = fieldName.data

    cur.execute('SELECT privateKey FROM userDatabase WHERE publicKey = (?)', (className.PublicKey.data,))
    data = cur.fetchall()

    # Ensure that the user is registered with info-base
    if data != [(userKey,)]:
        raise ValidationError("Private-public key pairs don't match!")

def verifyWordOne (className, fieldName):
    userWord = fieldName.data

    cur.execute('SELECT wordOne FROM userDatabase WHERE publicKey = (?)', (className.PublicKey.data,))
    data = cur.fetchall()
    
    if data != [(userWord,)]:
        raise ValidationError("Incorrect Word!")

def verifyWordTwo (className, fieldName):
    userWord = fieldName.data

    cur.execute('SELECT wordTwo FROM userDatabase WHERE publicKey = (?)', (className.PublicKey.data,))
    data = cur.fetchall()
    
    if data != [(userWord,)]:
        raise ValidationError("Incorrect Word!")

def verifyWordThree (className, fieldName):
    userWord = fieldName.data

    cur.execute('SELECT wordThree FROM userDatabase WHERE publicKey = (?)', (className.PublicKey.data,))
    data = cur.fetchall()
    
    if data != [(userWord,)]:
        raise ValidationError("Incorrect Word!")

def verifyWordFour (className, fieldName):
    userWord = fieldName.data

    cur.execute('SELECT wordFour FROM userDatabase WHERE publicKey = (?)', (className.PublicKey.data,))
    data = cur.fetchall()
    
    if data != [(userWord,)]:
        raise ValidationError("Incorrect Word!")

def verifyWordFive (className, fieldName):
    userWord = fieldName.data

    cur.execute('SELECT wordFive FROM userDatabase WHERE publicKey = (?)', (className.PublicKey.data,))
    data = cur.fetchall()
    
    if data != [(userWord,)]:
        raise ValidationError("Incorrect Word!")

def verifyWordSix (className, fieldName):
    userWord = fieldName.data

    cur.execute('SELECT wordSix FROM userDatabase WHERE publicKey = (?)', (className.PublicKey.data,))
    data = cur.fetchall()
    
    if data != [(userWord,)]:
        raise ValidationError("Incorrect Word!")

def verifyWordSeven (className, fieldName):
    userWord = fieldName.data

    cur.execute('SELECT wordSeven FROM userDatabase WHERE publicKey = (?)', (className.PublicKey.data,))
    data = cur.fetchall()
    
    if data != [(userWord,)]:
        raise ValidationError("Incorrect Word!")

class FirstForm(FlaskForm):
    PublicKey = StringField('PublicKey', validators=[DataRequired(), checkPublicKey])
    PrivateKey = StringField('PrivateKey', validators=[DataRequired(), checkPrivateKey])
    wordOne = StringField('Word One', validators =[DataRequired(), verifyWordOne])
    wordTwo = StringField('Word Two', validators =[DataRequired(), verifyWordTwo])
    wordThree = StringField('Word Three', validators =[DataRequired(), verifyWordThree])
    wordFour = StringField('Word Four', validators =[DataRequired(), verifyWordFour])
    wordFive = StringField('Word Five', validators =[DataRequired(), verifyWordFive])
    wordSix = StringField('Word Six', validators =[DataRequired(), verifyWordSix])
    wordSeven = StringField('Word Seven', validators =[DataRequired(), verifyWordSeven])

@app.route('/', methods=('GET', 'POST'))
def login():
    form = FirstForm()
    if form.validate_on_submit():        
        return "Sucessfully logged in! Messaging app coming soon!"

    return render_template('login.html', form=form)

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