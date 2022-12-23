import streamlit as st
import time
import numpy as np
import streamlit.components.v1 as components

st.set_page_config(page_title="Base Teorica", page_icon="📈")

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()

for i in range(1, 101):
    status_text.text("%i%% Completado" % i)
    progress_bar.progress(i)

progress_bar.empty()
st.button("Reiniciar")

# #######################################################################################################################################################################
components.html(
    """
    
<center><img src="https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png"></center><br/>

    """,height=20,
)

st.write("# CONCLUSIONES") 

components.html(
    """
    
<center><img src="https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png"></center><br/>

    """,height=20,
)

st.markdown("""**¿Se valido o no los resultados?**

> Se considera que los resultados de la investigación son válidos pero el estudio nunca está libre de errores. """)

st.markdown("""**Los resultados validados son:**
> 1.- raf1t0mendoza@gmail.com y betzy.romen@gmail.com obtienen el PRIMER índice más alto de similitud con un porcentaje de 78/100

> 2.- dvillagrac@unsa.edu.pe y floresgarnicaedwinmaycol@gmail.com obtienen el SEGUNDO índice más alto de similitud con un porcentaje de 72/100""")

st.markdown("""**¿Es efectivo el metodo de correlación de pearson?**

> En estadística, el coeficiente de correlación de Pearson es una medida de dependencia lineal entre dos variables aleatorias cuantitativas. A diferencia de la covarianza, la correlación de Pearson es independiente de la escala de medida de las variables.

> De manera menos formal, podemos definir el coeficiente de correlación de Pearson como un índice que puede utilizarse para medir el grado de relación de dos variables siempre y cuando ambas sean cuantitativas y continuas mostrando asi su efectividad.

> En esta oportunidad se logro con el objetivo que era lograr validad los datos mediante dos caminos, y demostrar la efectividad de ambos.""")

st.markdown("""**Correlación de Pearson y Regresión Lineal, ¿cual es su relación?**

> La correlación cuantifica como de relacionadas están dos variables, mientras que la regresión lineal consiste en generar una ecuación (modelo) que, basándose en la relación existente entre ambas variables, permita predecir el valor de una a partir de la otra.""")

import streamlit.components.v1 as components
components.html(
    """
    
<center><img src="https://estadisticaitm.github.io/reg_files/figure-html/unnamed-chunk-2-1.png" width="290" height="390"></center>

    """,height=140,
)
components.html(
    """
    
<center><img src="https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png"></center><br/>

    """,height=20,
)

