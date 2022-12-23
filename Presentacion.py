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
<center><font face = "MingLiU" size = 5 color = white ><b> UNIVERSIDAD NACIONAL DE SAN AGUSTÍN DE AREQUIPA </b></font><br/>
<center><font face = "MingLiU" size = 3.5 color = white  > FACULTAD DE PRODUCCIÓN Y SERVICIOS </font><br/>
<center><font face = "MingLiU" size = 4 color = white  ><b> ESCUELA PROFESIONAL DE INGENIERÍA EN TELECOMUNICACIONES </b></font><br/>
<br/>

<center><img src="https://upload.wikimedia.org/wikipedia/commons/f/f9/Escudo_UNSA.png" width="120" height="150"></center><br/>
    

<center><font face = "MingLiU" size = 5 color = white  ><b> Ingeniero Renzo Bolivar - Docente DAIE </b></font><br/>
<center><font face = "MingLiU" size = 5 color = white ><b> Curso : Computación 1 </b></font><br/>
<br/>

<center><img src="https://user-images.githubusercontent.com/19308295/115926252-2b8a0c00-a448-11eb-9d9c-b43beaf0ff68.png"></center><br/>

<center><font face = "MingLiU" size = 5 color = white  ><b> GRUPO D - Nº 2 </b></font><br/></center> 

<center><font face = "MingLiU" size = 5 color = white  ><b>Alumnos: </b></font><br/></center>
 
<center><font face = "MingLiU" size = 4 color = white > Arnold Jhony Jara Esteban </font><br/></center> 
<center><font face = "MingLiU" size = 3 color = white > Maycol Denne Ccolque Hilario </font><br/></center>
<center><font face = "MingLiU" size = 3 color = white > Diego Sanguinetti Rodríguez </font><br/></center>
<center><font face = "MingLiU" size = 3 color = white > Jared Valenzuela Menendez </font><br/></center>
<center><font face = "MingLiU" size = 3 color = white > Brahian David Chipa Tejada </font><br/></center>
<center><font face = "MingLiU" size = 3 color = white > Kusi Lucero Valero Arizabal </font><br/></center>
<center><font face = "MingLiU" size = 3 color = white > Mayta Llacma Delfor Paul </font><br/></center>
<br/>
 
<center><img src="https://user-images.githubusercontent.com/19308295/115926252-2b8a0c00-a448-11eb-9d9c-b43beaf0ff68.png"></center><br/>

<center> <h1> <font face color = white >INVESTIGACIÓN FORMATIVA</h1> </font> </center> 
<center> <h1> <font face color = white >PROYECTO FINAL</h1> </font> </center> 
<center> <h1> <font face color = white >PYTHON - Inteligencia Artificial</h1> </font> </center>
<center><img src="https://user-images.githubusercontent.com/19308295/115926252-2b8a0c00-a448-11eb-9d9c-b43beaf0ff68.png"></center><br/>
""",
    height=1000,
)

