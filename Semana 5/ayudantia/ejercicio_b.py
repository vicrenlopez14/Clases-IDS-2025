"""
¡Bienvenido a la ESEN! Si estás aquí, seguramente sea porque sueñas en convertirte en un Autovengador y luchar contra las fuerzas del Lado Oscuro de la Programación del Emperador Issem, líder de los Deceptinant.

Convertirse en un Autovengador no es tarea sencilla. Requiere de disciplina, esfuerzo y una capacidad intelectual sobresaliente. Para llegar a serlo, deberás superar una serie de desafíos que pondrán a prueba tu lógica y tu temple.

La primera gran tarea a la que todo aspirante es sometido es relativamente sencilla: encontrar la suma de dos enteros.

Es tu momento de brillar, ¡buena suerte!

Entrada
La única línea de entrada consiste en dos enteros
 y

Salida
La salida consiste en un único entero, la suma de
 y

"""

if __name__ == '__main__':
    # Receive
    numbers = input()

    # Process
    numbersSplit = numbers.split(" ")
    numA = int(numbersSplit[0])
    numB = int(numbersSplit[1])

    # Debug check
    # print(f"{numA} {numB}")

    # Result
    result=numA+numB

    # Print
    print(result)

