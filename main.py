import os
import shutil
import re
import math


def accect_remove(text):
    text = re.sub(r'(?i)[ÁÀÂÃ]', 'a', text)
    text = re.sub(r'(?i)[ÉÈÊ]', 'e', text)
    text = re.sub(r'(?i)[ÍÌÎ]', 'i', text)
    text = re.sub(r'(?i)[ÓÒÔÕ]', 'o', text)
    text = re.sub(r'(?i)[ÚÙÛ]', 'u', text)
    text = re.sub(r'(?i)[Ç]', 'c', text)
    return text


def normalize_names(kml='', person_name=''):
    kml = accect_remove(kml).removesuffix('.kml').upper()
    person_name = accect_remove(person_name).upper()
    return {'kml': kml, 'person_name': person_name}


def compare_names(kml_name, person_name):
    kml_name = normalize_names(kml_name)['kml'].split()
    person_name = normalize_names('_', person_name)['person_name'].split()
    result = [x for x in kml_name if x in person_name]
    if len(kml_name) > len(person_name):
        return len(result) >= math.floor(len(kml_name) / 2)
    else:
        return len(result) >= math.floor(len(person_name) / 2)


def folder_exists(folder):
    return os.path.isdir(folder)


def is_area_consolidada(file):
    file = file.removesuffix('.kml')
    result = re.search(r'^(AREA)|\s*(CONSOLIDADA).*', file)
    return result != None


def is_recibo(folder):
    result = re.search(r'^RECIBO\s*E.*', folder)
    return result != None


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
            dir_items = os.listdir(current_path)
            dir_items = [x for x in dir_items if folder_exists(current_path + f'\\{x}') and is_recibo(x)]
            if(len(dir_items) > 0):
                for item in dir_items:
                    current_sub_path = current_path + '\\' + item
                    # verfiricar se o item é uma dessas duas pastas
                    if is_recibo(item):

                        current_files = os.listdir(current_sub_path)
                        # itera arquivos da pasta

                        area_consolidada_files = [x for x in current_files if is_area_consolidada(x)]

                        person_kml_found = 0
                        if len(area_consolidada_files) == 0:
                            for file in current_files:
                                current_rsitem = current_sub_path + '\\' + file
                                kml = normalize_names(file, folder)['kml']
                                person_name = normalize_names(file, folder)['person_name']

                                # match = re.search(rf"{kml}", person_name)
                                match = compare_names(kml, person_name)

                                if match:
                                    matches += 1
                                    person_kml_found += 1
                                    try:
                                        print(f'DUPLICANDO {kml}')
                                        duplicated.append(folder)
                                        shutil.copy(current_rsitem,
                                                    current_sub_path + '\\' + 'AREA CONSOLIDADA.kml')
                                    except shutil.SameFileError as e:
                                        print('Erro o arquivo já existe', e)
                                if person_kml_found == 0:
                                    not_duplicated[f'{folder}'] = 'não tem kml com o nome da pessoa'

                        else:
                            already_exists_file.append(folder)

                    # não tem pasta 'RECIBO E SHAPE' ou 'RECIBO E SHAPEFILE'
            else:
                not_duplicated[folder] = "'RECIBO E SHAPE' ou 'RECIBO E SHAPEFILE' não existe"

    print('\n')

    print(f'ARQUIVOS "AREA CONSOLIDADA.kml" EXISTENTES = {len(already_exists_file)}\n')
    for i in already_exists_file:
        print(i)

    print('\n')

    print(f'NÃO DUPLICADOS = {len(not_duplicated)}\n')

    for key in not_duplicated:
        print(f'{key} - {not_duplicated[key]}')

    print('\n')

    print(f'PASTAS {folders_count}')
    #print(f'MATCHES {matches}')
    print(f'ARQUIVOS DUPLICADOS =  {len(duplicated)}')


file_duplicator()
#print(is_area_consolidada('REPRESA ARTIFICIAL.kml'))
