# Ask for quantity
wage = input("Introduzca su salario: ")

# Has one dollar sign

# Print and evaluate inline
print(f"El valor ingresado {"tiene un símbolo de dolar" if wage.count("$") == 1 else "no tiene solo un símbolo de dólar"}.")

# Print and evaluate inline
print(f"El valor ingresado {"sí" if wage[0] == "$" else "no"} tiene un símbolo de dolar al inicio")