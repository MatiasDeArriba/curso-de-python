nombre = "Mati"
apellido = "De Arriba"
edad = 30

# Concatenar
completo = nombre + " " + apellido 

# f-strings (La forma moderna y correcta)
saludo = f"Hola, {nombre}! Tenés {edad} años."
print(saludo)  # <-- PASO 1.1: Imprimir el saludo

# Métodos útiles asignados e impresos
mayusculas = "hola mundo".upper()      
print(mayusculas)  # <-- PASO 1.2: Imprimir "HOLA MUNDO"

limpio = "  hola  ".strip()        
print(limpio)      # <-- PASO 1.3: Imprimir "hola"

lista = "hola mundo".split(" ")   
print(lista)       # <-- PASO 1.4: Imprimir ["hola", "mundo"]