## By Daniel Limón <hola@dlimon.net>,
## como parte del Curso Básico de Python de Platzi.com

import random

def generar_pwd():
    #Arrays de generación
    mayus = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    minus = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    simbolos = ["!", "@", "#", "$", "%", "&", "/", "(" ")", "=", "?", "¡"]
    numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    caracteres = mayus + minus + simbolos + numeros

    #Generador
    password = []
    for i in range(22): #password de 22 caracteres
        random_char = random.choice(caracteres) #Elige aleatoriamente un elemento del array caracteres.
        password.append(random_char)

    password = "".join(password) #join() para convertir cada elemento del array password a un string
    return password

def main():
    password = generar_pwd()
    print("Tu nueva contraseña es: "+password)


if __name__ == "__main__":
    main()
