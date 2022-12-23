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

st.write("# BASE TEÓRICA") 

components.html(
    """
    
<center><img src="https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png"></center><br/>

    """,height=20,
)


st.markdown("""
### OBJETIVOS
Los Objetivos de la investigación formativa son:
 
- **Competencia Comunicativa** Presentación de sus resultados con lenguaje de programación Python utilizando los archivos Jupyter Notebook.
- **Competencia Aprendizaje**: con las aptitudes en **Descomposición** (desarticular el problema en pequeñas series de soluciones), **Reconocimiento de Patrones** (encontrar simulitud al momento de resolver problemas), **Abstracción** (omitir información relevante), **Algoritmos** (pasos para resolución de un problema).
- **Competencia de Trabajo en Equipo**: exige habilidades individuales y grupales orientadas a la cooperación, planificación, coordinación, asignación de tareas, cumplimiento de tareas y solución de conflictos en pro de un trabajo colectivo, utilizando los archivos Jupyter Notebook los cuales se sincronizan en el servidor Gitlab con comandos Git.
""")
components.html(
    """
<center><img src="https://user-images.githubusercontent.com/19308295/115926252-2b8a0c00-a448-11eb-9d9c-b43beaf0ff68.png"></center><br/>

<center> <h1><font face = "MingLiU" size = 6 color = white  > Aplicación en IA</h1></font> </center> 
<center> <h1><font face = "MingLiU" size = 6 color = white  > Sistema Recomendador</h1> </font></center> 
<font face = "MingLiU" size = 3 color = white >
Un sistema de recomendación es una herramienta que establece un conjunto de criterios y valoraciones sobre los datos de los usuarios para realizar predicciones sobre recomendaciones de elementos que puedan ser de utilidad o valor para el usuario. Estos sistemas seleccionan datos proporcionados por el usuario de forma directa o indirecta, y procede a analizar y procesar información del historial del usuario para transformar estos datos en conocimiento de recomendación.
</font><br/>

<font face = "MingLiU" size = 3 color = white > 
La compatibilidad o similitud será encontrada con el algoritmo de Correlación de Pearson y será verificada con la La Matrix de Correlación de Pearson con una librería de Python y utilizando una función personal.</font>

<center><img src="https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png"></center><br/>

<center> <font face = "MingLiU" size = 5 color = white  > <h1>Base Teórica</h1> </font>  </center> 

""",height=470,
)

