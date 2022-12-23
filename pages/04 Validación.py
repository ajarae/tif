import streamlit as st
import time
import numpy as np
import streamlit.components.v1 as components
import pandas as pd
#import matplotlib.pyplot as plt
#import matplotlib
#import seaborn as sns
#from scipy.spatial.distance import euclidean

st.set_page_config(page_title="Validación", page_icon="📈")

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
# last_rows = np.random.randn(5, 1)
# chart = st.line_chart(last_rows)

for i in range(1, 101):
    # new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    status_text.text("%i%% Completado" % i)
    # chart.add_rows(new_rows)
    progress_bar.progress(i)
    # last_rows = new_rows
    # time.sleep(0.05)

progress_bar.empty()

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# Reboot.
st.button("Reiniciar")

# #######################################################################################################################################################################


data = pd.read_csv('Lugares_T.csv')

components.html(
    """
    
<center><img src="https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png"></center><br/>

    """,height=20,
)

st.write("# VALIDACIÓN") 

components.html(
    """
    
<center><img src="https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png"></center><br/>

    """,height=20,
)

st.write("## Validación Matriz de Correlación")

code="""
values = data[data.columns[1:]].to_numpy()
email = data[data.columns[0]].to_numpy()

#Filas desde [1:] en adelante
print(values)

#Columna de Correos [0] 
print(email)

#Extracción de datos, en columnas
#data
"""
st.code(code, language='python')

values = data[data.columns[1:]].to_numpy()
email = data[data.columns[0]].to_numpy()
#Filas desde [1:] en adelante
st.write(values)
#Columna de Correos [0] 
st.write(email)
#Extracción de datos, en columnas
#data

code="""
#Reemplazamos los valores en "0" por columna en "data",para evitar los NAN, por su moda
data.isnull().sum()
for i in data.columns[1:]:
    data[i].fillna(data[i].mean(), inplace=True)
data.isnull().sum()
"""
st.code(code, language='python')

data.isnull().sum()
for i in data.columns[1:]:
    data[i].fillna(data[i].mean(), inplace=True)
st.write(data.isnull().sum())

components.html(
   """
<center><font size = 5 color = white  ><b> Fórmula Coeficiente de Correlación de Pearson </b></font></center> <br/>

    """,height=40,
)

