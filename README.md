# KeyBuddy
We realized that online security is the backbone of our digital world. We wanted to create a convenient yet secure authentication platform that could be integrated with developers' web applications.

KeyBuddy is a login platform that uses Secure Shell (SSH) keys paired with a unique seven-word combination to ensure reliability and ease. In order to build the platform, we first created several Python modules that were responsible for generating unique seven-word combinations as well as public-private key pairs. After that, we created a hash function (using SHA-256) and worked with our local database (using SQLite). Finally, we used HTML, CSS, and Flask in order to create a sample website that used KeyBuddy to handle user credentials. Since we are a group of beginners, using Flask was a challenge but we managed to create a web application.

### Usage
```sh
$ git clone https://github.com/karmdesai/KeyBuddy.git
$ cd KeyBuddy
$ python app.py
```

### What's Next
- [x] Style the web application.
- [] Create a sample service that can used to demo KeyBuddy (e.g. a messaging platform).
- [] Switch from a local, centralized solution to a decentralized solution (e.g. blockchain).