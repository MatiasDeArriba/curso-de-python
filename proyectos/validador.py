# --- SIMULADOR DE VALIDACIÓN DE QA ---
print("=== Sistema de Registro de Usuario ===")
# Entrada de datos
usuario = input("Ingrese nombre de usuario:")
password = input("Ingresa contraseña:")


# Reglas de Validacion
# 1. El Usuario debe tener al menos 5 caracteres
# 2. La contraseña debe tener al menos 8 caracteres


print("\n--- Resultados del Test ---")
if len(usuario) >= 5 and len(password) >= 8:
    print("✅ ESTADO: Regustro Exitoso.")
    print(f"Bienvenido, {usuario}. Tu cuenta ha sido creada.")
else:
    print("❌ ESTADO: Error en el registro.")    
    # Debugging (Para saber exactamente qué falló)
    if len(usuario) < 5:
        print("Error: El nombre de usuario debe tener al menos 5 caracteres.)")
    if len(password) < 8:
        print("Error: La Contraseña es muy corta (minimo 8 caracteres).")
print("---------------------------")            