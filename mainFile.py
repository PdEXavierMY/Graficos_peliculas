#-----------------------------------------------------------------------------------------
# @Autor: Aurélien Vannieuwenhuyze
# @Empresa: Junior Makers Place
# @Libro
# @Capítulo: 03 - Estadísticas para comprender los datos
#
# Módulos necesarios:
#   PANDAS 0.24.2
#   NUMPY 1.16.3
#   JMPEstadísticas (copiar el archivo dentro de su proyecto al mismo nivel que este archivo)
#
# Para instalar un módulo:
#   Haga clic en el menú File > Settings > Project:nombre_del_proyecto > Project interpreter > botón +
#   Introduzca el nombre del módulo en la zona de búsqueda situada en la parte superior izquierda
#   Elegir la versión en la parte inferior derecha
#   Haga clic en el botón install situado en la parte inferior izquierda
#-----------------------------------------------------------------------------------------

import pandas as pd
import JMPEstadisticas as jmp
import numpy as np
from introducir import solicitar_introducir_numero_extremo
import matplotlib.pyplot as plt

#--- CREACION DE UN DATAFRAME ----
def conseguircriticas():
    criticas = pd.read_csv("rotten_tomatoes_movies.csv", encoding = "UTF8", sep = ",")
    criticas = criticas.dropna(subset=["tomatometer_rating"])
    criticas = criticas.dropna(subset=["audience_rating"])
    critica_pro, critica_audiencia = list(criticas["tomatometer_rating"]), list(criticas["audience_rating"])
    return critica_pro, critica_audiencia

critica_pro, critica_audiencia = conseguircriticas()
observaciones_pro, observaciones_audiencia = pd.DataFrame({'NOTAS':np.array(critica_pro)}), pd.DataFrame({'NOTAS':np.array(critica_audiencia)})

#--- MAIN ---
if __name__ == "__main__":
    eleccion = solicitar_introducir_numero_extremo("Elige de quién quieres realizar las estadísticas(críticos=1, público=2 o las dos tablas a la vez(3))", 1, 3)
    stats1, stats2 = jmp.Estadisticas(observaciones_pro['NOTAS']), jmp.Estadisticas(observaciones_audiencia['NOTAS'])
    if eleccion == 1:
        stats1.analisisCaracteristica()
    elif eleccion == 2:
        stats2.analisisCaracteristica()
    elif eleccion == 3:
        #,media,mediana,cuartil_1,cuartil_2,cuartil_3:
        #de profesionales:
        media_pr = stats1.calculoMediaAritmetica()
        mediana_pr = stats1.calculoMediana()
        cuartil_pr = stats1.calculoDelosCuartiles(mediana_pr[0], mediana_pr[1])

        #de público:
        media_pu = stats2.calculoMediaAritmetica()
        mediana_pu = stats2.calculoMediana()
        cuartil_pu = stats2.calculoDelosCuartiles(mediana_pu[0], mediana_pu[1])

        jmp.Estadisticas([]).visualizarjunto(observaciones_pro['NOTAS'], observaciones_audiencia['NOTAS'], media_pr, mediana_pr, cuartil_pr, media_pu, mediana_pu, cuartil_pu)