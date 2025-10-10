# Ask for quantity
wage = input("Introduzca su salario: ")

# Has one dollar sign
times=0

for i in wage:
    # Check how many times it appears
    if i == "$":
        times+=1

# Print and evaluate inline
print(f"El valor ingresado {"tiene un símbolo de dolar" if times == 1 else "no tiene solo un símbolo de dólar"}.")

# Print and evaluate inline
print(f"El valor ingresado {"sí" if wage[0] == "$" else "no"} tiene un símbolo de dolar al inicio")