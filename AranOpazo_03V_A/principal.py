import funciones as fn

trabajadores = ["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]

sueldo = {}

while True:
    try:
        print("\n-----\tMENU\t-----")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")

        opc = int(input("Ingrese una opción:\t"))

        if opc == 1:
            print("\nAsignar sueldos aleatoriamete")
            if sueldo:
                sueldo = fn.asignar_sueldos(trabajadores)
                print(sueldo)
        
        elif opc == 2:
            print("\nClasificar sueldos: menores a $800.000, entre $800.000 y $2.000.000 y mayores a $2.000.000")
            if sueldo:
                clasificacion = fn.clasificar_sueldos(trabajadores)
                print(clasificacion)

        elif opc == 3:
            print("\nVer las estadisticas de los sueldos: sueldo mas alto, sueldo mas bajo, promedio de sueldos y media geométrica")
            fn.estadisticas(sueldo)

        elif opc == 4:
            print("\nSe generará un reporte de sueldos en formato csv")
            fn.reporte_sueldos(sueldo)
        
        elif opc == 5:
            print("\nFinalizando programa...")
            print("Desarrollado por Aran Opazo")
            print("R.U.T.: 16.575.051-9\n")
            break

        else:
            print("\nIngrese solo números entre 1 y 5")

    except:
        print("\nIngrese solo opciones válidas")