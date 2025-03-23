import json

datos = json.load(open("pr1.json"))

for equipo in datos['equipos']:
    print(f"Nombre: {equipo['nombre']}")
    print(f"Ciudad: {equipo['ciudad']}")
    print(f"Estadio: {equipo['estadio']}")

    for jugador in datos['jugadores']:
        if jugador['equipo'] == equipo['nombre']:
            jugador_estrella = jugador['nombre']
            dorsal = jugador['dorsal']
            break
    print(f"Jugador Estrella: {jugador_estrella}, Nº{dorsal}")

    for entrenador in datos['entrenadores']:
        if entrenador['equipo'] == equipo['nombre']:
            entrenador = entrenador['nombre']
            break
    print(f"Entrenador: {entrenador}")

    print("Partidos:")
    for partido in datos['partidos']:
        if partido['equipo1'] == equipo['nombre'] or partido['equipo2'] == equipo['nombre']:
            print(f"  - {partido['equipo1']} vs {partido['equipo2']}: {partido['resultado']}")
    print()

print(f"Entre los mejores jugadores encontramos a:")
for jugador in datos['mejores']: print(jugador)

print()
print(f"Año: {datos['fecha']}")
print(f"Autor: {datos['nombre']}")
