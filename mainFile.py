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
#observaciones = pd.DataFrame({'NOTAS':np.array([3,19,10,15,14,12,9,8,11,12,11,12,13,11,14,16])})

#--- ANALISIS DE UNA CARACTERISTICA ---
if __name__ == "__main__":
    eleccion = solicitar_introducir_numero_extremo("Elige de quién quieres realizar las estadísticas(críticos=1, público=2 o las dos tablas a la vez(3))", 1, 3)
    stats1, stats2 = jmp.JMPEstadisticas(observaciones_pro['NOTAS']), jmp.JMPEstadisticas(observaciones_audiencia['NOTAS'])
    if eleccion == 1:
        stats1.analisisCaracteristica()
    elif eleccion == 2:
        stats2.analisisCaracteristica()
    elif eleccion == 3:
        #,media,mediana,cuartil_1,cuartil_2,cuartil_3:
        #de profesionales:
        media_pr = stats1.calculoMediaAritmetica
        mediana_pr = stats1.calculoMediana
        cuartil1_pr = stats1.calculoDelosCuartiles
        cuartil2_pr = stats1.calculoDelosCuartiles
        cuartil3_pr = stats1.calculoDelosCuartiles

        #de público:
        media_pu = stats2.calculoMediaAritmetica
        mediana_pu = stats2.calculoMediana
        cuartil1_pu = stats2.calculoDelosCuartiles
        cuartil2_pu = stats2.calculoDelosCuartiles
        cuartil3_pu = stats2.calculoDelosCuartiles

        print(media_pr, media_pu, mediana_pr, mediana_pu, cuartil1_pr, cuartil1_pu, cuartil2_pr, cuartil2_pu, cuartil3_pr, cuartil3_pu)

        plt.subplot(4, 2, 1)
        plt.hist(observaciones_pro['NOTAS'])
        plt.title("Histograma y media(profesionales)")
        plt.axvline(media_pr, color='red', linestyle='dashed', linewidth=1,label = str(media_pr))
        plt.legend(loc='upper right')

        plt.subplot(4, 2, 2)
        plt.hist(observaciones_pro['NOTAS'])
        plt.title("Histograma y mediana(profesionales)")
        plt.axvline(mediana_pr[0], color='green', linestyle='dashed', linewidth=1,label = str(mediana_pr[0]))
        plt.legend(loc='upper right')

        plt.subplot(4, 2, 3)
        plt.hist(observaciones_pro['NOTAS'])
        plt.title("Histograma y cuartiles(profesionales)")
        plt.axvline(cuartil1_pr[0], color='orange', linestyle='dashed', linewidth=1,label = "Q1: "+str(cuartil1_pr[0]))
        plt.axvline(cuartil2_pr[1], color='orange', linestyle='dashed', linewidth=1,label = "Q2: "+str(cuartil2_pr[1]))
        plt.axvline(cuartil3_pr[2], color='orange', linestyle='dashed', linewidth=1,label = "Q3: "+str(cuartil3_pr[2]))
        plt.legend(loc='upper right')

        plt.subplot(4, 2, 4)
        plt.boxplot(observaciones_pro['NOTAS'])
        plt.title("Diagrama de caja y bigotes(profesionales)")
        plt.show()

        plt.subplot(4, 2, 5)
        plt.hist(observaciones_audiencia['NOTAS'])
        plt.title("Histograma y media(público)")
        plt.axvline(media_pu, color='red', linestyle='dashed', linewidth=1,label = str(media_pu))
        plt.legend(loc='upper right')

        plt.subplot(4, 2, 6)
        plt.hist(observaciones_audiencia['NOTAS'])
        plt.title("Histograma y mediana(público)")
        plt.axvline(mediana_pu[0], color='green', linestyle='dashed', linewidth=1,label = str(mediana_pu[0]))
        plt.legend(loc='upper right')

        plt.subplot(4, 2, 7)
        plt.hist(observaciones_audiencia['NOTAS'])
        plt.title("Histograma y cuartiles(público)")
        plt.axvline(cuartil1_pu[0], color='orange', linestyle='dashed', linewidth=1,label = "Q1: "+str(cuartil1_pu[0]))
        plt.axvline(cuartil2_pu[1], color='orange', linestyle='dashed', linewidth=1,label = "Q2: "+str(cuartil2_pu[1]))
        plt.axvline(cuartil3_pu[2], color='orange', linestyle='dashed', linewidth=1,label = "Q3: "+str(cuartil3_pu[2]))
        plt.legend(loc='upper right')

        plt.subplot(4, 2, 8)
        plt.boxplot(observaciones_audiencia['NOTAS'])
        plt.title("Diagrama de caja y bigotes(público)")
        plt.show()