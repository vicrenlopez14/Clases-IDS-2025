"""
6 peticiones para su fruta favorita.
"""

kids=list()

# Six times
for i in range(6):
    # Ask what kid it is
    kidNum= int(input("¿De qué niño estamos hablando (número)?: "))

    kids.append(input(f"¿Cuál es la fruta favorita del niño {i + 1}?: "))

# Print them
for i in range(len(kids)):
    print(f"La fruta favorita del niño número {i} es {kids[i]}")

# Esto está malo, no le entendí a alvin jajaja