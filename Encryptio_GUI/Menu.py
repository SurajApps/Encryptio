from guizero import App, Text, PushButton, Box, Picture


def Main_Menu():
    menu_app = App(title="Encrypt.io", width=500, height=500, layout="grid")
    button_box = Box(menu_app, layout="grid", grid=[0, 2])

    def EncryptLaunch():
        from Encrypt import Encrypt_Menu

    encrypt_button = PushButton(button_box, text="Encrypt Files", grid=[0, 0], command=EncryptLaunch)
    decrypt_button = PushButton(button_box, text="Decrypt Files", grid=[1, 0])
    genkey_button = PushButton(button_box, text="Generate Encryption Keys", grid=[2, 0])

    main_title_text = "Welcome to Encrypt.io!"
    main_text = "Use the following buttons to encrypt, decrypt and generate encryption keys."
    main_title = Text(menu_app, text=main_title_text, grid=[0, 0])
    main_text_element = Text(menu_app, text=main_text, grid=[0, 1])

    front_logo_path = "Encryptio_GUI/res/encryption.png"
    front_logo = Picture(menu_app, image=front_logo_path, grid=[0, 3])

    menu_app.display()


Main_Menu()
