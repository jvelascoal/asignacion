import streamlit as st
import pandas as pd
import numpy as np


st.title('Reorganización de congregaciones religiosas')
st.subheader('Autor: Jonás Velasco')

data = pd.DataFrame({
    'cities' : ['Aguascalientes'],
    'lat' : [21.881696],
    'lon' : [-102.2975663]
})


def fetch_data():
    df = pd.read_csv("Hogares.csv")
    return df

data1 = fetch_data()

if st.checkbox('Mostrar datos de las familias'):
    #st.subheader('Raw data')
    st.write(data1)

def fetch_data2():
    df = pd.read_csv("CentrosReunion.csv")
    return df

CentrosReunion = fetch_data2()

if st.checkbox('Mostrar datos de las centros de reunión'):
    #st.subheader('Raw data')
    st.write(CentrosReunion)


data2 = pd.DataFrame({
    'lat' : data1["lat"],
    'lon' : data1["lon"],
    'name'  : data1["id"],
    'gurobi' : data1["gurobi"],
    'localsolver' : data1["localsolver"],
    'cplex' : data1["cplex"]
})

reunion = pd.DataFrame({
    'lat' : CentrosReunion["lat"],
    'lon' : CentrosReunion["lon"],
    'name' : CentrosReunion["id"]
})

#st.subheader('Mapa de Aguascalientes')
#st.map(data2, zoom=12)


