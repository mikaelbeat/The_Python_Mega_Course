import folium, pandas
from datetime import datetime

date_now = datetime.now()
date_now = date_now.strftime("%H:%M:%S")

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])


def colorizer(elevation):
    if elevation < 1000:
        return "green"
    elif elevation > 1000 and elevation < 3000:
        return "orange"
    else:
        return "red"
    

map_html = folium.Map(location=[38.2, -99.1], zoom_start=3)

fgv = folium.FeatureGroup(name="Volcanoes")


for lt, ln ,el in zip(lat, lon, elev):
    fgv.add_child(folium.Marker(location=[lt, ln], popup=f"{el}m", icon=folium.Icon(color=colorizer(el))))
    
fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(), 
                            style_function=lambda x: {"fillColor":"green" if x["properties"]["POP2005"] < 10000000 
                            else "orange" if 10000000 <= x["properties"]["POP2005"] < 20000000
                            else "red"}))

map_html.add_child(fgv)
map_html.add_child(fgp)
map_html.add_child(folium.LayerControl())

map_html.save("Map1.html")
print(f"Map created, {date_now}")