st.markdown(
    """
   
    ### Análisis de Correlación

El **análisis de correlación** es el primer paso para construir modelos explicativos y predictivos más complejos.

El análisis de correlación consiste en un procedimiento estadístico para determinar si dos variables están relacionadas o no. El resultado del análisis es un coeficiente de correlación que puede tomar valores entre -1 y +1. El signo indica el tipo de correlación entre las dos variables . Un signo positivo indica que existe una relación positiva entre las dos variables; es decir, cuando la magnitud de una incrementa, la otra también. Un signo negativo indica que existe una relación negativa entre las dos variables. Mientras los valores de una incrementan, los de la segunda variable disminuyen. Si dos variables son independientes, el coeficiente de correlación es de magnitud cero . La fuerza de la relación lineal incrementa a medida que el coeficiente de correlación se aproxima a -1 o a +1.



A menudo nos interesa observar y **medir la relación entre 2 variables numéricas** mediante el análisis de correlación. 
Se trata de una de las *técnicas más habituales en análisis de datos* y el primer paso necesario antes de construir cualquier **modelo explicativo o predictivo más complejo**.
Para poder tener el  Datset hay que recolectar información a travez de encuentas.


### ¿Qué es la correlación?

La correlación es un tipo de asociación entre dos variables numéricas, específicamente evalúa la **tendencia (creciente o decreciente) en los datos**.

Dos variables están asociadas cuando una variable nos da información acerca de la otra. Por el contrario, cuando no existe asociación, el aumento o disminución de una variable no nos dice nada sobre el comportamiento de la otra variable.
 
Dos variables ***se correlacionan cuando muestran una tendencia creciente o decreciente***.

### Como se clasifica la correlacion 

La correlación trata de establecer la relación o dependencia que existe entre las dos variables que intervienen en una distribución bidimensional 
Es decir, determinar si los cambios en una de las variables influyen en los cambios de la otra. En caso de que suceda, diremos que las variables están correlacionadas o que hay correlación entre ellas.

### Tipos de Correlacion

1. **Correlación directa**

La correlación directa se da cuando al aumentar una de las variables la otra aumenta.
 
La recta correspondiente a la nube de puntos de la distribución es una recta creciente
""")
components.html(
    """
    
<center><img src="https://www.superprof.es/apuntes/wp-content/uploads/2019/05/estadistica-correlacion.gif"></center><br/>

    """,height=200,
)
st.markdown("""
2. **Correlación inversa**
 
 
 La correlación inversa se da cuando al aumentar una de las variables la otra disminuye.
 
 La recta correspondiente a la nube de puntos de la distribución es una recta decreciente.
""")
components.html(
    """
    <center><img src="https://www.superprof.es/apuntes/wp-content/uploads/2019/05/estadistica-correlacion-2.gif"></center><br/>
    """,height=200,
)
st.markdown(""" 
 3. **Correlación nula**
 
 
 La correlación nula se da cuando no hay dependencia de ningún tipo entre las variables.
 
 En este caso se dice que las variables son incorreladas y la nube de puntos tiene una forma redondeada.
 
""")
components.html(
    """
    <center><img src="https://www.superprof.es/apuntes/wp-content/uploads/2019/05/estadistica-correlacion-3.gif"></center><br/>

    """,height=200,
)
st.markdown(""" 

### ¿Cómo se mide la correlación?

Tenemos el coeficiente de **correlación lineal de Pearson** que se *sirve para cuantificar tendencias lineales*, y el **coeficiente de correlación de Spearman** que se utiliza para *tendencias de aumento o disminución, no necesariamente lineales pero sí monótonas*. 

### Correlación de Pearson

El coeficiente de correlación lineal de Pearson mide una tendencia lineal entre dos variables numéricas.

Es el método de correlación más utilizado, pero asume que:
 
- La tendencia debe ser de tipo lineal.
- No existen valores atípicos (outliers).
- Las variables deben ser numéricas.
- Tenemos suficientes datos (algunos autores recomiendan tener más de 30 puntos u observaciones).

Los dos primeros supuestos se pueden evaluar simplemente con un diagrama de dispersión, mientras que para los últimos basta con mirar los datos y evaluar el diseño que tenemos.

### Cómo se interpreta la correlación

El signo nos indica la dirección de la relación, como hemos visto en el diagrama de dispersión.
- un valor positivo indica una relación directa o positiva,
- un valor negativo indica relación indirecta, inversa o negativa,
- un valor nulo indica que no existe una tendencia entre ambas variables (puede ocurrir que no exista relación o que la relación sea más compleja que una tendencia, por ejemplo, una relación en forma de U).

La magnitud nos indica la fuerza de la relación, y toma valores entre $-1$ a $1$. Cuanto más cercano sea el valor a los extremos del intervalo ($1$ o $-1$) más fuerte será la tendencia de las variables, o será menor la dispersión que existe en los puntos alrededor de dicha tendencia. Cuanto más cerca del cero esté el coeficiente de correlación, más débil será la tendencia, es decir, habrá más dispersión en la nube de puntos.
- Un valor menor que 0 indica que existe una correlación negativa, es decir, que las dos variables están asociadas en sentido inverso. Cuánto más se acerca a -1, mayor es la fuerza de esa relación invertida (cuando el valor en una sea muy alto, el valor en la otra será muy bajo). Cuando es exactamente -1, eso significa que tienen una correlación negativa perfecta.
- Un valor mayor que 0 indica que existe una correlación positiva. En este caso las variables estarían asociadas en sentido directo. Cuanto más cerca de +1, más alta es su asociación. Un valor exacto de +1 indicaría una relación lineal positiva perfecta.
- Finalmente, una correlación de 0, o próxima a 0, indica que no hay relación lineal entre las dos variables.
""")
components.html(
    """

<center><img src="https://user-images.githubusercontent.com/25250496/204172549-2ccf3be3-a2b3-4b49-9cd4-adb66e28621d.png" width="500" height="150"></center>

<center> <h3>Fórmula Coeficiente de Correlación de Pearson</h3> </center>  
<center> <h3> </h3> </center> 
    """,height=200,
)
components.html(
    """
    <center><img src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHCBUWFBgVFRUZGBgZGhgcGhgYGhgeGBoaHBkaHBocHBgcIS4lHh4tHxgcJjgmLC8xNUM1GiQ7QDszPy40NTEBDAwMBgYGEAYGEDEdFh0xMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMf/AABEIAHUBsAMBIgACEQEDEQH/xAAbAAEAAgMBAQAAAAAAAAAAAAAABQYBAwQCB//EAEcQAAIBAwICBQkFBgQDCQEAAAECAAMEERIhBTEGE0FRlBUWIlJUYYHS0xQjMnGRBzNCYqGxQ3KT0WOSslN0oqOkwcPi8DT/xAAUAQEAAAAAAAAAAAAAAAAAAAAA/8QAFBEBAAAAAAAAAAAAAAAAAAAAAP/aAAwDAQACEQMRAD8A+zREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERA5ruoVRmVS7BSQoOCxA5Z75U+BdMK92jPQschWZXVrhFdWXYqylcgy5mfP+K27WHEqdxRUtRvGFOtSXsqfw1FX+8CY4X0jq1qte3No1OrRVGCtVUh9ZIUhgNl9Eknc7cszk4d0wq1VtX+zgU7iq1Et1mTqUv6SDT6VPCE5ODvy7ZZ7qyVtbKAtR0KdYANQGDp/MAnOJBW/RtNFqlG4ZfseU1KEJYhND6gchW3J5bZMC1xMCeS45ZGYHJxLiNOgmuo2FyAAASzMThVVRuzE9gnHxPjtO3ofaKy1EQY1DRl1z2sFJxIi4freMU6bbrbWzVVHYalRymrHeFXY/zHvk30jWk1tWWsQEZGU57yMDA7TnG0DRxDpHSorQZ1qZuGC01VCzFiMgFQdjjf8AWdd1xWnTq0aDkh62vQoGc6ACxJ7AMj9ZVf2d02rIK9wxetQzbqrDBpBcBiR67jSxPdgSStLys/Fa1IVWNClQplkwmkVXY4GoLq/AAcEnnAtUTmvLlaaM7Z0qMnSCT8FG5kP53W3/ABv9Ct8kCwSI6ScUW3t3qszIoH41TXoz/EV7RN3C+K06+TT1+jjOtHTn3awCZ56QrSNtVWsQKbIytn3jAwO05xgQKxf8SuaK0Xe8b78haarZhnLFdQBUVMjbf4HMstHiq9d9nfWtTGV1qAKoAGpqZBIOM7rsR2jG8q/7PKbVkFauxarb5t0RgQaQTALFT/iOArMe7AHbJT9oKYszWXZ6DpVRu1SrjVj80LL+TGBYby6SmjVKjBUUEszHAAEhr7pTRo0Er1adZEdwqZpnUSfwZUHKhuQ1YPeBODpHU6644fQb8Duazr2NoTUg+DlT8J29PbAV+HXKciKbOp22an6akHs3THxgdfGeO0rYUzUWoetcIgRCzayMhSByOAfdtN95xanSeijkh67aUXGTqCljnHLYGQfRfVdinfVlK5Reopn+HUo6yqcfxMcgdyjvYzct5VbihorUbqqduHqU8Jp1u2EIbTq5K22e6BZxMznuLhURnbOlRk4BJx7gNzIcdLbb/jf6Ff5IFglc6V8aFAU0DtTes6ojrS61SxONJGQATnt7pI8N4tTr6ur1+jjOunUTn3a1GfhIL9pVAmwequA9u1OuhPY1N1P9sj9IGu8vri3r0KdW6LmqxCIlqDq041AsH9HAPPlJ+14qj1GokMlRN9DjBZc4DqRkMvvB27cTg4BbtVb7dVXS1RAKKHnSon0gD3O2zNj3DsnJ04PV/Zbhfxpc01HvWq2hlPePSzjvAgW0TMwJmAiIgIiICIiAiIgIiICYzBkN0iuKtO3d6TohRWZnqKWAVVJ2UEZOcDc8t94EzmR3lq36/wCzdYOuxq6vDatPrcuXvkPwS7vq629cmlTpuoapTKtrKlThg2SAdWPR7u3skL07vTbXlrcUWQVXV7dg+dIp1GUJUbHJFqFSc/lAtvnHa5qjrl+4z1uzfd4ODq22mwcbt+o+09avU4z1m+nHfy5e+c/DOBpRt2o/iLhjVdvxVHb8bse893YMDslR6K03uaC2DqRStnenXY/4io3oID2hhhm/SB9As7xKqK9NtSsMq2CMjvGROmalXAAGwGAB2DuEjL+reh8UKVsyYG9WtURs9owtJhj4wJiYlfFfieRmhZ4yM4uK5OO3A6gbybaoFUs22AScZPIZOMDJgbola897L163hbv6Uz572Xr1vC3f0oFkiVvz3svXreFu/pR572Xr1vC3f0oFkiVvz3svXreFu/pR572Xr1vC3f0oE7XrKis7MFVQSSeQA7c/CUfg/HLa4rteVq9NQuUt6bOPRTOGcj1m/tJat0wsXUqxqspGCrWl2QR3EdVvODyvwf8A7D/0Nz9GB323SqlVuLinTZGp0KK1Hqqc4Y6zju2C5nLwe6qLwyjVZ0pVaoWo79WzLqqnXuib6irDeeU47wtVdFRlWopVwtndLrUggg4pbjBP6z3wzpHw23pilS61UXkPs14eQAG7UyTsBA98M4tUaqitd03BO6rb1FLbdjHYTzc0NHGLchmJe3uSdTEjZ6eMDkMAkTq89LH1qvhLv6UjLji3DHrrXLXPWoCqsKXEBpViCyhQmADgbYgdfF0+z8Ro3h/dVKZt6rdiNq1U2P8AKSWUns2nfd8Nq1bqnUZkNtTBK08HJqbaXJzg43wPfmc1TplYsCrGqynYg2t2QfgaU80Ol9iihENVVXYKLS7AA7gOqgb+D8FrUby5rak6quVbQAdSuoxqzncsOf5CZ4dwOrSvLmuKilLh0crpOoaKegLnOMdufhMee9l69bwt39KPPey9et4W7+lAscSuee9l69bwt39KPPey9et4W7+lAsRzIG94XWq3NN3dDb08kUsHU1TbS7HODjfA9+Zr897L163hbv6Uee9l69bwt39KA4TwatRvLmvrTqq5VurAbUrqMas8iWHP8hOfps/W01sqZzVrumQN9NJXDVHbuXSCue9hN56bWR/jreEu/pTno9KuHozMvWBnOWYWl3lj7z1W8DPSq2NN7W6UErbPpcAZPVOugt+SnDH3LO/pDZvd2dSlb1EHXIV6w5ZdDDDEY55H95ynprZH+KqR/wB1uz/8U1WvS3h9MFU6xASThbS7AyTknApQJ3g9maNClSOPu6aJ6OcYRQowD7hIy34JVS9q3AqJoqinqUqS4Cg+iGzjTk55Tz572Xr1vC3f0o897L163hbv6UCwgT0JXPPey9et4W7+lHnvZevW8Ld/SgWMiV3prwWreWj21J1p69IZmBPoqwbAAPaRiY897L163hbv6Uee9l69bwt39KBP0FwqggAgDYchtyHulW6UAXNe3tEOdNVK1Yj+BaZ1Jn3lwBjuz3ToPTay9et4S7+lNFv0r4emrR1i6jltNpdjJPMn7reBbBMyt+e9l61bwl39KPPey9et4W7+lAskSt+e9l69bwt39KPPey9et4W7+lAskSt+e9l69bwt39KPPey9et4W7+lAskSt+e9l69bwt39KWPMDMREBERASD6W2FWvaVKFI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EGQKBn3MxPwlq6hfVH6COqXuH6DlAqPAL5jY1LkuiNVqVGWoaZbNMVClNmVN2JRRv754teN1GdAb2m2WUFRa1QSM7gE8vzlj4TwWhbJ1dBNC5zjLN37ZYk4GTgchJDqxAqHSegFveHvqbLXDgjUdOBQqHAXlz3+M6Ollsy1ba9RSxt3cVFUEsaNUBahUDmQQrfkDJPiPAKFd0qVA5amdSFatVQjYxlQrAA4Mkwm2Phvv+uecCE45Zi+s2p0ayhKq4LgasqeeMHnJWxoFKaISCVUDKjAOBjYdk206YUYUAZJOwxue2bYFfsOANSu69wtY6a7IzJpGdS09ABfnpwM475PaZ6iBgCMTMQIDpTwR7qmtNagpqHR2ypbVoYMF5jYkbybpg4GeeBy5fCbIgU/jJF5dUKFM6koVRWruu6AorBKerkWLMCQOQG/OW/E1U6KqMKAo7gABvN0DGJmIgIiICIiAiIgIiICIiAiIgJgzMQI3jfDEuaFSg49F1I94PYw94OCJGdBOFVra0FOu2qprcls51DOFOf8AKBLIRAEDMREBERAREQEREBERAREQEREBERAREQIPpXwQXdq9HOltmpv2pUXdGHx2PuJnnodY1KFlRpVf3iqS/I+mzM7bjmcsZOwBAzERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERA//Z"width="290" height="85" > ></center><br/>

    """,height=110,
)
st.markdown("""

**Distancia Euclidiana**: La distancia euclidiana es la generalización del __`teorema de Pitágoras`__.
 
Las herramientas de distancia euclidiana describen la relación de cada celda con un origen o un conjunto de orígenes basándose en la distancia de la línea recta. Existen tres herramientas euclidianas: Distancia euclidiana proporciona la distancia desde cada celda en el ráster hasta el origen más cercano.


$$d_{E}(x,y)=\sqrt{\sum_{i=1}^{n}(x_{i}-y_{i})^{2}}$$

"""
)

components.html(
    """
    
<center><img src="https://www.superprof.es/apuntes/wp-content/uploads/2019/05/estadistica-correlacion.gif"></center><br/>

    """,height=200,
)


components.html(
    """
    
<center><img src="https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png"></center><br/>

    """,height=20,
)
