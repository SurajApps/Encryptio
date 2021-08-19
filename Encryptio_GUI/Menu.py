from guizero import App, Text, PushButton, Box, Picture
# import os


def Main_Menu():
    # logo_path = "Encryptio_GUI/res/encryption.png"
    menu_app = App(title="Encrypt.io", width=530, height=150, layout="grid")
    button_box = Box(menu_app, layout="grid", grid=[0, 2])

    def EncryptLaunch():
        from Encryptio_GUI.Encrypt import Encrypt_Menu

    def DecryptLaunch():
        from Encryptio_GUI.Decrypt import Decrypt_Menu

    def KeyGenLaunch():
        from Encryptio_GUI.KeyGen import KeyGen_Menu

    encrypt_button = PushButton(button_box, text="Encrypt Files", grid=[0, 0], command=EncryptLaunch)
    decrypt_button = PushButton(button_box, text="Decrypt Files", grid=[1, 0], command=DecryptLaunch)
    genkey_button = PushButton(button_box, text="Generate Encryption Keys", grid=[2, 0], command=KeyGenLaunch)

    main_title_text = "Welcome to Encrypt.io!"
    main_text = "Use the following buttons to encrypt, decrypt and generate encryption keys."
    main_title = Text(menu_app, text=main_title_text, grid=[0, 0])
    main_text_element = Text(menu_app, text=main_text, grid=[0, 1])

    # front_logo = Picture(menu_app, image=logo_path, grid=[0, 3])
    # print(os.getcwd())
    menu_app.display()


# Main_Menu()
