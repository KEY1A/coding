#Escribe un programa que calcule el promedio de 5 numeros que esten dentro del programa


def main():
    # Inicializacion de variables
    suma = 0
    promedio = 0
    # Definicion de los 5 numeros
    numeros = [1, 2, 3, 4, 5]  # Puedes cambiar estos números a los que necesites
    # Ciclo para sumar los 5 numeros
    for numero in numeros:
        suma = suma + numero
    # Calculo del promedio
    promedio = suma / 5
    # Impresion del promedio
    print("El promedio es:", promedio)

if __name__ == "__main__":
    main()