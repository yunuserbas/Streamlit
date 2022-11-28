import streamlit as st
import requests 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.title('Hello Wilders, welcome to my application!')
st.write('coucou coucou')

df = pd.read_csv("velib.csv")

# Quasiment tous les éléments streamlit peuvent être affichés dans la "sidebar"
st.sidebar.title("coucou")
st.sidebar.write("hello")

option_velo = st.sidebar.selectbox(
	    'Quel type de vélo ?',
	    ('mechanical', 'ebike'))

# On peut créer plusieurs "colonnes" pour afficher des éléments côte à côte
# La liste qui suit contient 2 éléments, il y aura donc 2 colonnes
# La première colonne a un poids de "2", elle sera donc 2 fois plus large
col1, col2 = st.columns([2, 1])

# Les éléments à afficher dans chaque colonne :
with col1:
	fig, ax = plt.subplots()
	ax = sns.boxplot(df[option_velo])
	st.pyplot(fig)

with col2:
	fig, ax = plt.subplots()
	ax = sns.boxplot(df[option_velo])
	st.pyplot(fig)

# Ici, nous repartons en centré pleine page, sans les colonnes
link_station = "https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_information.json"
r_stations = requests.get(link_station)
df_stations = pd.json_normalize(r_stations.json()['data']['stations'])
df_merge = pd.merge(left = df,
         right = df_stations,
         on = "station_id")

fig_heatmap = px.density_mapbox(df_merge, 
                        lat='lat', 
                        lon='lon', 
                        z=option_velo, 
                        radius=20,
                        center=dict(lat=48.865983, lon=2.275725	), 
                        zoom=10,
                        mapbox_style="stamen-terrain")
st.plotly_chart(fig_heatmap)


