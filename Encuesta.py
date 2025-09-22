# Autor: Antonio Betancourt

print("Encuesta de ideas de proyecto\n")

nombres = []
ideas = []

for persona in range(10):
    print("\n- Persona", persona + 1)

    nombre = input("\nEscribe tu nombre: ")
    idea = input("Escribe tu idea de proyecto: ")
    nombres += [nombre]   
    ideas += [idea]       

print("\n--- Resultados de la encuesta ---")
for persona in range(10):
    print("\n", persona + 1, ". Nombre: ", nombres[persona], " |  Idea: ", ideas[persona])

