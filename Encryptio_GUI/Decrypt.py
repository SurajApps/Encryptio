from guizero import App, Text, PushButton, Box, TextBox, info
from cryptography.fernet import Fernet
import os


def Decrypt_Menu():

    key_path = ""
    file_decrypt = ""
    decrypted_path = ""

    key = ""
    original_file = ""
    decrypted_file = ""

    finalpath = ""

    decrypt_app = App(title="Decrypt Files", width=600, height=210, layout="grid")
    key_box = Box(decrypt_app, layout="grid", grid=[0, 1], width="fill")
    file_box = Box(decrypt_app, layout="grid", grid=[0, 2], width="fill")

    title_text = "Use the following buttons to set the Fernet encryption key and the file to be decrypted."
    title = Text(decrypt_app, text=title_text, grid=[0, 0])

    key_textbox = TextBox(key_box, grid=[2, 0], multiline=False, width="fill")
    file_textbox = TextBox(file_box, grid=[2, 0], multiline=False, width="fill")

    def key_file_set():
        nonlocal key_path
        open_title = "Open the Fernet Key file"
        key_path = decrypt_app.select_file(title=open_title, filetypes=[["Fernet Keys", "*.key"]])
        key_textbox.value = key_path
        # print(path_name)

    def decrypt_file_set():
        nonlocal file_decrypt
        open_file_title = "Open the File to Decrypt"
        file_decrypt = decrypt_app.select_file(title=open_file_title, filetypes=[["Crypted Files", "*.crypted"]])
        file_textbox.value = file_decrypt

    def KeySetup():
        nonlocal key_path, key

        with open(key_path, 'rb') as mykey:
            key = mykey.read()

        FileSetup()

    def FileSetup():
        nonlocal file_decrypt, original_file, decrypted_path

        with open(file_decrypt, "rb") as file:
            original_file = file.read()

        if file_decrypt.__contains__(".crypted"):
            decrypted_path = os.path.splitext(file_decrypt)[0]

        DecryptFile()

    def DecryptFile():
        nonlocal key, original_file, decrypted_file, file_decrypt, decrypt_app, decrypted_path, finalpath
        f = Fernet(key)

        decrypted = f.decrypt(original_file)
        # print(encrypted_file)
        with open(decrypted_path, 'wb') as save_decrypted:
            decrypted_file = save_decrypted.write(decrypted)

        decrypt_info_text = "The file: " + file_decrypt + " has been decrypted as: " + decrypted_path
        decrypt_info = decrypt_app.info(title="Decryption Successful!", text=decrypt_info_text)

    key_textcontent = "Click the button to set the Fernet key location."
    key_text = Text(key_box, grid=[0, 0], text=key_textcontent)
    key_button = PushButton(key_box, grid=[1, 0], text="Set Key File", command=key_file_set)

    file_textcontent = "Click the button to set the file to decrypt."
    file_text = Text(file_box, grid=[0, 0], text=file_textcontent)
    file_button = PushButton(file_box, grid=[1, 0], text="Set File to decrypt", command=decrypt_file_set)

    encrypt_button = PushButton(decrypt_app, grid=[0, 3], text="Decrypt File", command=KeySetup)

    decrypt_app.display()


Decrypt_Menu()
