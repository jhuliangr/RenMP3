import eyed3
import PySimpleGUI as sg
import os

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
        sg.Button('Rename it all', size=(12,2))
    ]
]
layout = [
    [
        sg.Column(file_list_column)
    ]
]

window = sg.Window("Music Renamer", layout)

archivoSeleccionado = False
array = []
def bring_files():
    folder = values["-FOLDER-"]
    file_list = os.listdir(folder)
    fnames = [
        f
        for f in file_list
        if os.path.isfile(os.path.join(folder, f))
        and f.lower().endswith(('.mp3', '.m4a', '.wma','.aac', '.wmv', '.flac'))
    ]
    window["-FILE LIST-"].update(fnames)
    return True, file_list

# not yet used
# def etiquetas(song, directory):        
#     f = eyed3.load(os.path.join(directory, song))
#     if f.tag != None:
#         if  f.tag.title == 'EJE RECORD [53639408]':
#             f.tag.title = ''
#         if  f.tag.album == 'EJE RECORD [53639408]':
#             f.tag.album = ''            
#         if  f.tag.artist == 'EJE RECORD [53639408]':
#             f.tag.artist = ''
            
#         f.tag.save()   

pirate_music_providers = [' (Www.FlowHot.Net)','{HD Studios}','(CrazY_BoyZ)',' (Dj Ubi)', '(Xtreme 48-75-87-36)', ' (Www.FlowHoT.NeT)','(www.AbdelLaEsenciayEstudiosOdisea.com)', '(Abdel La Esencia Y Estudios Odisea)', ' (FlowActivo.Com)', '(Abdel La Esencia)', ' (WwW.BaniCrazy.NeT)']
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == "-FOLDER-":
        selected_file, array = bring_files()
        
        
    if event == 'Rename it all':
        if not selected_file:
            msg_window = sg.Window(title="msg window",
                   layout=[[sg.Text('You must select a directory for using the program')],
                           [sg.Text('')],
                           [sg.Text('                                    '), sg.Button('Ok', s=(6,1))]],
                   margins=(10, 10))
            while True:
                event, values = msg_window.read()
                if event == "Ok" or event == sg.WIN_CLOSED:
                    break
            msg_window.close()
            # make a disable for not having to use this
        elif array == []:
            msg_window = sg.Window(title="msg window",
                   layout=[[sg.Text('The actual directory is empty')],
                           [sg.Text('')],
                           [sg.Text('                             '), sg.Button('Ok', s=(6,1))]],
                   margins=(10, 10))
            while True:
                event, values = msg_window.read()
                if event == "Ok" or event == sg.WIN_CLOSED:
                    break
            msg_window.close()
        else:
            directory = values["-FOLDER-"]
            content = os.listdir(directory)
            for song in content:
                if not os.path.isfile(os.path.join(directory, song)) or not song.lower().endswith(('.mp3', '.m4a', '.wma','.aac', '.wmv', '.flac')):
                    continue
                
                for promocion in pirate_music_providers:
                    if promocion in song: 
                        # temp.replace('(www.AbdelLaEsenciayEstudiosOdisea.com)', '')
                        temp = song[:song.find(promocion)]
                        if(song[-5]=='.'):
                            temp+='.flac'
                        else:
                            temp += song[-4:]
                        os.rename(os.path.join(directory, song), os.path.join(directory, temp))
                        song = temp
                temp = ''
                cond = True                                                
                if song[0]>='0' and song[0]<='9':
                    for j in song:
                        if ((j>='0' and j<='9') or j == ' ' or j == '-' or j == '.') and cond:
                            continue
                        else:
                            cond = False
                            temp+=j
                    
                

                if cond == False:
                    if temp in content:
                        temp+=' to erase'
                    os.rename(os.path.join(directory, song), os.path.join(directory, temp))
                    # print(os.path.join(directory, song),' con -> ',os.path.join(directory, temp))
                    
            
            msg_window = sg.Window(title="Msg window",
                layout=[[sg.Text('your music has been renamed successfully :D')],
                        [sg.Text('')],
                        [sg.Text('                       '), sg.Button('Ok', s=(6,1))]],
                margins=(10, 10))
            while True:
                event, val = msg_window.read()
                if event == "Ok" or event == sg.WIN_CLOSED:
                    break
            msg_window.close()
            bring_files()
            
        
        
    elif event == "-FILE LIST-":
        try:
            filename = os.path.join(
                values["-FOLDER-"], values["-FILE LIST-"][0]
            )
        except:
            pass
        
window.close()

#crear excepcion para cuando hay un archivo con el mismo nombre de uno procesado




# f = eyed3.load(file)
#         filecito=file.replace("yt1s.com - ","")
#         ficherito=filecito.replace(".mp3","")
#         f.tag.title = ficherito
#         fichier=ficherito.split()
#         f.tag.artist= fichier[0]+" "+fichier[1]
#         f.tag.album="name_album"
#         f.tag.save()
#         os.rename(file, file.replace("yt1s.com - ",""))

# implement a double click event for songs to open them
