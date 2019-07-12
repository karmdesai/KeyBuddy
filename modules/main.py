# Import the dependencies
import hashlib
import sqlite3
from modules import generateKey
from modules import generateWords

conn = sqlite3.connect("sshDatabase.db", check_same_thread = False)
cur = conn.cursor()

# Create the table
cur.execute ('''CREATE TABLE IF NOT EXISTS userDatabase (publicKey, privateKey, wordOne,
            wordTwo, wordThree, wordFour, wordFive, wordSix, wordSeven)''')
conn.commit()

class Main ():
    # masterList that contains all of the users
    masterList = []

    # Hash function
    def hash (self, wordToHash):
        wordToHashByte = str.encode(wordToHash)
        hashObject = hashlib.sha256(wordToHashByte).hexdigest()

        return hashObject

    # User ssh-key generator
    def generateNewUser (self):

        wordOne = str(generateWords.generateWords()[0])
        wordTwo = str(generateWords.generateWords()[1])
        wordThree = str(generateWords.generateWords()[2])
        wordFour = str(generateWords.generateWords()[3])
        wordFive = str(generateWords.generateWords()[4])
        wordSix = str(generateWords.generateWords()[5])
        wordSeven = str(generateWords.generateWords()[6])

        userInfo = {
            'publicKey': generateKey.generateKey()[0],
            'privateKey': generateKey.generateKey()[1],

            # Randomly generate seven words and hash them
            'wordOne': self.hash(wordOne),
            'wordTwo': self.hash(wordTwo),
            'wordThree': self.hash(wordThree),
            'wordFour': self.hash(wordFour),
            'wordFive': self.hash(wordFive),
            'wordSix': self.hash(wordSix),
            'wordSeven': self.hash(wordSeven)
        }

        self.masterList.append(userInfo)

        # Large multi-line string that will be returned when a new user is created
        # Uses HTML within the string - have to find a workaround for that
        userAccountInfo = """
        <center><h1>Account Information</h1></center>
        <p>Your Words (In Order) Are:
            <ol>
                <li>{}</li> <br> <li>{}</li> <br> <li>{}</li> <br> <li>{}</li>
                 <br> <li>{}</li> <br> <li>{}</li> <br> <li>{}</li>
            </ol>
            <br>
            <em>Remember these words! They cannot be reset and
            you will need them to log in!</em> <br><br><br>
            <strong>Your Public Key Is:</strong> {} <br><br>
            <strong>Your Private Key Is:</strong> {} </p>""".format (wordOne, wordTwo, wordThree,
            wordFour, wordFive, wordSix, wordSeven, userInfo['publicKey'], userInfo['privateKey'])

        userInfoTuple = (userInfo['publicKey'], userInfo['privateKey'], wordOne, wordTwo, wordThree,
        wordFour, wordFive, wordSix, wordSeven)

        cur.execute('INSERT INTO userDatabase VALUES (?,?,?,?,?,?,?,?,?)', userInfoTuple)
        conn.commit()

        return userAccountInfo
