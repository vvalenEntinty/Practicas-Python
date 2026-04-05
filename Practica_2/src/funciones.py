def inicializar_resultados(rounds):
    resultados = {}
    for nombre in rounds[0]['scores']:
        resultados[nombre] = {
            'puntaje':0,
            'rondas_ganadas':0,
            'mejor_ronda':0,
            'promedio':0
        }
    return resultados

def procesar_ronda(ronda, resultados):
    puntajes_ronda = {}
    for nombre in ronda['scores']:
        puntaje_ronda = sum(ronda['scores'][nombre].values())
        resultados[nombre]['puntaje'] += puntaje_ronda
        if puntaje_ronda > resultados[nombre]['mejor_ronda']:
            resultados[nombre]['mejor_ronda'] = puntaje_ronda
        puntajes_ronda[nombre] = puntaje_ronda
    max_puntaje = max(puntajes_ronda.values())
    ganador = max(puntajes_ronda, key=lambda n: puntajes_ronda[n])
    resultados[ganador]['rondas_ganadas'] += 1
    return ganador, max_puntaje, puntajes_ronda    

def calcular_promedios(resultados, total_rondas):
    for nombre in resultados:
        resultados[nombre]['promedio'] = resultados[nombre]['puntaje'] / total_rondas if total_rondas > 0 else 0