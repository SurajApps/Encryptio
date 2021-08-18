from guizero import App, Text, PushButton, Box, TextBox


def Encrypt_Menu():
    key_path = ""
    file_encrypt = ""

    encrypt_app = App(title="Encrypt Files", width=500, height=500, layout="grid")
    key_box = Box(encrypt_app, layout="grid", grid=[0, 1])
    file_box = Box(encrypt_app, layout="grid", grid=[0, 2])

    title_text = "Use the following buttons to set the Fernet encryption key and the file to be encrypted."
    title = Text(encrypt_app, text=title_text, grid=[0, 0])

    key_textbox = TextBox(key_box, grid=[0, 2], multiline=False)

    def key_file_set():
        nonlocal key_path
        open_title = "Open the Fernet Key file"
        key_path = encrypt_app.select_file(title=open_title, filetypes=[["All Files", "*.*"], ["Fernet Keys", "*.key"]])
        key_textbox.value = key_path
        # print(path_name)

    key_textcontent = "Click the button to set the Fernet key location."
    key_text = Text(key_box, grid=[0, 0], text=key_textcontent)
    key_button = PushButton(key_box, grid=[0, 1], text="Set Key File", command=key_file_set)

    encrypt_app.display()


Encrypt_Menu()
