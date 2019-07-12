# Import the dependencies
import random
import string
import urllib.request

def generateWords ():
    # Create an alphabet list
    # Use only lowercase letters to simplify the large list
    alphabetList = list(string.ascii_lowercase)

    # Open the URL that contains the words
    wordsUrl = "https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english-no-swears.txt"
    UrlResponse = urllib.request.urlopen(wordsUrl)

    # Read the words and create a list of them
    longText = UrlResponse.read().decode()
    wordsList = longText.splitlines()

    # Clean up the list of words
    for index, word in enumerate(wordsList):
        for letter in word:
            if letter not in alphabetList:
                wordsList.pop(index)

    # List that stores the 7 random words
    userWords = []

    # Randomly append 7 words to userWords
    def randomWords (listWords):
        for num in range (0, 7):
            listWords.append(random.choice(wordsList))

    randomWords(userWords)

    return userWords
