from guizero import App, Text, PushButton, Box, TextBox, info
from cryptography.fernet import Fernet


def Encrypt_Menu():
    key_path = ""
    file_encrypt = ""
    encrypted_path = ""
    key = ""
    original_file = ""
    encrypted_file = ""

    encrypt_app = App(title="Encrypt Files", width=600, height=210, layout="grid")
    key_box = Box(encrypt_app, layout="grid", grid=[0, 1], width="fill")
    file_box = Box(encrypt_app, layout="grid", grid=[0, 2], width="fill")

    title_text = "Use the following buttons to set the Fernet encryption key and the file to be encrypted."
    title = Text(encrypt_app, text=title_text, grid=[0, 0])

    key_textbox = TextBox(key_box, grid=[2, 0], multiline=False, width="fill")
    file_textbox = TextBox(file_box, grid=[2, 0], multiline=False, width="fill")

    def key_file_set():
        nonlocal key_path
        open_title = "Open the Fernet Key file"
        key_path = encrypt_app.select_file(title=open_title, filetypes=[["Fernet Keys", "*.key"]])
        key_textbox.value = key_path
        # print(path_name)

    def encrypt_file_set():
        nonlocal file_encrypt
        open_file_title = "Open the File to Encrypt"
        file_encrypt = encrypt_app.select_file(title=open_file_title, filetypes=[["All Files", "*.*"]])
        file_textbox.value = file_encrypt

    def KeySetup():
        nonlocal key_path, key

        with open(key_path, 'rb') as mykey:
            key = mykey.read()

        FileSetup()

    def FileSetup():
        nonlocal file_encrypt, original_file

        with open(file_encrypt, "rb") as file:
            original_file = file.read()

        EncryptFile()

    def EncryptFile():
        nonlocal key, original_file, encrypted_file, file_encrypt, encrypt_app, encrypted_path
        f = Fernet(key)

        encrypted = f.encrypt(original_file)
        # print(encrypted_file)
        encrypted_path = file_encrypt + ".crypted"
        with open(encrypted_path, 'wb') as save_encrypted:
            encrypted_file = save_encrypted.write(encrypted)

        encrypt_info_text = "The file: " + file_encrypt + " has been encrypted as: " + encrypted_path
        encrypt_info = encrypt_app.info(title="Encryption Successful!", text=encrypt_info_text)

    key_textcontent = "Click the button to set the Fernet key location."
    key_text = Text(key_box, grid=[0, 0], text=key_textcontent)
    key_button = PushButton(key_box, grid=[1, 0], text="Set Key File", command=key_file_set)

    file_textcontent = "Click the button to set the file to encrypt."
    file_text = Text(file_box, grid=[0, 0], text=file_textcontent)
    file_button = PushButton(file_box, grid=[1, 0], text="Set File to Encrypt", command=encrypt_file_set)

    encrypt_button = PushButton(encrypt_app, grid=[0, 3], text="Encrypt File", command=KeySetup)

    encrypt_app.display()


Encrypt_Menu()
