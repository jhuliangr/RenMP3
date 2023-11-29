import os


def get_rid_of_promotions(directory, song, promocion):
    if promocion in song: 
        temp = song[:song.find(promocion)]
        if(song[-5]=='.'):
            temp+='.flac'
        else:
            temp += song[-4:]
        os.rename(os.path.join(directory, song), os.path.join(directory, temp))
        return temp
    else:
        return song
    
def get_rid_of_track_numbers(song, temp, cond):
    if song[0]>='0' and song[0]<='9':
        for j in song:
            if ((j>='0' and j<='9') or j == ' ' or j == '-' or j == '.') and cond:
                continue
            else:
                cond = False
                temp+=j
        return False, temp
    else:
        return cond, temp