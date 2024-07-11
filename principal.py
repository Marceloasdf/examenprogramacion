import random,os,csv
from funciones import *
trabajadores = ["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]
while True:
    print("""menu datos de trabajadores
        1) Asignar sueldos aleatorios
        2) Clasificar sueldos
        3) Ver estadisticas
        4) Reporte de sueldos
        5) Salir del programa""")
    opc=validaropc([1,2,3,4,5])
    if opc==1:
        opcion1()
    elif opc==2:
        opcion2()
    elif opc==3:
        opcion3()
    elif opc==4:
        opcion4()
    elif opc==5:
        opcion5()
    else:
        print("opcion incorrecta")