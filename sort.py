import os,shutil
folder={
    'videos':['.mp4'],
    'audios':['.wav','.mp3'],
    'images':['.jpj','.png'],
    'document':['.doc','.xlsx','.xls','.pfd','.zip','.rar'],
}

def rename_folder():
    for folder in os.listdir(dicrectory):
        if os.path.isdir(os.path.join(dicrectory,folder))==True:
            os.rename(os.path.join(dicrectory,folder),os.path.join(dicrectory,folder.lower()))


def create_move(ext,file_name):
    find=False
    for folder_name in folder: 
        if '.'+ext in folder[folder_name]:
            if folder_name not in os.listdir(dicrectory):
                os.mkdir(os.path.join(dicrectory,folder_name))
            shutil.move(os.path.join(dicrectory,file_name),os.path.join(dicrectory,folder_name))
            find=True
            break
            
    if find!=True:
        if other_name not in os.listdir(dicrectory):
            os.mkdir(os.path.join(dicrectory,other_name))
        shutil.move(os.path.join(dicrectory,file_name),os.path.join(dicrectory,other_name))

            





dicrectory= input('enter the location:')
other_name=input('enter the folder name for Unkown file')
rename_folder()
all_files=os.listdir(dicrectory)
for i in all_files:
    if os.path.isfile(os.path.join(dicrectory,i))==True:
        create_move(i.split('.')[-1],i)

