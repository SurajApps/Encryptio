from guizero import App, Text, PushButton, Box, TextBox
from cryptography.fernet import Fernet


def KeyGen_Menu():
    keygen_app = App(title="Generate Encryption Key", width=1000, height=500, layout="grid")
    path_box = Box(keygen_app, layout="grid", grid=[0, 1])
    keygen_box = Box(keygen_app, layout="grid", grid=[0, 2])
    key_name = ""
    path_name = ""
    temp_space = ""
    complete_key_location = ""

    title_text = "Use the following options to setup a Fernet key in your chosen location."
    title = Text(keygen_app, text=title_text, grid=[0, 0])

# Keygen stuff
    name_text = Text(keygen_box, grid=[0, 0], text="Set the Name of the Key:")
    name_box = TextBox(keygen_box, grid=[1, 0], multiline=False, width="fill")

    def key_name_change():
        nonlocal name_box, key_name
        key_name = name_box.value
        print(key_name)

    name_box.update_command(key_name_change)
    # name_select = PushButton(keygen_box, text="Set Key Name", grid=[2, 0], command=key_name_change)
    backslash = '''/'''

    def CreateKeyPath():
        nonlocal key_name, path_name, complete_key_location
        complete_key_location = path_name + backslash + key_name
        GenerateFernetKey()

    def GenerateFernetKey():
        key = Fernet.generate_key()

        with open(complete_key_location, 'wb') as mykey:
            mykey.write(key)

        print(key)

    key_detail_set = PushButton(keygen_box, text="Generate Fernet Key", grid=[3, 0], command=CreateKeyPath)
# Path Stuff

    def key_path_set():
        nonlocal path_name, keygen_app
        path_name = keygen_app.select_folder()
        path_select_box.value = path_name
        print(path_name)

    path_select = PushButton(path_box, text="Select Key Path", grid=[2, 0], command=key_path_set, align="right")
    path_select_box = TextBox(path_box, grid=[1, 0], multiline=False, width="fill", align="left")
    path_select_text = Text(path_box, grid=[0, 0], text="Set the Path of the key using the button:")

    keygen_app.display()


KeyGen_Menu()
