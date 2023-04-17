#!/usr/bin/env python3
#author: Hans saldias
#practica scrip sencillos
from colorama import init, Fore, Back, Style
print(Fore.YELLOW+
'''
88b 88  dP"Yb  8888b.   dP"Yb      888888 Yb  dP 888888
88Yb88 dP   Yb  8I  Yb dP   Yb       88    YbdP    88
88 Y88 Yb   dP  8I  dY Yb   dP .o.   88    dPYb    88
88  Y8  YbodP  8888Y"   YbodP  `"'   88   dP  Yb   88
\n''')
print(Fore.GREEN+'''
Este scrip es sencillo solo para crear archivos.txt, para guardar info o listas de password para hacking etc.
create by: Hans Saldias\n''')
print(Fore.BLUE+"=-="*20)
nombre = input(Fore.RED+"¿Cual es tu nombre?: ")
print(Fore.BLUE+'\n'+"=-="*20)

while True:
	archivo=open("HackerNoDo.txt",'a')
	archivo.write("\n"+(input(Fore.RED+f"{nombre}, Ingresa datos a guardar: ")))
	archivo.close()
	print(Fore.GREEN+f"{nombre} el archivo tiene el nombre de HackerNoDo.txt esta en la memoria interna del equipo o donde tienes guardado el scrip...Gracias ")  
	print("para salir de escribir (ctr + z osino + c)")
	

		
	

