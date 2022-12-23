#!/usr/bin/env python
# coding: utf-8
import numpy as np
import pandas as pd
import streamlit as st
#import matplotlib.pyplot as plt
#import matplotlib
#import seaborn as sns
#from scipy.spatial.distance import euclidean
import time
import streamlit.components.v1 as components

components.html(
    """
    
<center><img src="https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png"></center><br/>

    """,height=20,
)

st.write("# PROCESAMIENTO") 

components.html(
    """
    
<center><img src="https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png"></center><br/>

    """,height=20,
)


code="""
# Importamos el archivo .csv
data = pd.read_csv('Lugares_T.csv')"""
st.code(code, language='python')

# Archivo CSV separado por comas
data = pd.read_csv('Lugares_T.csv')
# El archivo debe estar anexado
# Mostrar todo
st.write(data)

code="""data.shape
#Tamaño de la matriz
#(51 Usuarios,53 Preguntas +1)"""
st.code(code, language='python')

st.write(data.shape)
#Tamaño de la matriz
#(51 Usuarios,53 Preguntas +1)

code="""data.dtypes
# Información de las columnas"""
st.code(code, language='python')
st.write(data.dtypes)

st.markdown("""
# **Imputación de datos**

## Visualización de valores nulos (NaN)
""")

code="""data.isnull().sum()
#devuelve el número de valores faltantes en el conjunto de datos."""
st.code(code, language='python')

st.write(data.isnull().sum())


st.markdown("""# Por Columna """)

code="""for i in data.columns[1:]:
    data[i].fillna(data[i].mean(), inplace=True)

data.isnull().sum()
#Devuelve el NUEVO número de valores faltantes en el conjunto de datos.

#Deberia de estar en "0" todos, lo que significaría que esta CORRECTO.
"""
st.code(code, language='python')

for i in data.columns[1:]:
    data[i].fillna(data[i].mean(), inplace=True)

st.write(data.isnull().sum())

# Comprobamos


st.markdown(""" ## **2.- Correlación de Pearson (Similitud)**

A continuación se procede con la extracción de datos, en columnas:
""")


#Se parte de Data
File = data[data.columns[1:]].to_numpy()
correos = data[data.columns[0]].to_numpy()

code="""
file = data[data.columns[1:]].to_numpy()
correos = data[data.columns[0]].to_numpy()
#Filas desde [1:] en adelante
print(file)
#Columna de Correos [0] 
print(correos)
#Extracción de datos, en columnas"""
st.code(code, language='python')
st.write(File)
st.write(correos)
st.markdown("""
## **3.- Correlación en Pandas**
""")
# In[ ]:
code="""file.T"""
st.code(code, language='python')

st.write(File.T)


st.markdown(""" ## **4.- Matriz de Correlación**

**Transpuesta**""")


code="""df = pd.DataFrame(file.T,columns = correos)
df"""
st.code(code, language='python')
df = pd.DataFrame(File.T,columns = correos)
# st.write(df)

code1="""m_corr_pandas = df.corr()
m_corr_pandas"""
st.code(code1, language='python')

m_corr_pandas = df.corr()
# st.write(m_corr_pandas)


code2="""m_corr_d_pandas = np.round(m_corr_pandas, decimals = 4)
m_corr_d_pandas"""
st.code(code2, language='python')
m_corr_d_pandas = np.round(m_corr_pandas, decimals = 4)
# st.write(m_corr_d_pandas)


st.markdown("""## Gráfica de Calor""")

code="""
#Versión Simplificada
plt.matshow(m_corr_d_pandas,vmin=-1, vmax=+1, cmap = 'YlOrRd')
plt.title('MAPA DE CALOR DE LA CORRELACIÓN', fontsize = 10)
plt.colorbar()
plt.show()"""
st.code(code, language='python')


#Versión Simplificada
#plt.matshow(m_corr_d_pandas,vmin=-1, vmax=+1, cmap = 'YlOrRd'))
#plt.title('MAPA DE CALOR DE LA CORRELACIÓN', fontsize = 10))
#plt.colorbar())
#plt.show()
#st.markdown("""
#![1](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEglowCz3JVIsPlVcVXo4H3Vle292h8M9nA3LYpzAoqKNkZyEZIOHjUIV13M61gto1DsdxnWaweljEMzGoQXz5TGXHpp_9Q8TINLQRtb9jq-irVmy4CmzMm5GtrMZmXXmKwDWX2boxRzBe5GYguX_SN_8bEncQAb0m7sZaySai42wl1GoqNQoasvsileWw/s1460/1.png)
#""")

