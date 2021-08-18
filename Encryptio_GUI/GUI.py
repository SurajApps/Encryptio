import os
from guizero import App, Box, PushButton, Text, Picture, Window


def main_GUI():
    main_app = App(title="Encryptio", width=540, height=640, layout="grid")
    buttton_box = Box(main_app, layout="grid", grid=[0, 1])

    message = Text(main_app, text="Welcome to Encryptio!", grid=[0, 0])

    def action_encrypt():
        encrypt_window = Window(main_app)
        main_app.display()
        # print("Encrypt")

    def action_decrypt():
        print("Decrypt")

    def action_generatekey():
        print("Generate Encryption Key")

    encrypt_button = PushButton(master=buttton_box, text="Encrypt File", grid=[0, 0], command=action_encrypt)
    decrypt_button = PushButton(master=buttton_box, text="Decrypt File", grid=[1, 0], command=action_decrypt)
    generate_button = PushButton(master=buttton_box, text="Generate Encryption Key", grid=[2, 0], command=action_generatekey)

    front_picture = Picture(main_app, image="Encryptio_GUI/res/encryption.png", grid=[0, 2])

    print(os.getcwd())
    main_app.display()


main_GUI()
