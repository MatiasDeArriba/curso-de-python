# --- SIMULADOR DE CAJERO AUTOMÁTICO ---
# Este programa gestiona un saldo bancario permitiendo operaciones básicas
# a través de un menú interactivo.

def ejecutar_cajero():
    # 1. Definimos el estado inicial (Variables)
    saldo = 1000.0  # Usamos float para permitir decimales (dinero)
    activo = True   # Bandera para mantener el bucle funcionando

    print("--- BIENVENIDO AL SISTEMA BANCARIO ---")

    # 2. El bucle 'while' mantiene el programa corriendo hasta que el usuario decida salir
    while activo:
        print("\nMenú de opciones:")
        print("1. Ver saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Salir")

        opcion = input("\nSeleccione una opción (1-4): ")

        # 3. Estructura de control if/elif/else para la lógica del menú
        if opcion == "1":
            # Formateamos a 2 decimales para que se vea profesional
            print(f"Su saldo actual es: ${saldo:.2f}")

        elif opcion == "2":
            try:
                # Convertimos la entrada a float para cálculos matemáticos
                monto_deposito = float(input("Ingrese el monto a depositar: "))
                if monto_deposito > 0:
                    saldo += monto_deposito # Suma simplificada: saldo = saldo + monto
                    print(f"Depósito exitoso. Nuevo saldo: ${saldo:.2f}")
                else:
                    print("Error: El monto debe ser mayor a cero.")
            except ValueError:
                # Este bloque evita que el programa falle si el usuario escribe letras
                print("Error: Ingrese un número válido.")

        elif opcion == "3":
            try:
                monto_retiro = float(input("Ingrese el monto a retirar: "))
                # Validación de reglas de negocio: no retirar más de lo que hay
                if 0 < monto_retiro <= saldo:
                    saldo -= monto_retiro # Resta simplificada
                    print(f"Retiro exitoso. Saldo restante: ${saldo:.2f}")
                elif monto_retiro > saldo:
                    print("Error: Fondos insuficientes.")
                else:
                    print("Error: El monto debe ser mayor a cero.")
            except ValueError:
                print("Error: Ingrese un número válido.")

        elif opcion == "4":
            print("Gracias por usar nuestros servicios. ¡Hasta pronto!")
            activo = False # Rompemos el bucle cambiando el valor de la bandera

        else:
            # Captura cualquier entrada que no esté entre 1 y 4
            print("Opción no válida. Intente nuevamente.")

# 4. Llamada a la función para iniciar el programa
if __name__ == "__main__":
    ejecutar_cajero()