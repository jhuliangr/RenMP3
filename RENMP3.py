import PySimpleGUI as sg
import os
from utils.bring_files import bring_files
from utils.functions import *
from utils.windows import *
from utils.constants import *

selected_file = False
WINDOW = Layout()
array = []


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

while True:
    event, values = WINDOW.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == "-FOLDER-":
        selected_file, array = bring_files(values['-FOLDER-'], WINDOW)
        
    if event == 'Rename it all':
        if not selected_file:
            msg_window = Alert("Alert", 'You must select a directory for using the program')
            while True:
                event, values = msg_window.read()
                if event == "Ok" or event == sg.WIN_CLOSED:
                    break
            msg_window.close()
            
        elif array == []:
            msg_window = Alert("Alert", 'The actual directory is empty')
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
                
                for promocion in PIRATE_MUSIC_PROVIDERS:
                    song = get_rid_of_promotions(directory, song, promocion)
                temp = ''
                cond = True   
                cond, temp = get_rid_of_track_numbers(song, temp, cond)                                            
                    
                if cond == False:
                    if temp in content:
                        temp+=' to erase'
                    os.rename(os.path.join(directory, song), os.path.join(directory, temp))
                    
            
            msg_window = Alert("Success",'Your music has been renamed successfully :D' )
            while True:
                event, val = msg_window.read()
                if event == "Ok" or event == sg.WIN_CLOSED:
                    break
            msg_window.close()
            bring_files(values['-FOLDER-'], WINDOW)
            
        
        
    elif event == "-FILE LIST-":
        try:
            filename = os.path.join(
                values["-FOLDER-"], values["-FILE LIST-"][0]
            )
        except:
            pass
        
WINDOW.close()

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
