#las funciones

def ver(d): 
    for k,v in d.items(): print(f"{k}: {v}")

def eliminar(d):
    if not d: print("Vacío"); return
    print(list(d.keys()))
    k = input("Clave: ")
    if k in d: print(f"Eliminado: {d.pop(k)}")
    else: print("No existe")

def agregar(d):
    k = input("Clave: ")
    v = input("Valor: ")
    d[k] = v
    print(f"✓ {k}: {v}")

def buscar(d):
    if not d: print("Vacío"); return
    k = input("Clave a buscar: ")
    if k in d: print(f"Valor: {d[k]}")
    else: print("No existe")

def contar(d):
    print(f"Total: {len(d)} elementos")
