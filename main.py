import os
import shutil
import re


def accect_remove(text):
    text = re.sub(r'(?i)[ÁÀÂÃ]', 'a', text)
    text = re.sub(r'(?i)[ÉÈÊ]', 'e', text)
    text = re.sub(r'(?i)[ÍÌÎ]', 'i', text)
    text = re.sub(r'(?i)[ÓÒÔÕ]', 'o', text)
    text = re.sub(r'(?i)[ÚÙÛ]', 'u', text)
    text = re.sub(r'(?i)[Ç]', 'c', text)
    return text


def file_duplicator():
    path = input('Digite o caminho da pasta: ')
    os.chdir(path)
    print('Diretório atual: ', os.getcwd())

    dirs = os.listdir()
    folders_count = len(dirs)
    matches = 0
    duplicated = []
    not_duplicated = {}
    already_exists_file = []
    for folder in dirs:
        # folder = pasta com o nome da pessoa
        current_path = path + '\\' + folder
        if os.path.isdir(current_path):
            dir_items = os.listdir(path + '\\' + folder)
            for item in dir_items:
                current_sub_path = current_path + '\\' + item
                # verificar se é um diretorio
                if os.path.isdir(current_sub_path):
                    # verfiricar se o item é uma dessas duas pastas
                    if item in ('RECIBO E SHAPE', 'RECIBO E SHAPEFILE'):
                        current_files = os.listdir(current_sub_path)
                        # itera arquivos da pasta
                        for rsitem in current_files:
                            current_rsitem = current_sub_path + '\\' + rsitem
                            if os.path.isfile(current_rsitem) and current_rsitem.endswith('.kml'):
                                if rsitem not in ('AREA CONSOLIDADA.kml', 'CONSOLIDADA.kml'):
                                    area_consolidada_exists = os.path.exists(current_sub_path + '\\CONSOLIDADA.kml') \
                                        or os.path.exists(current_sub_path + '\\AREA CONSOLIDADA.kml')
                                    if not area_consolidada_exists:
                                        kml = accect_remove(rsitem).removesuffix('.kml').upper()
                                        person_name = accect_remove(folder).upper()

                                        match = re.search(rf"{kml}", person_name)

                                        if match:
                                            matches += 1
                                            try:
                                                print(f'DUPLICANDO {folder}')
                                                duplicated.append(folder)
                                                shutil.copy(current_rsitem,
                                                            current_sub_path + '\\' + 'AREA CONSOLIDADA.kml')
                                            except shutil.SameFileError as e:
                                                print('Erro o arquivo já existe', e)
                                        else:
                                            not_duplicated[f'{folder}'] = 'não tem kml com o nome da pessoa'
                                else:
                                    already_exists_file.append(folder)
                    # não tem pasta 'RECIBO E SHAPE' ou 'RECIBO E SHAPEFILE'
                    else:
                        not_duplicated[f'{folder}'] = "'RECIBO E SHAPE' ou 'RECIBO E SHAPEFILE' não existe"

    print('\n')

    print(f'ARQUIVOS "AREA CONSOLIDADA.kml" EXISTENTES = {len(already_exists_file)}\n')
    for i in already_exists_file:
        print(i)

    print('\n')

    print(f'NÃO DUPLICADOS {len(not_duplicated)}:\n')

    for key in not_duplicated:
        print(f'{key} - {not_duplicated[key]}')

    print('\n')

    print(f'PASTAS {folders_count}')
    print(f'MATCHES {matches}')
    print(f'ARQUIVOS DUPLICADOS =  {len(duplicated)}')



file_duplicator()
