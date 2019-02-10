import folium
import sys

copyright_osm = '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'

_map = folium.Map(location=[35.681167, 139.767052], attr=copyright_osm)

# データ
# https://github.com/dataofjapan/land/blob/master/japan.geojson
data_path = sys.argv[1]

# GeoJson読み込み
folium.GeoJson(data_path, name='geojson').add_to(_map)
folium.LayerControl().add_to(_map)

_map.save('sample.html')
