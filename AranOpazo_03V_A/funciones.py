import statistics,csv
import random as rd

def asignar_sueldos(trabajadores):
    sueldo = {}
#    sueldo = {trabajador : 0 for trabajador in trabajadores}
    
    for trabajador in trabajadores:
        sueldo = rd.randint(300000,2500000)
        trabajadores[trabajador] = sueldo
        print(trabajador,": $",sueldo)
    
    print("Sueldos asignados aleatoriamente de forma exitosa",sueldo)

    return sueldo


def clasificar_sueldos(trabajadores):
    menor_800mil = {}
    entre_800mil_y_2palos = {}
    mayor_2palos = {}

    for trabajador,sueldo in trabajadores:
        if sueldo < 800000:
            menor_800mil[trabajador] = sueldo
        elif sueldo <= 2000000:
            entre_800mil_y_2palos[trabajador] = sueldo
        else:
            mayor_2palos[trabajador] = sueldo
    
    print("\nClasificacion realizada exitosamene")
    
    print("Sueldos menores a $800.000\tTOTAL\t:",len(menor_800mil))
    for trabajador,sueldo in menor_800mil.items():
        print(trabajador,":\t$",sueldo)

    print("Sueldos entre $800.000 y $2.000.000\tTOTAL\t:",len(entre_800mil_y_2palos))
    for trabajador,sueldo in entre_800mil_y_2palos.items():
        print(trabajador,":\t$",sueldo)

    print("Sueldos mayores a $2.000.000\tTOTAL\t:",len(mayor_2palos))
    for trabajador,sueldo in mayor_2palos.items():
        print(trabajador,":\t$",sueldo)


def estadisticas(sueldo):
    max_sueldo = {}
    min_sueldo = {}
    promedio_sueldos = {}
    media_geometrica = {}

    lista_sueldos = list(sueldo.values())  

    for sueldo in lista_sueldos:
        max_sueldo = max(sueldo)
        min_sueldo = min(sueldo)
        promedio_sueldos = sum(sueldo) / len(lista_sueldos)
        media_geometrica = statistics.geometric_mean(sueldo)

    print("El sueldo mas alto es:\t$",max_sueldo)
    print("El sueldo mas bajo es:\t$",min_sueldo)
    print("El promedio de sueldos es:\t$",promedio_sueldos)
    print("La media geometrica de los sueldos es:\t$",media_geometrica)
    
    return max_sueldo,min_sueldo,promedio_sueldos,media_geometrica


def reporte_sueldos(sueldo):  
    # Descuento_salud = 0
    # Descuento_afp = 0

    dscto_salud = 0.7
    dscto_afp = 0.12
    sueldo_liquido = sueldo - dscto_salud - dscto_afp

    Descuento_salud = sueldo*dscto_salud
    Descuento_afp = sueldo*dscto_afp


    with open('Reporte de sueldos.csv','w') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(['Nombre Empleado','Sueldo Base','Descuento Salud','Descuento AFP','Sueldo Líquido'])
