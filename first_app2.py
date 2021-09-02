import streamlit as st
import pandas as pd
import numpy as np
from streamlit_folium import folium_static
import folium

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

opcion = st.selectbox('Soluciones', ['Nada', 'Gurobi','Localsolver','Cplex'])

st.write('Usted seleccionó: ', opcion)

if opcion == 'Gurobi':
	m = folium.Map(location=[21.881696, -102.2975663], zoom_start=13)
#	folium_static(m)
	for i in range(4):
		if i == 0:
			folium.Marker(location=[reunion['lat'][i], reunion['lon'][i]], popup=reunion['name'][i],icon=folium.Icon(color='red', icon='home', prefix='fa')).add_to(m)
		if i == 1:
			folium.Marker(location=[reunion['lat'][i], reunion['lon'][i]], popup=reunion['name'][i],icon=folium.Icon(color='green', icon='home', prefix='fa')).add_to(m)
		if i == 2:
			folium.Marker(location=[reunion['lat'][i], reunion['lon'][i]], popup=reunion['name'][i],icon=folium.Icon(color='pink', icon='home', prefix='fa')).add_to(m)
		if i == 3:
			folium.Marker(location=[reunion['lat'][i], reunion['lon'][i]], popup=reunion['name'][i],icon=folium.Icon(color='blue', icon='home', prefix='fa')).add_to(m)

	for i in range(50):
		if data2['gurobi'][i] == 0:
			folium.Marker(location=[data2['lat'][i], data2['lon'][i]], popup=data2['name'][i],icon=folium.Icon(color='red', icon='users', prefix='fa')).add_to(m)

		if data2['gurobi'][i] == 1:
			folium.Marker(location=[data2['lat'][i], data2['lon'][i]], popup=data2['name'][i],icon=folium.Icon(color='green', icon='users', prefix='fa')).add_to(m)

		if data2['gurobi'][i] == 2:
			folium.Marker(location=[data2['lat'][i], data2['lon'][i]], popup=data2['name'][i],icon=folium.Icon(color='pink', icon='users', prefix='fa')).add_to(m)

		if data2['gurobi'][i] == 3:
			folium.Marker(location=[data2['lat'][i], data2['lon'][i]], popup=data2['name'][i],icon=folium.Icon(color='blue', icon='users', prefix='fa')).add_to(m)

	folium_static(m)
	st.write('Obj1 (distancia Hogar a Centro:): 189.152')
	st.write('Obj2 (distancia Hogar a Hogar): 807.702')
	st.write('Personas: 46.0, 45.0, 43.0, 42.0')
	st.write('SMAPIS: 11.0, 12.0, 12.0, 12.0')


if opcion == 'Localsolver':
	m = folium.Map(location=[21.881696, -102.2975663], zoom_start=13)
#	folium_static(m)
	for i in range(4):
		if i == 0:
			folium.Marker(location=[reunion['lat'][i], reunion['lon'][i]], popup=reunion['name'][i],icon=folium.Icon(color='red', icon='home', prefix='fa')).add_to(m)
		if i == 1:
			folium.Marker(location=[reunion['lat'][i], reunion['lon'][i]], popup=reunion['name'][i],icon=folium.Icon(color='green', icon='home', prefix='fa')).add_to(m)
		if i == 2:
			folium.Marker(location=[reunion['lat'][i], reunion['lon'][i]], popup=reunion['name'][i],icon=folium.Icon(color='pink', icon='home', prefix='fa')).add_to(m)
		if i == 3:
			folium.Marker(location=[reunion['lat'][i], reunion['lon'][i]], popup=reunion['name'][i],icon=folium.Icon(color='blue', icon='home', prefix='fa')).add_to(m)

	for i in range(50):
		if data2['localsolver'][i] == 0:
			folium.Marker(location=[data2['lat'][i], data2['lon'][i]], popup=data2['name'][i],icon=folium.Icon(color='red', icon='users', prefix='fa')).add_to(m)

		if data2['localsolver'][i] == 1:
			folium.Marker(location=[data2['lat'][i], data2['lon'][i]], popup=data2['name'][i],icon=folium.Icon(color='green', icon='users', prefix='fa')).add_to(m)

		if data2['localsolver'][i] == 2:
			folium.Marker(location=[data2['lat'][i], data2['lon'][i]], popup=data2['name'][i],icon=folium.Icon(color='pink', icon='users', prefix='fa')).add_to(m)

		if data2['localsolver'][i] == 3:
			folium.Marker(location=[data2['lat'][i], data2['lon'][i]], popup=data2['name'][i],icon=folium.Icon(color='blue', icon='users', prefix='fa')).add_to(m)

	folium_static(m)
	st.write('Obj1 (distancia Hogar a Centro:): 189.153')
	st.write('Obj2 (distancia Hogar a Hogar): 798.372')
	st.write('Personas: 46.0, 46.0, 42.0, 42.0')
	st.write('SMAPIS: 11.0, 12.0, 12.0, 12.0')


if opcion == 'Cplex':
	m = folium.Map(location=[21.881696, -102.2975663], zoom_start=13)
#	folium_static(m)
	for i in range(4):
		if i == 0:
			folium.Marker(location=[reunion['lat'][i], reunion['lon'][i]], popup=reunion['name'][i],icon=folium.Icon(color='red', icon='home', prefix='fa')).add_to(m)
		if i == 1:
			folium.Marker(location=[reunion['lat'][i], reunion['lon'][i]], popup=reunion['name'][i],icon=folium.Icon(color='green', icon='home', prefix='fa')).add_to(m)
		if i == 2:
			folium.Marker(location=[reunion['lat'][i], reunion['lon'][i]], popup=reunion['name'][i],icon=folium.Icon(color='pink', icon='home', prefix='fa')).add_to(m)
		if i == 3:
			folium.Marker(location=[reunion['lat'][i], reunion['lon'][i]], popup=reunion['name'][i],icon=folium.Icon(color='blue', icon='home', prefix='fa')).add_to(m)

	for i in range(50):
		if data2['cplex'][i] == 0:
			folium.Marker(location=[data2['lat'][i], data2['lon'][i]], popup=data2['name'][i],icon=folium.Icon(color='red', icon='users', prefix='fa')).add_to(m)

		if data2['cplex'][i] == 1:
			folium.Marker(location=[data2['lat'][i], data2['lon'][i]], popup=data2['name'][i],icon=folium.Icon(color='green', icon='users', prefix='fa')).add_to(m)

		if data2['cplex'][i] == 2:
			folium.Marker(location=[data2['lat'][i], data2['lon'][i]], popup=data2['name'][i],icon=folium.Icon(color='pink', icon='users', prefix='fa')).add_to(m)

		if data2['cplex'][i] == 3:
			folium.Marker(location=[data2['lat'][i], data2['lon'][i]], popup=data2['name'][i],icon=folium.Icon(color='blue', icon='users', prefix='fa')).add_to(m)

	folium_static(m)
	st.write('Obj1 (distancia Hogar a Centro:): 187.405')
	st.write('Obj2 (distancia Hogar a Hogar): 861.075')
	st.write('Personas: 46.0, 45.0, 42.0, 43.0')
	st.write('SMAPIS: 11.0, 12.0, 12.0, 12.0')


