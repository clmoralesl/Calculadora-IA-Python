print ('Bienvenido a calculadora IA')
diccionariocalculos = {}
def ingresodatos():
    while True:
        print('-----------Ingreso de datos-----------')
        llaveingreso = input('Ingrese el nombre de la operatoria:\n').capitalize()
        valoringreso = input('Ingrese el cálculo de la operatoria:\n')
        diccionariocalculos[llaveingreso] = valoringreso
        print('Se ha ingresado correctamente la siguiente opertaria:')
        print(f'{llaveingreso} = {valoringreso}')
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
def borrardatos():
    while True:
        print('-----------Borrar datos-----------') 
        if not diccionariocalculos:
            print('No existen operaciones guardadas')
            break
        else:
            listardiccionario()
            llaveborrar = input ('Ingrese la operación a borrar:\n').capitalize()
            if llaveborrar in diccionariocalculos:
                del diccionariocalculos[llaveborrar]
                print(f'Operación {llaveborrar} borrada exitosamente')
            else:
                print(f'No se ha encontrado la operación {llaveborrar}')
                break
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
def probarllave():
    print('-----------Probar operaciones-----------')
    listardiccionario()
    if diccionariocalculos:
        llaveprueba = input("Ingrese la operatoria que desea probar:\n").capitalize()
        if llaveprueba in diccionariocalculos:
            for llave, valor in diccionariocalculos.items():
                if llaveprueba == llave:
                    print(valor)
    else:
        print('Volviendo al menu principal')
def listardiccionario():
    if not diccionariocalculos:
        print('No existen operatorias guardadas')
    else:
        print ('Las operatorias disponibles son las siguientes:')
        for llave, valor in diccionariocalculos.items():
            print(f'Operatoria:{llave}\nResultado:{valor}')     
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
        if opcionmenu >5 or opcionmenu <1:
            print('Opción inválida, vuelva a intentar')
            continue
    except ValueError:
        print ('Error de datos, intente nuevamente')
    match opcionmenu:
        case 1:
            ingresodatos()
        case 2:
            borrardatos()
        case 3:
            print('-----------Listado de datos-----------')
            listardiccionario()
        case 4:
            probarllave()
        case 5:
            print('Saliendo del programa, Gracias por su preferencia')
            break
