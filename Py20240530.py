print ('Bienvenido a calculadora IA')
diccionariocalculos = {}
def ingresodatos(llave,valor):
    diccionariocalculos[llave] = valor
def borrardatos(llave):
    if llave in diccionariocalculos:
        del diccionariocalculos[llave]
        print(f'Operación {llave} borrada exitosamente')
    else:
        print(f'No se ha encontrado la operación {llave}')
def probarllave(llave):
    for llaveprueba, valor in diccionariocalculos.items():
        if llaveprueba == llave:
            print(valor)
while True:
    try:
        print ('''
-----------Calculadora-----------
1) Ingresar datos al diccionario
2) Borrar datos del diccionario
3) Listar los datos del diccionario
4) Probar la operación
5) Salir del programa
    ''')
        opcionmenu = int(input('Ingrese una opción:\n'))
    except ValueError:
        print ('Error de datos, intente nuevamente')
    if opcionmenu == 1:
            while True:
                print('-----------Ingreso de datos-----------')
                llaveingreso = input('Ingrese el nombre de la operatoria:\n').capitalize()
                valoringreso = input('Ingrese el cálculo de la operatoria:\n')
                ingresodatos(llaveingreso,valoringreso)
                print(diccionariocalculos)
                while True:
                    try:
                        print('¿Desea ingresar otra operación?')
                        print('1) SI')
                        print('2) NO')
                        continuaringreso = int(input())
                        if continuaringreso !=1 and continuaringreso !=2:
                            print('Ingrese una opción válida')
                            continue
                        else:
                            break
                    except ValueError:
                        print('Error de dato, vuelva a intentar')
                        continue
                if continuaringreso == 1:
                    continue
                else:
                    break
    elif opcionmenu == 2:
        while True:
            print('-----------Borrar datos-----------')  
            llaveborrar = input ('Ingrese la operación a borrar:\n').capitalize()
            borrardatos(llaveborrar)
            while True:
                    try:
                        print('¿Desea borrar otra operación?')
                        print('1) SI')
                        print('2) NO')
                        borraringreso = int(input())
                        if borraringreso !=1 and borraringreso !=2:
                            print('Ingrese una opción válida')
                            continue
                        else:
                            break
                    except ValueError:
                        print('Error de dato, vuelva a intentar')
                        continue
            if borraringreso == 1:
                continue
            else:
                break
    elif opcionmenu == 3:
        print('-----------Listado de datos-----------')
        if not diccionariocalculos:
                print('No existen operatorias')
        else:
            for llave,valor in diccionariocalculos.items():
                print(f'Operatoria:{llave}\nResultado:{valor}')        
    elif opcionmenu == 4:
        llaveprueba = input("Ingrese la operatoria a ingresar").capitalize()
        probarllave(llaveprueba)
    elif opcionmenu == 5:
        print('Saliendo del programa, Gracias por su preferencia')
    else:
       print('Opción inválida')