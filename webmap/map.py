import folium
import pandas as pd
data = pd.read_csv('Volcanoes.csv')
cordinates_list = zip(list(data["LAT"]),list(data["LON"]))
volc_name = list(data["NAME"])

map = folium.Map(location = [34.7999992,-108.0009995 ], zoom_start=6, titles="Mapbox Bright")
fg = folium.FeatureGroup(name='My Map')

for cordinates,name in zip(cordinates_list,volc_name):
    print(cordinates)
    print(name)
    fg.add_child(folium.CircleMarker(location=list(cordinates),radius=6,fill_color='red', fill_capacity=1, popup=(str(name)), icon=folium.Icon(color='green')))
map.add_child(fg)
map.save('map.html')
