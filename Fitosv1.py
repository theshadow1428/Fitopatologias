patologias = { # Pues ponemos todas las patologías aqui con los pesos de sus sintomas

    # Estos son los virus
    "Virus rugoso café del tomate (ToBRFV)": {
        "mosaicos": 2,
        "necrosis": 2,
        "deformacion": 2,
        "reduccion_vigor": 2,
        "manchas_fruto": 2,
        "deformacion_fruto": 2,
        "cambios_color_fruto": 1
    },

    "Virus del mosaico del tomate (ToMV)": {
        "mosaicos": 3,
        "deformacion": 2,
        "reduccion_vigor": 2,
        "manchas_fruto": 1,
        "deformacion_fruto": 2
    },

    "Virus del mosaico del pepino (CMV)": {
        "mosaicos": 3,
        "deformacion": 2,
        "reduccion_vigor": 2,
        "amarillamiento": 1
    },

    "Virus de la hoja amarilla en cuchara (TYLCV)": {
        "amarillamiento": 3,
        "deformacion": 3,
        "enrollamiento": 3,
        "reduccion_vigor": 2,
        "crecimiento_reducido": 2
    },

    "Virus de la marchitez manchada del tomate (TSWV)": {
        "necrosis": 3,
        "manchas": 2,
        "marchitez": 2,
        "reduccion_vigor": 1,
        "bronceado": 2,
        "daño_flores": 1,
        "manchas_fruto": 2
    },

    "Virus de la marchitez manchada de Impatiens (INSV)": {
        "necrosis": 3,
        "manchas": 2,
        "marchitez": 2,
        "reduccion_vigor": 1,
        "bronceado": 2,
        "daño_flores": 1
    },
    # Aqui van las bacterias

    "Cáncer bacteriano": {
        "marchitez": 3,
        "necrosis": 2,
        "lesiones_tallo": 3,
        "manchas_fruto": 2,
        "reduccion_vigor": 2
    },

    "Mancha bacteriana": {
        "manchas": 3,
        "necrosis": 2,
        "lesiones_tallo": 1,
        "manchas_fruto": 3,
        "necrosis_fruto": 2
    },

    "Peca o mancha bacteriana": {
        "manchas": 3,
        "necrosis": 2,
        "manchas_fruto": 2,
        "humedad_alta": 2
    },


    # Los hongos y oomnicitos

    "Tizón tardío": {
        "manchas": 3,
        "necrosis": 3,
        "marchitez": 2,
        "manchas_fruto": 3,
        "pudricion": 2,
        "humedad_alta": 3
    },

    "Tizón temprano": {
        "manchas": 3,
        "necrosis": 2,
        "manchas_circulares": 3,
        "defoliacion": 2,
        "manchas_fruto": 2
    },

    "Oídio o cenicilla": {
        "micelio": 3,
        "manchas": 1,
        "amarillamiento": 2,
        "reduccion_vigor": 1
    },

    "Moho de la hoja o Fulvia": {
        "manchas": 2,
        "amarillamiento": 2,
        "micelio": 3,
        "defoliacion": 2,
        "humedad_alta": 2
    },

    "Damping-off": {
        "marchitez": 3,
        "reduccion_vigor": 2,
        "necrosis": 2,
        "lesiones_tallo": 2
    },

    "Fusariosis": {
        "marchitez": 3,
        "amarillamiento": 2,
        "reduccion_vigor": 2,
        "necrosis": 2
    },

    "Pudrición de corona y raíz": {
        "marchitez": 3,
        "reduccion_vigor": 2,
        "necrosis": 2,
        "pudricion": 3
    },

    #Y aqui las plagas (No es tan de ahuevo separarlas pero pues solo para que cuando vayamos agregando pues nos ayude)

    "Mosca blanca": {
        "insectos": 3,
        "mielecilla": 3,
        "fumagina": 3,
        "amarillamiento": 2,
        "deformacion": 1,
        "presencia_ninfas": 3
    },

    "Trips": {
        "insectos": 3,
        "bronceado": 3,
        "daño_flores": 3,
        "manchas": 1,
        "deformacion": 1
    },

    "Paratrioza": {
        "insectos": 3,
        "reduccion_vigor": 2,
        "amarillamiento": 2,
        "deformacion": 1
    },

    "Araña roja": {
        "acaros": 3,
        "punteaduras": 3,
        "bronceado": 3,
        "amarillamiento": 2,
        "defoliacion": 2
    },

    "Gusano del fruto": {
        "larvas": 3,
        "perforaciones": 3,
        "manchas_fruto": 2,
        "daño_fruto": 3,
        "galerias": 1
    }
}

#Funcion de las respuestas (Cuanto vale s y n en booleanos) y que hacer si ponen otra opcion

def preguntar(texto):

    while True:

        respuesta = input(texto + " (s/n): ").lower()

        if respuesta == "s":
            return True

        elif respuesta == "n":
            return False

        else:
            print("Respuesta no válida. Escribe s o n.")