components.html(
    """
    <center><img src="data:image/jpeg;base64,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XUqxqspGCrWl2QR3EdVvODyvwf8A7D/0Nz9GB323SqlVuLinTZGp0KK1Hqqc4Y6zju2C5nLwe6qLwyjVZ0pVaoWo79WzLqqnXuib6irDeeU47wtVdFRlWopVwtndLrUggg4pbjBP6z3wzpHw23pilS61UXkPs14eQAG7UyTsBA98M4tUaqitd03BO6rb1FLbdjHYTzc0NHGLchmJe3uSdTEjZ6eMDkMAkTq89LH1qvhLv6UjLji3DHrrXLXPWoCqsKXEBpViCyhQmADgbYgdfF0+z8Ro3h/dVKZt6rdiNq1U2P8AKSWUns2nfd8Nq1bqnUZkNtTBK08HJqbaXJzg43wPfmc1TplYsCrGqynYg2t2QfgaU80Ol9iihENVVXYKLS7AA7gOqgb+D8FrUby5rak6quVbQAdSuoxqzncsOf5CZ4dwOrSvLmuKilLh0crpOoaKegLnOMdufhMee9l69bwt39KPPey9et4W7+lAscSuee9l69bwt39KPPey9et4W7+lAsRzIG94XWq3NN3dDb08kUsHU1TbS7HODjfA9+Zr897L163hbv6Uee9l69bwt39KA4TwatRvLmvrTqq5VurAbUrqMas8iWHP8hOfps/W01sqZzVrumQN9NJXDVHbuXSCue9hN56bWR/jreEu/pTno9KuHozMvWBnOWYWl3lj7z1W8DPSq2NN7W6UErbPpcAZPVOugt+SnDH3LO/pDZvd2dSlb1EHXIV6w5ZdDDDEY55H95ynprZH+KqR/wB1uz/8U1WvS3h9MFU6xASThbS7AyTknApQJ3g9maNClSOPu6aJ6OcYRQowD7hIy34JVS9q3AqJoqinqUqS4Cg+iGzjTk55Tz572Xr1vC3f0o897L163hbv6UCwgT0JXPPey9et4W7+lHnvZevW8Ld/SgWMiV3prwWreWj21J1p69IZmBPoqwbAAPaRiY897L163hbv6Uee9l69bwt39KBP0FwqggAgDYchtyHulW6UAXNe3tEOdNVK1Yj+BaZ1Jn3lwBjuz3ToPTay9et4S7+lNFv0r4emrR1i6jltNpdjJPMn7reBbBMyt+e9l61bwl39KPPey9et4W7+lAskSt+e9l69bwt39KPPey9et4W7+lAskSt+e9l69bwt39KPPey9et4W7+lAskSt+e9l69bwt39KWPMDMREBERASD6W2FWvaVKFI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EGQKBn3MxPwlq6hfVH6COqXuH6DlAqPAL5jY1LkuiNVqVGWoaZbNMVClNmVN2JRRv754teN1GdAb2m2WUFRa1QSM7gE8vzlj4TwWhbJ1dBNC5zjLN37ZYk4GTgchJDqxAqHSegFveHvqbLXDgjUdOBQqHAXlz3+M6Ollsy1ba9RSxt3cVFUEsaNUBahUDmQQrfkDJPiPAKFd0qVA5amdSFatVQjYxlQrAA4Mkwm2Phvv+uecCE45Zi+s2p0ayhKq4LgasqeeMHnJWxoFKaISCVUDKjAOBjYdk206YUYUAZJOwxue2bYFfsOANSu69wtY6a7IzJpGdS09ABfnpwM475PaZ6iBgCMTMQIDpTwR7qmtNagpqHR2ypbVoYMF5jYkbybpg4GeeBy5fCbIgU/jJF5dUKFM6koVRWruu6AorBKerkWLMCQOQG/OW/E1U6KqMKAo7gABvN0DGJmIgIiICIiAiIgIiICIiAiIgJgzMQI3jfDEuaFSg49F1I94PYw94OCJGdBOFVra0FOu2qprcls51DOFOf8AKBLIRAEDMREBERAREQEREBERAREQEREBERAREQIPpXwQXdq9HOltmpv2pUXdGHx2PuJnnodY1KFlRpVf3iqS/I+mzM7bjmcsZOwBAzERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERA//Z"width="290" height="85" > </center><br/>

    """,height=110,
)

code="""
#Interpretación:
#Sumatoria desde el primer elemento (i) hasta el final (n) de 1 en 1
#de la multiplicación de (Xi - X(promedio))
#por (Yi - Y(promedio))

#Dividido por el producto de las raices de ((Xi - X(promedio))²) y ((Yi - Y(promedio))²)
"""
st.code(code, language='python')

code="""
import numpy as np
import math
sml = []

def correlation(x,y):
    mdx = x.mean()
    mdy = y.mean()
    numerador = np.sum((x-mdx)*(y-mdy))
    denominador = np.sqrt(np.sum((x-mdx)**2)*np.sum((y-mdy)**2))
    r = numerador/denominador
    return r

for i in range(len(email)):
    for j in range(len(email)):
        datta = data.loc[[i,j],:]
        nuevo = datta[datta.columns[1:]].to_numpy()
        sml.append(correlation(nuevo[0],nuevo[1]))

smld = np.array(sml).reshape(len(email),len(email))
matrix = pd.DataFrame(smld,email,email)
matrix
"""
st.code(code, language='python')

import numpy as np
import math
sml = []

@st.cache
def correlation(x,y):
    mdx = x.mean()
    mdy = y.mean()
    numerador = np.sum((x-mdx)*(y-mdy))
    denominador = np.sqrt(np.sum((x-mdx)**2)*np.sum((y-mdy)**2))
    r = numerador/denominador
    return r

for i in range(len(email)):
    for j in range(len(email)):
        datta = data.loc[[i,j],:]
        nuevo = datta[datta.columns[1:]].to_numpy()
        sml.append(correlation(nuevo[0],nuevo[1]))

smld = np.array(sml).reshape(len(email),len(email))
matrix = pd.DataFrame(smld,email,email)
# st.write(matrix)

st.write("## Gráfica de Calor") 

code="""
#Versión Simplificada
plt.matshow(matrix,vmin=-1, vmax=+1, cmap = 'YlOrRd')
plt.title('MAPA DE CALOR DE LA CORRELACIÓN', fontsize = 10)
plt.colorbar()
plt.show()"""
st.code(code, language='python')


