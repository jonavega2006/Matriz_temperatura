import random

ciudades = ["Ciudad COCA", "Ciudad SACHA", "Ciudad LORETO"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 4  

matriz_temperaturas = []
for i in range(len(ciudades)):
    matriz_temperaturas.append([])
    for w in range(semanas):
        matriz_temperaturas[i].append([])
        for j in range(len(dias_semana)):
            matriz_temperaturas[i][w].append([random.randint(10, 35) for _ in range(24)])

print("==============================================")
print("= MATRIZ DE TEMPERATURA                      =")
print("==============================================")
print("= Seleccione una opción:                     =")
print("= [1]. Ver temperaturas de una ciudad        =")
print("= [2]. Ver temperaturas de todas las ciudades=")
print("==============================================")
opcion = input("Ingrese el número de opción: ")
print("==============================================")

if opcion == "1":
    for idx, ciudad in enumerate(ciudades):
        print(f"{idx + 1}. {ciudad}")
    try:
        seleccion_ciudad = int(input("Ingrese el número de la ciudad: ")) - 1
        if 0 <= seleccion_ciudad < len(ciudades):
            print("\nSeleccione una semana (1-", semanas, "):")
            for w in range(semanas):
                print(f"{w + 1}. Semana {w + 1}")
            seleccion_semana = int(input("Ingrese el número de la semana: ")) - 1
            if 0 <= seleccion_semana < semanas:
                print("\nTemperaturas promedio para", ciudades[seleccion_ciudad], "en Semana", seleccion_semana + 1)
                for j in range(len(dias_semana)):
                    promedio = sum(matriz_temperaturas[seleccion_ciudad][seleccion_semana][j]) / 24
                    print(dias_semana[j] + ":", round(promedio, 2), "°C")
            else:
                print("Selección de semana inválida")
        else:
            print("Selección de ciudad inválida")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número.")

elif opcion == "2":
    for i in range(len(ciudades)):
        print("\nTemperaturas promedio para", ciudades[i])
        for w in range(semanas):
            print("\nSemana", w + 1)
            for j in range(len(dias_semana)):
                promedio = sum(matriz_temperaturas[i][w][j]) / 24
                print(dias_semana[j] + ":", round(promedio, 2), "°C")
else:
    print("Opción inválida")