print("              SOLANUM - BETA")
print("     Sistema de análisis de patologías")


#Preguntas (Algunas preguntas son generales y por lo tanto no tendran tanto peso, pero otras si son más especificas y por lo tanto son mas pesadas)

print("\nPor favor responda las siguientes preguntas en base a lo que observe:\n")

sintomas = {}


sintomas["mosaicos"] = preguntar(
    "¿Observa mosaicos o patrones verde claro/verde oscuro?"
)

sintomas["amarillamiento"] = preguntar(
    "¿Observa amarillamiento en las hojas?"
)

sintomas["necrosis"] = preguntar(
    "¿Observa necrosis o tejidos café/negros?"
)

sintomas["marchitez"] = preguntar(
    "¿La planta presenta marchitez?"
)

sintomas["deformacion"] = preguntar(
    "¿Observa deformación o enrollamiento de hojas?"
)

sintomas["enrollamiento"] = preguntar(
    "¿Las hojas presentan enrollamiento o abarquillamiento?"
)

sintomas["reduccion_vigor"] = preguntar(
    "¿La planta presenta reducción de crecimiento o vigor?"
)

sintomas["crecimiento_reducido"] = sintomas["reduccion_vigor"]

sintomas["lesiones_tallo"] = preguntar(
    "¿Observa lesiones, cancros o agrietamientos en tallos?"
)

sintomas["daño_flores"] = preguntar(
    "¿Observa daño, deformación o caída de flores?"
)

sintomas["manchas_fruto"] = preguntar(
    "¿El fruto presenta manchas?"
)

sintomas["deformacion_fruto"] = preguntar(
    "¿El fruto presenta deformaciones?"
)

sintomas["cambios_color_fruto"] = preguntar(
    "¿El fruto presenta cambios anormales de coloración?"
)

sintomas["pudricion"] = preguntar(
    "¿Observa pudrición?"
)

sintomas["micelio"] = preguntar(
    "¿Observa micelio, esporulación o estructuras similares a hongos?"
)

sintomas["insectos"] = preguntar(
    "¿Observa insectos directamente en la planta?"
)

sintomas["presencia_ninfas"] = preguntar(
    "¿Observa ninfas, huevos o estados juveniles de insectos?"
)

sintomas["acaros"] = preguntar(
    "¿Observa ácaros?"
)

sintomas["mielecilla"] = preguntar(
    "¿Observa presencia de mielecilla?"
)

sintomas["fumagina"] = preguntar(
    "¿Observa fumagina?"
)

sintomas["punteaduras"] = preguntar(
    "¿Observa punteaduras cloróticas en las hojas?"
)

sintomas["bronceado"] = preguntar(
    "¿Observa bronceado del follaje?"
)

sintomas["galerias"] = preguntar(
    "¿Observa galerías dentro de las hojas?"
)

sintomas["perforaciones"] = preguntar(
    "¿Observa perforaciones o daños por alimentación?"
)

sintomas["daño_fruto"] = preguntar(
    "¿Observa daño directo en los frutos?"
)

sintomas["larvas"] = preguntar(
    "¿Observa larvas?"
)

sintomas["defoliacion"] = preguntar(
    "¿Existe defoliación prematura?"
)

sintomas["manchas"] = preguntar(
    "¿Observa manchas en hojas u otras partes de la planta?"
)

sintomas["necrosis_fruto"] = preguntar(
    "¿El fruto presenta lesiones necróticas?"
)

sintomas["manchas_circulares"] = preguntar(
    "¿Las manchas presentan forma circular?"
)

sintomas["humedad_alta"] = preguntar(
    "¿La humedad dentro del invernadero es alta?"
)



#Calculo de punts y procentajes

resultados = {}

for patologia, caracteristicas in patologias.items():

    puntos = 0
    puntos_maximos = sum(caracteristicas.values())

    for sintoma, peso in caracteristicas.items():

        if sintomas.get(sintoma, False):

            puntos += peso

    porcentaje = (puntos / puntos_maximos) * 100

    resultados[patologia] = {
        "puntos": puntos,
        "maximo": puntos_maximos,
        "porcentaje": porcentaje
    }


# Resultados y ordenarlos de mayor a menor puntuacion

resultados_ordenados = sorted(
    resultados.items(),
    key=lambda x: x[1]["porcentaje"],
    reverse=True
)

# Mostramos los resultados

print("\n==============================================")
print("                 RESULTADOS")

for i, (patologia, datos) in enumerate(resultados_ordenados[:5], 1):

    print(
        f"{i}. {patologia}: "
        f"{datos['porcentaje']:.1f}% "
    )


# Top 1 de patologias probables

principal = resultados_ordenados[0]

print("\n==============================================")

print("Patología con mayor coincidencia:")

print(principal[0])

print(
    f"Nivel de coincidencia: "
    f"{principal[1]['porcentaje']:.1f}%"
)

print("Los porcentajes representan coincidencia con los síntomas")
print("y no constituyen un diagnóstico definitivo.")
