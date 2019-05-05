# Import the required dependencies
from Crypto.PublicKey import RSA

# Make a function that generates a public-private key pair
def generateKey (bits = 2048):
    
    # Create a list to store the public-private keys
    keyPair = []

    newKey = RSA.generate (bits, e = 65537)
    publicKey = newKey.publickey().exportKey("PEM")
    privateKey = newKey.exportKey("PEM")

    # Clean up the public key - remove unwanted text
    publicKeyList = publicKey.splitlines()
    publicKeyListTwo = []
    finalPublicKey = ''

    for byteSection in publicKeyList:
        publicKeyListTwo.append(byteSection.decode('utf-8'))

    publicKeyListTwo.pop(0)
    publicKeyListTwo.pop(-1)

    for keySection in publicKeyListTwo:
        finalPublicKey += keySection

    print(finalPublicKey)
    
    # Clean up the private key - remove unwanted text
    privateKeyList = privateKey.splitlines()
    privateKeyListTwo = []
    finalPrivateKey = ''

    for byteSection in privateKeyList:
        privateKeyListTwo.append(byteSection.decode('utf-8'))

    privateKeyListTwo.pop(0)
    privateKeyListTwo.pop(-1)

    for keySection in privateKeyListTwo:
        finalPrivateKey += keySection

    keyPair.append(finalPublicKey)
    keyPair.append(finalPrivateKey)

    # Return the list that contains the public-private keys
    return keyPair

if __name__ ==  "__main__":
    generateKey()