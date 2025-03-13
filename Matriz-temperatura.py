# Función para calcular la temperatura promedio de cada ciudad
def calcular_temperatura_promedio(datos_ciudades):
    """
    Recibe un diccionario con temperaturas semanales de varias ciudades
    y calcula el promedio de cada una.
    """
    promedios = {}  # Diccionario donde guardaremos los resultados

    # Recorremos cada ciudad y sus temperaturas
    for ciudad, temperaturas in datos_ciudades.items():
        promedio = sum(temperaturas) / len(temperaturas)  # Calculamos el promedio
        promedios[ciudad] = promedio  # Guardamos el resultado en el diccionario

    return promedios  # Retornamos el diccionario con los promedios


# Función que muestra el menú para seleccionar una ciudad y ver su temperatura por semanas
def menu(datos):
    """
    Muestra un menú para que el usuario elija una ciudad y vea sus temperaturas semanales y promedio.
    """
    promedios = calcular_temperatura_promedio(datos)  # Calculamos los promedios una vez
    semanas = ["Semana 1", "Semana 2", "Semana 3", "Semana 4"]  # Etiquetas para las semanas

    while True:  # Bucle para repetir la selección de ciudad
        print("\nSeleccione una ciudad para ver sus temperaturas por semana y su promedio:")

        # Mostramos las opciones disponibles
        ciudades = list(datos.keys())  # Convertimos las claves en una lista
        for i, ciudad in enumerate(ciudades, 1):  # Enumeramos desde 1
            print(f"[{i}] {ciudad}")

        # Pedimos al usuario que seleccione una ciudad
        try:
            opcion = int(input("\nIngrese el número de la ciudad: "))

            # Verificamos que la opción sea válida
            if 1 <= opcion <= len(ciudades):
                ciudad_seleccionada = ciudades[opcion - 1]  # Obtenemos el nombre de la ciudad
                print(f"\nTemperaturas en {ciudad_seleccionada}:")

                # Mostramos las temperaturas con su respectiva semana
                temperaturas = datos[ciudad_seleccionada]
                for i, temp in enumerate(temperaturas):
                    print(f"{semanas[i]}: {temp}°C")

                # Mostramos el promedio
                print(f"\nTemperatura promedio en {ciudad_seleccionada}: {promedios[ciudad_seleccionada]:.2f}°C")
            else:
                print("\n[!] Opción no válida, intente de nuevo.")
                continue  # Volver a mostrar el menú

        except ValueError:
            print("\n[!] Error: Ingrese un número válido.")
            continue  # Volver a mostrar el menú

        # Preguntamos si el usuario quiere seleccionar otra ciudad
        repetir = input("\n¿Quieres seleccionar otra ciudad? (si/no): ").strip().lower()
        if repetir != "si":
            print("\nSaliendo del programa...")
            break  # Salimos del bucle si la respuesta no es "si"


# Datos de ejemplo: temperaturas de 3 ciudades en 4 semanas
datos_temperaturas = {
    "Ciudad Quito": [25, 26, 24, 23],
    "Ciudad Cuenca": [30, 31, 29, 28],
    "Ciudad Loja": [20, 21, 19, 18]
}

# Llamamos a la función del menú para iniciar el programa
menu(datos_temperaturas)
