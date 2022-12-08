# //////////////////////////////////////////////////////////////////////////////////////////
#
# BY: Jhonathan Vargas y Jose Martinez
# PROJECT: EnigmaScrypt
# V: 1.0.0
#
# Este projecto se hizo con la finalidad de ser presentado como Projecto semestral
# para la materia de Analsis y diseno de algoritmo impartida por Sharon Saldana
#
# EnigmaEncrypt es un programa enfocado a la codificacion y decodificacion de texto
# con la peculiaridad de que lo hara de una forma diferente dependiendo del dia,
# asemejando el funcionamiento de la 'Maquina Enigma', de ahi el nombre.
#
# //////////////////////////////////////////////////////////////////////////////////////////

# IMPORTANDO MODULOS

import string
import random


#ESTE CODIGO SE USO PARA GENERAR LOS 31 DICCIONARIOS QUE SE EMPLEARAN PARA ENCRIPTAR/DECRIPTAR
a = ['a','b','c','d','e','f','g','h','i','j'
    ,'k','l','m','n','ñ','o','p','q','r','s',
    't','u','v','w','x','y','z',' ','.',',',
    ';','_','-','/','(',')','?','¿']

d = []

number_of_strings = len(a)
length_of_string = 3
for i in range(31):
    c = '{'
    for x in range(number_of_strings):
        b="'"+a[x]+"'"+":"+"'"+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string))+"',"
        c = c+b.lower()
    c=c+'}'
    d.append(c)

print(d)
