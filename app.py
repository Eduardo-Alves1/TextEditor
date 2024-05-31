import PySimpleGUI as sg

menu_def = [["Arquivo", ["Abrir", "&Salvar", "Novo"]]]

layout = [
    [sg.Multiline(key="-MULT-", size=(80, 20))],
    [sg.Menu(menu_def, text_color="black")],
    [sg.Text(size=12, font="Helvetica")],
]

window = sg.Window("Text Editor", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == "Salvar":
        filename = sg.popup_get_file("Salvar", save_as=True, default_extension=".txt")
        if filename:
            with open(filename, "w") as arquivo:
                arquivo.write(values["-MULT-"])

    elif event == "Novo":
        window["-MULT-"].update("")
        filename = None

    elif event == "Abrir":
        new_filename = sg.popup_get_file("Abrir", default_extension=".txt")
        if new_filename:
            try:
                with open(new_filename, "r") as arquivo:
                    window["-MULT-"].update(arquivo.read())
                filename = new_filename
            except Exception as e:
                sg.popup_error(f"Erro ao abrir o arquivo {e}")

window.close()
