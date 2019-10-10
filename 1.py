import folium

fg=folium.FeatureGroup("my map")
fg.add_child(folium.GeoJson(data=(open('india_states.json','r',encoding='utf-8-sig').read())))

fg.add_child(folium.Marker(location=[27.1751, 78.0421],popup="this is were taj mahal is located  "))

map=folium.Map(location=[21.1458,79.0882],zoom_start=5)

map.add_child(fg)
map.save("test.html")