""" 1. Campus requiere administrar algunos datos de sus Campers
como por ejemplo, la creación, eliminación o búsqueda de los
developers, entre otros, por tal razón, ha solicitado el diseño de
un programa que cuente con el siguiente menú como panel de
control: """

""" 1.CREAR GRUPO ARTEMIS:
    1.1 LISTAR CAMPERS DE ARTEMIS
    1.2 AGREGAR CAMPERS A ARTEMIS 
    1.3 ELIMINAR CAMPERS DE ARTEMIS
    1.4 ORDENAR ALFABETICAMENTE EN LISTA DE ARTEMIS
    1.5 BUSCAR CAMPER EN LISTA DE ARTEMIS

    2. CREAR GRUPO SPUTNIK:
    2.1 LISTAR CAMPERS DE SPUTNIK
    2.2 AGREGAR CAMPERS A SPUTNKIK
    2.3 ELIMINAR CAMPERS DE SPUTNIK
    2.4 ORDENAR ALFABETICAMENTE EN SPUTNIK
    2.5 BUSCAR CAMPER EN LISTA DE SPUTNIK
    3. SALIR
    DIGITE OPCION: 
 """
nombre = ""
sputnik=[]
opc = 0
while opc !=3:
    print ('------------------------------\n')
    print(f'1.CREAR GRUPO ARTEMIS:\n 1.1 LISTAR CAMPERS DE ARTEMIS\n 1.2 AGREGAR CAMPERS A ARTEMIS \n 1.3 ELIMINAR CAMPERS DE ARTEMIS \n 1.4 ORDENAR ALFABETICAMENTE EN LISTA DE ARTEMIS \n 1.5 BUSCAR CAMPER EN LISTA DE ARTEMIS')
    print(f'\t2.CREAR GRUPO SPUTNIK:\n\t2.1 LISTAR CAMPERS DE SPUTNIK\n\t2.2 AGREGAR CAMPERS A SPUTNKIK\n\t2.4 ORDENAR ALFABETICAMENTE EN SPUTNIK\n\t2.5 BUSCAR CAMPER EN LISTA DE SPUTNIK\n\t3.SALIR \n\t\tDIGITE OPCION:')
 
    opc = float(input())
    if opc == 1:
        print ('------------------------------\n')
        print(f'Sputnik: {sputnik}\n')
    elif opc == 1.1:
        print ('\n------------------------------\nLISTA DE ESTUDIANTES ARTEMIS:')
        for i in sputnik: 
            print(f'* {i}')
    
    elif opc == 1.2:
        print ('------------------------------\n')
        nombre = input('Ingrese nombre completo del camper:')
        sputnik.insert(0,nombre)
        print(f'{nombre}-')
        
    elif opc == 1.3:
        print ('------------------------------\n')
        nombre = input('Ingrese el nombre a eliminar:')
        x= sputnik.index(nombre)    
        del sputnik[x]
        print(f'{nombre}+')

    elif opc ==1.4:
        print ('------------------------------\n')
        sputnik.sort()
        print ('\n------------------------------\nLISTA DE ESTUDIANTES ARTEMIS ORDENADOS:')
        for i in sputnik: 
            print(f'* {i}')


    



