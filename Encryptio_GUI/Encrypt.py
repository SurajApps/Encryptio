from guizero import App, Text, PushButton, Box, TextBox
from cryptography.fernet import Fernet

def Encrypt_Menu():
    key_path = ""
    file_encrypt = ""
    key = ""
    original_file = ""
    encrypted_file = ""

    encrypt_app = App(title="Encrypt Files", width=500, height=500, layout="grid")
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

    def FileSetup():
        nonlocal key_path, file_encrypt, key, original_file

        with open(key_path, 'rb') as mykey:
            key = mykey.read()
        return key

        f = Fernet(key)




    key_textcontent = "Click the button to set the Fernet key location."
    key_text = Text(key_box, grid=[0, 0], text=key_textcontent)
    key_button = PushButton(key_box, grid=[1, 0], text="Set Key File", command=key_file_set)

    file_textcontent = "Click the button to set the file to encrypt."
    file_text = Text(file_box, grid=[0, 0], text=file_textcontent)
    file_button = PushButton(file_box, grid=[1, 0], text="Set File to Encrypt", command=encrypt_file_set)

    encrypt_app.display()


Encrypt_Menu()
