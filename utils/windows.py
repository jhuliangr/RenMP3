import PySimpleGUI as sg

def Layout():
    button =  sg.Button('Rename it all', size=(12,2))

    file_list_column = [
        [
            sg.Text("Music Directory"),
            sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
            sg.FolderBrowse('Search', s=(10,1))
        ],
        [
            sg.Listbox(
                values=[], enable_events=True, size=(40, 20),
                key="-FILE LIST-"
            ),sg.Text(),
           button
        ]
    ]
    layout = [
        [
            sg.Column(file_list_column)
        ]
    ]
    return sg.Window("Music Renamer", layout)

def Alert(title, text):
    return sg.Window(title=title,
                    layout=[[sg.Text(text)],
                            [sg.Text('')],
                            [sg.Text('                                    '), sg.Button('Ok', s=(6,1))]],
                    margins=(10, 10))