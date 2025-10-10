"""
Se le ha asignado una palabra encriptada la cual servirá como su contraseña, para poder describable le
indican que dentro del texto encriptado la primera letra del texto encriptado si es la primera letra de su contraseña.
Después hay cada vez dos letras que no son parte de su contraseña.
"""

# Ask password and write it inline
print(f"La contraseña es: {input("Introduzca el texto encriptado: ")[::3]}" )