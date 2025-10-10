"""
Crear colección de nombres de 7 alumnos en el orden en que ingresaron al aula.
"""

# Define infinite list
students=list()

# 7 times
for i in range(7):
    # Ask each time
    students.append(input(f"¿Cuál es el nombre del estudiante que entró el {i+1}?: "))

# Print ordered results
for i in range(len(students)):
    print(f"{students[i]} entró el {i+1}º.")