import streamlit as st
st.set_page_config(
    page_title="Carátula",
    page_icon="👋",
)

st.write("# Hola Arnold! 👋")

st.sidebar.success("Selecciona.")


#!/usr/bin/env python
# coding: utf-8
import streamlit as st
import streamlit.components.v1 as components

st.markdown('Streamlit is **_really_ cool**.')

components.html(
    """
<center><img src="https://user-images.githubusercontent.com/19308295/115926252-2b8a0c00-a448-11eb-9d9c-b43beaf0ff68.png"></center><br/>
<br/>
<center><font face = "MingLiU" size = 5 ><b> UNIVERSIDAD NACIONAL DE SAN AGUSTÍN DE AREQUIPA </b></font><br/>
<center><font face = "MingLiU" size = 3.5 > FACULTAD DE PRODUCCIÓN Y SERVICIOS </font><br/>
<center><font face = "MingLiU" size = 4 ><b> ESCUELA PROFESIONAL DE INGENIERÍA EN TELECOMUNICACIONES </b></font><br/>
<br/>

<center><img src="https://empleoz.com/media/logo/592546c81ca7507c29e72496.png"></center><br/>
    

<center><font face = "MingLiU" size = 5 ><b> Ingeniero Renzo Bolivar - Docente DAIE </b></font><br/>
<center><font face = "MingLiU" size = 5 ><b> Curso : Computación 1 </b></font><br/>
<br/>

<center><img src="https://user-images.githubusercontent.com/19308295/115926252-2b8a0c00-a448-11eb-9d9c-b43beaf0ff68.png"></center><br/>

<center><font face = "MingLiU" size = 5 ><b> GRUPO D - Nº 2 </b></font><br/></center> 

<center><font face = "MingLiU" size = 5 ><b>Alumnos: </b></font><br/></center>
 
<center> Arnold Jhony Jara Esteban <br/></center> 
<center><font face = "MingLiU" size = 3 > Maycol Denne Ccolque Hilario </font><br/></center>
<center><font face = "MingLiU" size = 3 > Diego Sanguinetti Rodríguez </font><br/></center>
<center><font face = "MingLiU" size = 3 > Jared Valenzuela Menendez </font><br/></center>
<center><font face = "MingLiU" size = 3 > Brahian David Chipa Tejada </font><br/></center>
<center><font face = "MingLiU" size = 3 > Kusi Lucero Valero Arizabal </font><br/></center>
<center><font face = "MingLiU" size = 3 > Mayta Llacma Delfor Paul </font><br/></center>
<br/>
 
<center><img src="https://user-images.githubusercontent.com/19308295/115926252-2b8a0c00-a448-11eb-9d9c-b43beaf0ff68.png"></center><br/>

<center> <h1>INVESTIGACIÓN FORMATIVA</h1> </center> 
<center> <h1>PROYECTO FINAL</h1> </center> 
<center> <h1>PYTHON - Inteligencia Artificial</h1> </center>
<center><img src="https://user-images.githubusercontent.com/19308295/115926252-2b8a0c00-a448-11eb-9d9c-b43beaf0ff68.png"></center><br/>
""",
    height=1000,
)

