import random

personajes = [
    "un robot inteligente",
    "una científica",
    "un estudiante",
    "un explorador espacial"
]

lugares = [
    "en Marte",
    "en una ciudad inteligente",
    "en una selva amazónica",
    "en una estación espacial"
]

acciones = [
    "descubrió un tesoro oculto",
    "creó una nueva tecnología",
    "salvó a la humanidad",
    "encontró una civilización perdida"
]

personaje = random.choice(personajes)
lugar = random.choice(lugares)
accion = random.choice(acciones)

historia = f"Había una vez {personaje} que vivía {lugar}. Un día {accion} y cambió el futuro para siempre."

print("\nHISTORIA GENERADA POR IA\n")
print(historia)