#Versión Simplificada
#plt.matshow(matrix,vmin=-1, vmax=+1, cmap = 'YlOrRd'))
#plt.title('MAPA DE CALOR DE LA CORRELACIÓN', fontsize = 10))
#plt.colorbar())
#plt.show()
#<center><img src=""width="290" height="85" > </center><br/>
components.html(
    """
<center><img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4krD2rVOnY7zWIPvkTOwd81NagykaOxXWW0qIYwDmMg3NiwLSrjZWUypfwjoBTS1haJNLAuabV14Np6b2UyONXQBAm5xuyQx4hj9KtcF38-8Q1HNwBXa5jpVFOlhMQmAE0HQCHQSJHnyMH3eHNJOyiElp_h-IiAnXcgZW5bbzL8ciHnRtCaPNT8c2Mw/s1460/3.png" width="700" height="700"> </center>
    """,height=700,
)

#fig, ax = plt.subplots()
#sns.heatmap(matrix, vmin=-1, vmax=1, cmap = 'bwr')
#plt.title("MAPA DE CALOR DE LA CORRELACIÓN", fontsize = 10)
#st.pyplot(fig)

code="""
#Version Extendida
dfr = pd.DataFrame(matrix)
diccionario = {}
for i, correo in enumerate(email):
    diccionario.update({i:email})
dfr.rename(columns=diccionario, inplace=True)

plt.figure(figsize = (18,15))
sns.heatmap(dfr, xticklabels = dfr.columns, yticklabels = dfr.columns, vmin=-1, vmax=1, cmap = 'YlOrRd')
plt.title('MAPA DE CALOR DE LA CORRELACIÓN', fontsize = 20)
plt.show()"""
st.code(code, language='python')

#Version Extendida
dfr = pd.DataFrame(matrix)
diccionario = {}
for i, correo in enumerate(email):
    diccionario.update({i:email})
dfr.rename(columns=diccionario, inplace=True)

#plt.figure(figsize = (200,200))
# sns.heatmap(df, xticklabels = df.columns, yticklabels = df.columns, vmin=-1, vmax=1, cmap = 'bwr')
# plt.title("MAPA DE CALOR DE LA CORRELACIÓN", fontsize = 20)
# plt.show()

components.html(
    """
<center><img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiX0XpBzhYHmgI-HmYvXg9DKxZ0u4N52TkiOoxdU63PBnQIxfOuMZX3pDhgGebScCtFllLo_AYNoNm9e8eQLWgQYSDb3BsoAbeHzdhrQ9iAc7Md8Fm90rx-of4hAUwL9in5ZDFF5Leg4TrwFQbzWCtYFrmdkQdK9D39hNJlupTc0-KzYSaUC6ZacQA4qw/s1460/4.png" width="700" height="700"> </center>
    """,height=700,
)

#fig1, ax = plt.subplots()
#sns.heatmap(dfr, xticklabels = dfr.columns, yticklabels = dfr.columns, vmin=-1, vmax=1, cmap = 'bwr')
#plt.title("MAPA DE CALOR DE LA CORRELACIÓN", fontsize = 20)
#st.pyplot(fig1)

st.markdown(""" ## **Resultados**
**Algoritmo de Busqueda**""")

code="""#Algoritmo de busqueda de los mayores, se interpolan en pares
mayores = matrix.unstack()
print('Los mayores: \n')
print(mayores.sort_values(ascending=False)[range(len(values),((len(values)+4)))])
"""
st.code(code, language='python')

#Algoritmo de busqueda de los mayores, se interpolan en pares
mayores = matrix.unstack()
st.write('Los mayores: \n')
st.write(mayores.sort_values(ascending=False)[range(len(values),((len(values)+4)))])

st.write("""Los resultados de la similitud obtenidos en **Lugares Turísticos donde Viajar** según la tabla de Correlacion son lo siguientes encuestados:

1.-  raf1t0mendoza@gmail.com y betzy.romen@gmail.com obtienen el **PRIMER** índice más alto de mimilitud con un porcentaje de 78%

2.-  dvillagrac@unsa.edu.pe y floresgarnicaedwinmaycol@gmail.com obtienen el **SEGUNDO** índice más alto de mimilitud con un porcentaje de 72%

""")

components.html(
    """
    
<center><img src="https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png"></center><br/>

    """,height=20,
)