components.html(
    """
<center><img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEglowCz3JVIsPlVcVXo4H3Vle292h8M9nA3LYpzAoqKNkZyEZIOHjUIV13M61gto1DsdxnWaweljEMzGoQXz5TGXHpp_9Q8TINLQRtb9jq-irVmy4CmzMm5GtrMZmXXmKwDWX2boxRzBe5GYguX_SN_8bEncQAb0m7sZaySai42wl1GoqNQoasvsileWw/s1460/1.png" width="500" height="600"> </center>
    """,height="600",
)



#fig, ax = plt.subplots()
#sns.heatmap(m_corr_d_pandas, vmin=-1, vmax=1, cmap = 'YlOrRd')
#plt.title("MAPA DE CALOR DE LA CORRELACIÓN", fontsize = 10)
#st.pyplot(fig)



code="""
#Version Extendida
df = pd.DataFrame(m_corr_d_pandas)
diccionario = {}
for i, correo in enumerate(correos):
    diccionario.update({i:correo})
df.rename(columns=diccionario, inplace=True)

plt.figure(figsize = (18,15))
sns.heatmap(df, xticklabels = df.columns, yticklabels = df.columns, vmin=-1, vmax=1, cmap = 'YlOrRd')
plt.title('MAPA DE CALOR DE LA CORRELACIÓN', fontsize = 20)
plt.show()"""
st.code(code, language='python')

#Version Extendida
df = pd.DataFrame(m_corr_d_pandas)
diccionario = {}
for i, correo in enumerate(correos):
    diccionario.update({i:correo})
df.rename(columns=diccionario, inplace=True)

#plt.figure(figsize = (200,200))
# sns.heatmap(df, xticklabels = df.columns, yticklabels = df.columns, vmin=-1, vmax=1, cmap = 'YlOrRd')
# plt.title("MAPA DE CALOR DE LA CORRELACIÓN", fontsize = 20)
# plt.show()
components.html(
    """
    
<center><img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhpZ9zKXKC9vAkIXbTA3CxxeyRnmVBuZasVLzdVs7AEgT79DF_D5xKHA4o9aQgqciyHXEpsNCA4nKmGgu1k1jJ_bv-vNIto_1jb7HbGZs0R3vu97drrGyjIZRAwmRVq1AIwlexdgyB3IsSWmPV0JZRuhDkINbhLUcCRlwGD4dKR3dzPOh0bfqEhWVQC9w/s320/2.png"></center><br/>

    """,
)
#fig1, ax = plt.subplots()
#sns.heatmap(df, xticklabels = df.columns, yticklabels = df.columns, vmin=-1, vmax=1, cmap = 'YlOrRd')
#plt.title("MAPA DE CALOR DE LA CORRELACIÓN", fontsize = 20)
#st.pyplot(fig1)

st.markdown(""" ## **5.- Resultados**
**Algoritmo de Busqueda**""")

code="""#Algoritmo de busqueda de los mayores, se interpolan en pares
may = m_corr_d_pandas.unstack()
print('Los mayores: \n')
print(may.sort_values(ascending=False)[range(len(file),((len(file)+4)))])
"""
st.code(code, language='python')

#Algoritmo de busqueda de los mayores, se interpolan en pares
may = m_corr_d_pandas.unstack()
st.write('Los mayores: \n')
st.write(may.sort_values(ascending=False)[range(len(File),((len(File)+4)))])

st.write("""Los resultados de la similitud obtenidos en **Lugares Turísticos donde Viajar** según la tabla de Correlacion son lo siguientes encuestados:

1.-  raf1t0mendoza@gmail.com y betzy.romen@gmail.com obtienen el **PRIMER** índice más alto de mimilitud con un porcentaje de 78%

2.-  dvillagrac@unsa.edu.pe y floresgarnicaedwinmaycol@gmail.com obtienen el **SEGUNDO** índice más alto de mimilitud con un porcentaje de 72%

""")

components.html(
    """
    
<center><img src="https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png"></center><br/>

    """,height=20,
)








