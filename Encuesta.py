# Autor: Antonio Betancourt

# el numero de personas
total = 10   

nombres = [""] * total
ideas = [""] * total

print("\n--- Encuesta de Ideas de Proyecto ---\n")

for persona in range(total):
    nombre = input("Ingrese su nombre y apellido: ")
    idea = input("Ingrese la idea de proyecto: ")
    print("\n--- Su nombre e idea han sido registrados ---\n")
    nombres[persona] = nombre
    ideas[persona] = idea

print("\n--- Nombres e Ideas registradas ---\n")
for persona in range(total):
    print("Nombre:", nombres[persona], "   |   Idea:", ideas[persona], "\n")
