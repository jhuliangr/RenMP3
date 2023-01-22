import eyed3
import PySimpleGUI as sg
import os

file_list_column = [
    [
        sg.Text("Directorio de Musica"),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse('Buscar', s=(10,1))
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 20),
            key="-FILE LIST-"
        ),sg.Text(),
        sg.Button('Renombrar todo', size=(12,2))
    ]
]

layout = [
    [
        sg.Column(file_list_column)
    ]
]

window = sg.Window("Renombrador de Musica", layout)

archivoSeleccionado = False
array = []
def traer_archivos():
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

def etiquetas(song, directorio):        
    f = eyed3.load(os.path.join(directorio, song))
    if f.tag != None:
        if  f.tag.title == 'EJE RECORD [53639408]':
            f.tag.title = ''
            print('etiquetas titulo guardadas')
        if  f.tag.album == 'EJE RECORD [53639408]':
            f.tag.album = ''
            print('etiquetas album guardadas')
        if  f.tag.artist == 'EJE RECORD [53639408]':
            f.tag.artist = ''
            print('etiquetas artista guardadas')
        f.tag.save()   

basura = [' (Www.FlowHot.Net)',' (Dj Ubi)', '(Xtreme 48-75-87-36)', ' (Www.FlowHoT.NeT)','(www.AbdelLaEsenciayEstudiosOdisea.com)', '(Abdel La Esencia Y Estudios Odisea)', ' (FlowActivo.Com)', '(Abdel La Esencia)', ' (WwW.BaniCrazy.NeT)']
#implementar funcion para que cuando de doble click en una cancion se abra...
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == "-FOLDER-":
        archivoSeleccionado, array = traer_archivos()
        
        
    if event == 'Renombrar todo':
        if not archivoSeleccionado:
            emergente = sg.Window(title="Continuar",
                   layout=[[sg.Text('Debe seleccionar un directorio para poder hacer uso del programa')],
                           [sg.Text('')],
                           [sg.Text('                                    '), sg.Button('Ok', s=(6,1))]],
                   margins=(10, 10))
            while True:
                event, values = emergente.read()
                if event == "Ok" or event == sg.WIN_CLOSED:
                    break
            emergente.close()
            #sustituir esto por un button disable...
        elif array == []:
            emergente = sg.Window(title="Continuar",
                   layout=[[sg.Text('El directorio seleccionado está completamente vacío')],
                           [sg.Text('')],
                           [sg.Text('                             '), sg.Button('Ok', s=(6,1))]],
                   margins=(10, 10))
            while True:
                event, values = emergente.read()
                if event == "Ok" or event == sg.WIN_CLOSED:
                    break
            emergente.close()
        else:
            directorio = values["-FOLDER-"]
            content = os.listdir(directorio)
            for song in content:
                if not os.path.isfile(os.path.join(directorio, song)) or not song.lower().endswith(('.mp3', '.m4a', '.wma','.aac', '.wmv', '.flac')):
                    continue
                work = True
                for promocion in basura:
                    if promocion in song: 
                        # temp.replace('(www.AbdelLaEsenciayEstudiosOdisea.com)', '') #no esta funcionando.. pide ayuda
                        temp = song[:song.find(promocion)]
                        if(song[-5]=='.'):
                            temp+='.flac'
                        else:
                            temp += song[-4:]
                        os.rename(os.path.join(directorio, song), os.path.join(directorio, temp))
                        song = temp
                temporal = ''
                cond = True #
                # if song.lower().endswith(('.mp3')):
                #     etiquetas(song, directorio)                                                 
                
                if song[0]>='0' and song[0]<='9':
                    for j in song:
                        if ((j>='0' and j<='9') or j == ' ' or j == '-' or j == '.') and cond:
                            continue
                        else:
                            cond = False
                            temporal+=j
                

                if cond == False:
                    os.rename(os.path.join(directorio, song), os.path.join(directorio, temporal))
                    
            #poner un mensaje emergente que diga que ha sido hecho con exito el renombramiento...
            emergente = sg.Window(title="Continuar",
                layout=[[sg.Text('La música ha sido renombrada con éxito')],
                        [sg.Text('')],
                        [sg.Text('                       '), sg.Button('Ok', s=(6,1))]],
                margins=(10, 10))
            while True:
                event, val = emergente.read()
                if event == "Ok" or event == sg.WIN_CLOSED:
                    break
            emergente.close()
            traer_archivos()
            #poner el nombre del artista en la propiedad nombre de artista y el titulo en el titulo
            #eliminar flowhot, el transportador, abdel la escencia... etc
        
        
        
        
    elif event == "-FILE LIST-":
        try:
            filename = os.path.join(
                values["-FOLDER-"], values["-FILE LIST-"][0]
            )
        except:
            pass
        
window.close()


# f = eyed3.load(file)
#         filecito=file.replace("yt1s.com - ","")
#         ficherito=filecito.replace(".mp3","")
#         f.tag.title = ficherito
#         fichier=ficherito.split()
#         f.tag.artist= fichier[0]+" "+fichier[1]
#         f.tag.album="name_album"
#         f.tag.save()
#         os.rename(file, file.replace("yt1s.com - ",""))