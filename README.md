# Encrypt.io: A simple app to encrypt files

##What It Does

The encrypt.io app uses Fernet from the cryptography package to generate keys, and use those keys to encrypt and decrypt files.

## How it works

When launched, the app will ask the user whether to encrypt/decrypt or generate encryption keys. 
When the generate key button is pressed, it will ask the user to select a path and name the key. 
This then generates the encryption key.

Then, for both the encrypt and decrypt options, the key must be selected, and the file to encrypt and decrypt.

## How to Install

1. Get the latest release from [here](https://github.com/SurajApps/Encryptio/releases)
2. Run the below command to install:

``
pip install $FILE
``

Where ``$FILE`` is the latest wheel file from the releases above.

3. Then run the command ``encryptio_gui`` to open the application.