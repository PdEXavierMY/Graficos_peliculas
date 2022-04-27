# Graficos_peliculas

Link de kaggle al [csv](https://www.kaggle.com/datasets/stefanoleone992/rotten-tomatoes-movies-and-critic-reviews-dataset)

Link al [repositorio](https://github.com/Xavitheforce/Graficos_peliculas)
***

En este ejercicio he reutilizado el código proporcionado en Notas con las funciones necesarias para calcular una estadística de datos(media, moda, mediana, cuartiles) a partir de un dataset panda. Simplemente he ajustado el main para que reciba un dataset(link en la parte superior) y saque las columnas que interesan en forma de lista. A partir de esa lista, pandas crea un dataset y lo pasa por el archivo JMPEstadísticas.

```python
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
```
