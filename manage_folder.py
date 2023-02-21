import os

def Remake_folder(folder_path):

    if os.path.isdir(folder_path):
        print("Delete old result folder: {}".format(folder_path))
        os.system("rmdir /Q/s {}".format(folder_path))
    
    os.system("mkdir {}".format(folder_path))
    print("create folder: {}".format(folder_path))


def Make_folder(folder_path):

    os.system("mkdir {}".format(folder_path))
    print("create folder: {}".format(folder_path))


def Check_folder(folder_path):

    if os.path.isdir(folder_path) != True:
        Make_folder(folder_path)

