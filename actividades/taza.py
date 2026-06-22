while True:
    cafe = input("Estado del café (vacío/lleno): ")

    if cafe == "vacío":
        print("Rellenando el café.")
        break
    elif cafe == "lleno":
        print("¡A tomar!")
        break
    else:
        print("Está bien, esperá un momento.")

print("Listo, continuamos...")