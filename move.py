import os
import shutil
import re


def folder_exists(folder):
    return os.path.isdir(folder)


def is_recibo(folder):
    result = re.search(r'^RECIBO\s*E.*', folder)
    return result != None


def file_move():
    path = input('MOVE: Digite o diretorio: ')
    os.chdir(path)
    print('Diretório atual: ', os.getcwd())

    dirs = os.listdir()
    folders_count = len(dirs)
    move_count = 0
    not_moved = []
    for folder in dirs:
        # folder = pasta com o nome da pessoa
        current_path = path + '\\' + folder
        if os.path.isdir(current_path):
            dir_items = os.listdir(current_path)
            dir_items = [x for x in dir_items if folder_exists(current_path + f'\\{x}') and is_recibo(x)]

            for item in dir_items:
                current_sub_path = current_path + '\\' + item
                print(item)
                # verificar se é um diretorio

                current_files = os.listdir(current_sub_path)
                # itera arquivos da pasta

                for rsitem in current_files:
                    current_rsitem = current_sub_path + '\\' + rsitem
                    print(f'movendo - {rsitem}')
                    try:
                        shutil.move(current_rsitem, folder)
                    except shutil.SameFileError as e:
                        print('Exception ',e)
                move_count += 1
                os.rmdir(current_sub_path)

    print('movidos ', move_count)

    if not_moved:
        print('\nNão movido\n')
        for i in not_moved:
            print(i)


file_move()
