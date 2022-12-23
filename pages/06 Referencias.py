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

st.write("# REFERENCIAS") 

components.html(
    """
    
<center><img src="https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png"></center><br/>

    """,height=20,
)


st.markdown("""
- Isotalo, J. Basics of Statistics. Retrieved August 25, 2016, from http://www.mv.helsinki.fi/home/jmisotal/BoS.pdf
- José Alquicira. (2017). Análisis de correlación. 2022, Diciembre 5, Conogasi.org Sitio web: https://conogasi.org/articulos/analisis-de-correlacion-2/
- ¿Qué es el coeficiente de correlación de Pearson?, from https://www.questionpro.com/blog/es/coeficiente-de-correlacion-de-pearson/
- Cómo se interpreta el coeficiente de correlación de Pearson, from https://www.cimec.es/coeficiente-correlacion-pearson/ 
""")


components.html(
    """
    
<center><img src="https://user-images.githubusercontent.com/19308295/115926252-2b8a0c00-a448-11eb-9d9c-b43beaf0ff68.png"></center><br/>

    """,height=20,
)

