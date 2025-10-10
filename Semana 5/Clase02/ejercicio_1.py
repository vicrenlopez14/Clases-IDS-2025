# Capturar la cantidad de articulos producidos por mes y luego estimar el costo total.
# Recibir valores de los meses de enero, febrero y marzo
# Sabiendo que los costos en enero fue de 1.25, febrero 1.38 marzo 1.14

# Define months and costs
products = {
    'enero': 1.25,
    'febrero': 1.38,
    'marzo': 1.14
}

# Total holder
total = 0

# Ask for prices each month
for month in dict.keys(products):
    total+=float(input(f"Digite la cantidad de articulos en {month}: ")) * products[month]

# Print output
print(f"El costo total es ${round(total, 2)}")





