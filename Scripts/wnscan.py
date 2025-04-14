#!/usr/bin/env python3
import subprocess

objective = input("Indique la ip objetivo \n")

file_bool = False

while True:
    file_output = input("¿Desea almacenar los resultados en un archivo? (Y/N) \n")

    if file_output.casefold()=='y':
        file_bool=True
        break
    elif file_output.casefold()=='n':
        file_bool=False
        break


    else: print('Opcion no valida \n')  

if file_bool==True:
    subprocess.call(['nmap', '-Pn', '-sC', '-sV', '-p-', objective, '--min-rate', "5000", '-v', '-oN', 'Wnscan-Out'])

    print('\n ---»Se creo un archivo con el nombre Wnscan-Out')

else: subprocess.call(['nmap', '-Pn', '-sC', '-sV', '-p-' ,objective, '--min-rate', "5000", '-v'])

