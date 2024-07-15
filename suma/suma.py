def main():
    # Inicializacion de variables
    suma = 0
    promedio = 0
    numeros = []  # Lista vacía para almacenar los números

    # Ciclo para pedir al usuario los 5 numeros
    print("Por favor, ingresa 5 números:")
    for i in range(5):
        numero = float(input(f"Numero {i+1}: "))
        numeros.append(numero)

    # Ciclo para sumar los 5 numeros
    for numero in numeros:
        suma = suma + numero

    # Calculo del promedio
    promedio = suma / 5

    # Impresion del promedio
    print("El promedio es:", promedio)

if __name__ == "__main__":
    main()