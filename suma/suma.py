import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

def calcular_promedio():
    suma = 0
    numeros = []  # Lista para almacenar los números

    # Ciclo para pedir al usuario los 5 numeros
    for i in range(5):
        numero = simpledialog.askfloat("Input", f"Numero {i+1}: ", parent=root)
        if numero is None:  # Si el usuario cancela la entrada, terminar el programa.
            return
        numeros.append(numero)

    # Ciclo para sumar los 5 numeros
    for numero in numeros:
        suma += numero

    # Calculo del promedio
    promedio = suma / 5

    # Mostrar el promedio
    messagebox.showinfo("Resultado", f"El promedio es: {promedio}")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # No mostrar la ventana principal de Tkinter
    calcular_promedio()