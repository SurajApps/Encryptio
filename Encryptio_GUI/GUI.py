from guizero import App, Box, PushButton, TextBox, Text, Picture
import os


app = App(title="Encryptio", width=540, height=640, layout="grid")
buttton_box = Box(app, layout="grid", grid=[0,1])

message = Text(app, text="Welcome to Encryptio!", grid=[0, 0])

encrypt_button = PushButton(master=buttton_box, text="Encrypt File", grid=[0, 0])
decrypt_button = PushButton(master=buttton_box, text="Decrypt File", grid=[1, 0])
generate_button = PushButton(master=buttton_box, text="Generate Encryption Key", grid=[2, 0])

front_picture = Picture(app, image="Encryptio_GUI/res/encryption.png", grid=[0, 2])


def encrypt_action():
    print("Encrypt")


def Decrypt_Action():
    print("Decrypt")


def GenerateKey_Action():
    print("Generate Key")


print(os.getcwd())

app.display()
