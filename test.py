import re
import math
import os
texto = 'FRANCISCA DA SILVA SOUZA'
# pattern = re.compile(r'{texto}')
#
# print(pattern.match('JDOAIS') != None)
txt = "The rain in Spain"
x = re.search(rf"{texto}", 'FRANCISCA DA SILVA SOUZA - SITIO SOUZA')

# print(x)

a = ['de', 'freitas']
b = ['joao', 'pedro', 'de', 'freitas']

c = [x for x in a if x in b]

print(f'len a = {len(a)}, len b = {len(b)}, len c = {len(c)} len a / 2 = {len(b) / 2}')

# print(len(c) >= len(b) / 2)

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
    result = [x for x in person_name if x in kml_name]
    if len(kml_name) > len(person_name):
        print('if\n ',len(result) >= math.ceil(len(kml_name) / 2))

    else:
        print('else =', len(result) >= math.floor(len(person_name) / 2))
        print(f'len result = {len(result)}, len person_name = {math.floor(len(person_name) / 2)}')


# print(compare_names('joao .kml', 'joao pedro de freitas brito'))

print(os.path.isdir("C:\\Users\joao\Desktop\CORREÇAO DE IMAGEM\REGIONAL BACABAL\VITORINO FREIRE\JUÇARAL DO SARAIVA\ANTONIO CARLOS SOUSA DA CONCEIÇÃO\RECIBO E SHAPEFILES"))