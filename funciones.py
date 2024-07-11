import random,os,csv
trabajadores = ["Juan Perez","Maria Garcia","Carlos Lopez","Ana martinez","Pedro rodriguez","Laura hernandez","Miguel sanchez","Isabel gomez","Francisco Diaz","Elena fernandez"]
sueldos=[]
def opcion1():
    print("asignar sueldos aleatorios")
    sueldoJuan=numerorandom()
    sueldoMaria=numerorandom()
    sueldoCarlos=numerorandom()
    sueldoAna=numerorandom()
    sueldoPedro=numerorandom()
    sueldoLaura=numerorandom()
    sueldoMiguel=numerorandom()
    sueldoIsabel=numerorandom()
    sueldoFrancisco=numerorandom()             
    sueldoElena=numerorandom()   
    sueldo=[sueldoJuan,sueldoMaria,sueldoCarlos,sueldoAna,sueldoPedro,sueldoLaura,sueldoMiguel,sueldoIsabel,sueldoFrancisco,sueldoElena]
    sueldos.append(sueldo)
    print("sueldos asignados con exito")
    

#menor a 800k
#entre 800k-2millones
#sueldos superiores a 2 millones
menor800k=[]
entre800kdosmillones=[]
superiordosmillones=[]
def opcion2():
    print("Clasificador de sueldos")
    if not sueldos:
        print("asigne sueldos primero en la opcion 1")
    else:
        pass
         #  if sueldo_clasificar<800000:
       #     menor800k.append(sueldo_clasificar)
        #    print("menor a 800k")
        #elif sueldo_clasificar>800000 and sueldo_clasificar<2000000:
        #    entre800kdosmillones.append(sueldo_clasificar)
         #   print("entre 800k y 2 millones")
        #elif sueldo_clasificar>2000000:
         #   superiordosmillones.append(sueldo_clasificar)
          #  print("superior a 2 millones")

def opcion3():
    print("ver estadisticas")
    if not sueldos:
        print("asigne sueldos primero en la opcion 1")
    else:
        while True:
            print("""
            1) ver sueldo mas alto
            2) ver sueldo mas bajo
            3)  Promedio de sueldos
            4) Media geometrica""")
            opc2=validaropc([1,2,3,4])
            if opc2==1:
                print("sueldo mas alto")
            elif opc2==2:
                print("sueldo mas bajo")
            elif opc2==3:
                print("promedio de sueldos")
                promedio=promediosueldos()
                print(f"el promedio de sueldos es de ${promedio}")
            elif opc2==4:
                print("media geometrica")
                mediageo=mediageometrica
                print(mediageo)


def opcion4():
    print("Reporte de sueldos")
    if not sueldos:
        print("asigne sueldos primero en la opcion 1")
    else:
        for x in sueldos:
            print("Nombre empleado  Sueldo Base  Desc.salud  Desc.AFP  Sueldo liquido")
            print(f"Juan Perez",x[0], descsalud(x[0]), descAFP(x[0]),)
            print(f"Maria Garcia",x[1], descsalud(x[1]), descAFP(x[1]),)
            print(f"Carlos Lopez",x[2], descsalud(x[2]), descAFP(x[2]),)
            print(f"Ana Martinez",x[3], descsalud(x[3]), descAFP(x[3]),)
            print(f"Pedro Rodriguez",x[4], descsalud(x[4]), descAFP(x[4]),)
            print(f"Laura Hernandez",x[5], descsalud(x[5]), descAFP(x[5]),)
            print(f"Miguel Sanchez",x[6], descsalud(x[6]), descAFP(x[6]),)
            print(f"Isabel Gomez",x[7], descsalud(x[7]), descAFP(x[7]),)
            print(f"Francisco Diaz",x[8], descsalud(x[8]), descAFP(x[8]),)
            print(f"Elena Fernande2",x[9], descsalud(x[9]), descAFP(x[9]),)
            with open("sueldotrabajadores.csv","w",newline="") as archivo:
                escritorcsv=csv.writer(archivo)
                escritorcsv.writerows(sueldos)
            
                
                
            
            
            

def opcion5():
    print("Finalizando programa...")
    print("desarrolado por Marcelo Novoa")
    print("Rut: 21.620.822-6")

def descsalud(sueldobase):
    sueldosalud=sueldobase*0.07
    return sueldosalud

def descAFP(sueldobase):
    sueldoafp=sueldobase*0.12
    return sueldoafp
#def sueldoliquido(sueldobase):
    sueldoliquido=sueldobase
    return sueldoliquido
def numerorandom():
    numero=random.randint(300000,2500000)
    return numero

####

def validaropc(lista):
    while True:
        try:
            opc=int(input("seleccione opcion: "))
            if opc in (lista):
                return opc
            else:
                print("Error, no puede ingresar letras")
        except:
            print("Error! solo puede ingresar numeros enteros")

def promediosueldos():
    for x in sueldos:
        suma=x[0]+x[1]+x[3]+x[4]+x[5]+x[6]+x[7]+x[8]+x[9]
        promedio=suma/10
        return promedio
def mediageometrica():
    for x in sueldos:
        multiplicacion=x[0]*x[1]*x[3]*x[4]*x[5]*x[6]*x[7]*x[8]*x[9]
        media=multiplicacion**1/10
        return media
