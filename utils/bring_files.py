import os

def bring_files(data, window):
    folder = data
    file_list = os.listdir(folder)
    fnames = [
        f
        for f in file_list
        if os.path.isfile(os.path.join(folder, f))
        and f.lower().endswith(('.mp3', '.m4a', '.wma','.aac', '.wmv', '.flac'))
    ]
    window["-FILE LIST-"].update(fnames)
    return True, file_list