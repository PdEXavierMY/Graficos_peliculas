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

#--- CREACION DE UN DATAFRAME ----
def conseguirnotas():
    criticas = pd.read_csv("rotten_tomatoes_movies.csv", encoding = "UTF8", sep = ",")
    criticas = criticas.dropna(subset=["tomatometer_rating"])
    criticas = criticas.dropna(subset=["audience_rating"])
    critica_pro, critica_audiencia = list(criticas["tomatometer_rating"]), list(criticas["audience_rating"])
    return critica_pro, critica_audiencia

critica_pro, critica_audiencia = conseguirnotas()
observaciones_pro, observaciones_audiencia = pd.DataFrame({'NOTAS':np.array(critica_pro)}), pd.DataFrame({'NOTAS':np.array(critica_audiencia)})
#observaciones = pd.DataFrame({'NOTAS':np.array([3,19,10,15,14,12,9,8,11,12,11,12,13,11,14,16])})

#--- ANALISIS DE UNA CARACTERISTICA ---
if __name__ == "__main__":
    eleccion = solicitar_introducir_numero_extremo("Elige de quién quieres realizar las estadísticas(críticos=1 o público=2)", 1, 2)
    stats1, stats2 = jmp.JMPEstadisticas(observaciones_pro['NOTAS']), jmp.JMPEstadisticas(observaciones_audiencia['NOTAS'])
    if eleccion == 1:
        stats1.analisisCaracteristica()
    elif eleccion == 2:
        stats2.analisisCaracteristica()