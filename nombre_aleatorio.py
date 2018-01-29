import string
import random
from colorama import init, Fore
import time

# Inicia colorama
init()

letras = string.ascii_lowercase
vocales = "aeiou"
consonantes = "bcdfghjklmnpqrstvwxyz"

def generador(numero_de_letras):
	nombre = ""
	es_vocal = False
	cOv = random.choice([0,1])
	# Generador aleatorio de la primera letra
	if(cOv):
		nombre += random.choice(vocales).upper()
		es_vocal = True
	else:
		nombre += random.choice(consonantes).upper()
		
	# Generador del resto de letras
	print(nombre)
	for x in range(0, numero_de_letras-1):
		if(es_vocal):
			nombre += random.choice(consonantes)
			es_vocal = False
		else:
			nombre += random.choice(vocales)
			es_vocal = True
		print(nombre)
		time.sleep(0.8)
	print(Fore.RED + nombre)
print("----MadreNodriza----")
print("Inserta el numero de letras para el nombre.")
generador(int(input()))
