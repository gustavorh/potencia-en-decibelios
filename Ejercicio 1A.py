# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 14:35:33 2021

Nombre: Gustavo Reyes Herrera
RUT: oculto

Mis respuestas en este trabajo son propias, y están realizadas
en conformidad con la formación ética de la universidad.

"""
import math

# Se define la funcion 'potenciaDecibelios' con parametro 'potencia' obtenido del input ingresado por el usuario


def potenciaDecibelios(potencia):

    # Se calcula el valor en decibelios con la siguiente fórmula
    # 10 * Log(10)(Potencia / W0) donde W0 es la mínima potencia audible y 'potencia' es la potencia de la fuente emisora del sonido
    # El valor se guarda en la variable local 'decibelios'

    decibelios = 10 * math.log(potencia / (pow(10, -12)), 10)

    # Retornamos el valor calculado en la fórmula en decibelios
    return decibelios


# Preguntamos al usuario por la potencia de una fuente emisora para calcular en decibelios
potencia = int(input("Ingrese la potencia de una fuente emisora: "))

# Se pasa el valor obtenido del input a la funcion 'potenciaDecibelios' y el valor retornado se guarda en la variable 'decibelios'
decibelios = potenciaDecibelios(potencia)

# Se entrega el resultado final en pantalla al usuario de la potencia calculada en decibelios
print(f'La potencia en decibelios es: {decibelios}')
