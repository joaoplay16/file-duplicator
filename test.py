import re
texto = 'FRANCISCA DA SILVA SOUZA'
# pattern = re.compile(r'{texto}')
#
# print(pattern.match('JDOAIS') != None)
txt = "The rain in Spain"
x = re.search(rf"{texto}", 'FRANCISCA DA SILVA SOUZA - SITIO SOUZA')

print(x)