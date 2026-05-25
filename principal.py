# programa principal

from libreria import ver, eliminar, agregar, buscar, contar

# Diccionario inicial
datos = {"nombre": "Raul", "edad": 13, "correo": "raul@ejemplo.com"}

while True:
    print("\n1.Ver 2.Eliminar 3.Agregar 4.Buscar 5.Contar 6.Salir")
    op = input("> ")
    
    if op == "1": ver(datos)
    elif op == "2": eliminar(datos)
    elif op == "3": agregar(datos)
    elif op == "4": buscar(datos)
    elif op == "5": contar(datos)
    elif op == "6": print("Adiós"); break
    else: print("Opción inválida")
