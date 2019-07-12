# Import the dependencies
import sqlite3
import hashlib
from modules.main import Main
from flask_wtf import FlaskForm
from wtforms import StringField
from flask import Flask, render_template, redirect, url_for
from wtforms.validators import DataRequired, ValidationError, EqualTo

# Connect to the SQLite databases
conn = sqlite3.connect("sshDatabase.db", check_same_thread = False)
cur = conn.cursor()

global userKey

# Define the hash function
def hash (wordToHash):
    wordToHashByte = str.encode(wordToHash)
    hashObject = hashlib.sha256(wordToHashByte).hexdigest()

    return hashObject

# Create a function that verifies the public key
def checkPublicKey (className, fieldName):
    userKey = fieldName.data

    cur.execute('SELECT rowid FROM userDatabase WHERE publicKey = (?)', (userKey,))
    data = cur.fetchall()

    # Ensure that the user is registered with info-base
    if len(data) == 0:
        raise ValidationError("Couldn't find the public key!")

# Create a function that verifies the private key
def checkPrivateKey (className, fieldName):
    userKey = fieldName.data

    cur.execute('SELECT privateKey FROM userDatabase WHERE publicKey = (?)', (className.PublicKey.data,))
    data = cur.fetchall()

    # Ensure that the private and public keys march
    if data != [(userKey,)]:
        raise ValidationError("Private-public key pair doesn't match!")

# Create a function that verifies word one
def verifyWordOne (className, fieldName):
    userWord = fieldName.data

    cur.execute('SELECT wordOne FROM userDatabase WHERE publicKey = (?)', (className.PublicKey.data,))
    data = cur.fetchall()

    if data != [(userWord,)]:
        raise ValidationError("Incorrect Word!")

# Create a function that verifies word two
def verifyWordTwo (className, fieldName):
    userWord = fieldName.data

    cur.execute('SELECT wordTwo FROM userDatabase WHERE publicKey = (?)', (className.PublicKey.data,))
    data = cur.fetchall()

    if data != [(userWord,)]:
        raise ValidationError("Incorrect Word!")

# Create a function that verifies word three
def verifyWordThree (className, fieldName):
    userWord = fieldName.data

    cur.execute('SELECT wordThree FROM userDatabase WHERE publicKey = (?)', (className.PublicKey.data,))
    data = cur.fetchall()

    if data != [(userWord,)]:
        raise ValidationError("Incorrect Word!")

# Create a function that verifies word four
def verifyWordFour (className, fieldName):
    userWord = fieldName.data

    cur.execute('SELECT wordFour FROM userDatabase WHERE publicKey = (?)', (className.PublicKey.data,))
    data = cur.fetchall()

    if data != [(userWord,)]:
        raise ValidationError("Incorrect Word!")

# Create a function that verifies word five
def verifyWordFive (className, fieldName):
    userWord = fieldName.data

    cur.execute('SELECT wordFive FROM userDatabase WHERE publicKey = (?)', (className.PublicKey.data,))
    data = cur.fetchall()

    if data != [(userWord,)]:
        raise ValidationError("Incorrect Word!")

# Create a function that verifies word six
def verifyWordSix (className, fieldName):
    userWord = fieldName.data

    cur.execute('SELECT wordSix FROM userDatabase WHERE publicKey = (?)', (className.PublicKey.data,))
    data = cur.fetchall()

    if data != [(userWord,)]:
        raise ValidationError("Incorrect Word!")

# Create a function that verifies word seven
def verifyWordSeven (className, fieldName):
    userWord = fieldName.data

    cur.execute('SELECT wordSeven FROM userDatabase WHERE publicKey = (?)', (className.PublicKey.data,))
    data = cur.fetchall()

    if data != [(userWord,)]:
        raise ValidationError("Incorrect Word!")

class FirstForm(FlaskForm):
    PublicKey = StringField('PublicKey', validators = [DataRequired(), checkPublicKey])
    PrivateKey = StringField('PrivateKey', validators = [DataRequired(), checkPrivateKey])
    wordOne = StringField('Word One', validators = [DataRequired(), verifyWordOne])
    wordTwo = StringField('Word Two', validators = [DataRequired(), verifyWordTwo])
    wordThree = StringField('Word Three', validators = [DataRequired(), verifyWordThree])
    wordFour = StringField('Word Four', validators = [DataRequired(), verifyWordFour])
    wordFive = StringField('Word Five', validators = [DataRequired(), verifyWordFive])
    wordSix = StringField('Word Six', validators = [DataRequired(), verifyWordSix])
    wordSeven = StringField('Word Seven', validators = [DataRequired(), verifyWordSeven])

app = Flask(__name__)
app.config["SECRET_KEY"] = "Hello"

# Rendering the resgistration page
@app.route('/')
def registration():
    return render_template('registration.html')

# Rendering the login page
@app.route('/login', methods=('GET', 'POST'))
def login():
    myForm = FirstForm()
    return render_template('login.html', form = myForm)

# Background process that occurs without refreshing
@app.route('/generate')
def generate():
    mainSession = Main()
    return mainSession.generateNewUser()

# Rendering the message page
@app.route('/message')
def message():
    return render_template('message.html')

# Run the app
if __name__ == '__main__':
    app.run(debug = True)
