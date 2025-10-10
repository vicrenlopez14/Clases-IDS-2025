"""
- Crear una lista con los cinco dias laborales de la semana.
- Por medio de inputs iremos llenando la lista con la cantidad de productos vendidos.
Luego de cada dia actualizado mostrar un mensaje como, el dia lunes, se vendieron x
Calcule la cantidad de productos vendidos de la semana
"""

week = {
    'lunes': 0,
    'martes': 0,
    'miércoles': 0,
    'jueves': 0,
    'viernes':0,
    'sábado':0,
    'domingo': 0,
}

# Acc
total = 0

for day in dict.keys(week):
    # Ask for quantity per day
    quantity = int(input(f"¿Cuantos productos vendió el {day}?: "))

    # Print today's result
    print(f"El {day} se vendieron {quantity} productos.")

    # Add to total
    total+=quantity

# Print total
print(f"Se vendieron {total} productos en total.")