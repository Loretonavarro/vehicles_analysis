import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('data/vehicles_us.csv') # leer los datos
build_histogram = st.checkbox('Construir un histograma')
build_disp = st.checkbox('Construir gráfico de dispersión') # crear botón de dispersión

if build_histogram: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
    
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if build_disp: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de una gráfica de dispersión para el conjunto de datos de venta de coches')
    
    # crear una gráfica de dispersión
    fig = px.scatter(car_data, x="odometer", y="price")
    
    st.plotly_chart(fig, use_container_width=True)