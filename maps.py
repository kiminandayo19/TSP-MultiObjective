import json
import folium

# Here's the process we need to do in this program
# 1. Open and read the json latlong file
# 2. Open the json shortest path from tsp-mput
# 3. Create the map opject
# 4. Choose one point as the starting point and zoom
# 5. Add each point of the path to the map object

# Required python library to install : folium (to draw the map)
# How to install : pip install folium
# Do the installation first then you can run this python file

# Here's some global variable we need to use
URL_KOTA = 'data_kota.json'     # This is for the data_kota.json
URL_TSP = 'tsp.json'            # This is for the tsp result .json
URL_PETA = 'peta.html'          # This is to save the map result -> The map result is in html file

# Note that : If you use google colab, first thing to do is upload all the json file needed
# Then change the data_kota.json to /content/data_kota.json; tsp.json to /content/tsp.json

def map_coordinate(data_kota, data_tsp):
    """This func will maps the region with its LatLong and return the cap names and each cap LatLong"""
    caps = []
    coord = {}
    file = open(data_kota)      # For the city that contain lat long
    file2 = open(data_tsp)      # For the city from the TSP result
    data = json.load(file)      # Same as file
    data2 = json.load(file2)    # Same as file2

    # This is the process to take the lat long for each city
    # Surely the order is the same as the order of the route that need to travel
    for cap in data2["Urutan Kota"].keys():     # Here we iterate through the city in the order city from tsp
        for city in data:                       # Here we iterate through the all the latlong data.json we have
            if cap == city:             # This is to map the corresponding city
                caps.append(cap)
                coord[cap] = (float(data[cap]['lat']), float(data[cap]['long']))    # Here we take the lat long of  each city

    # This two line is making sure that from the last city the traveller need to go back to the first city
    caps.append(caps[0])
    coord[caps[0]+"1"] = (float(data[caps[0]]['lat']), float(data[caps[0]]['long']))
    
    file.close()
    file2.close()
    
    return caps, coord

def draw_maps(maps, coord):
    """This function is for drawing the maps with each lat long we have from map_coordinate
       function. This function is not returning anything but create the map result"""
    peta = folium.Map(location = [-7.8, 110.3], zoom_start = 11)    # This is to initialize the map first position
    point = []      # This is the list to save each point location we need to connect
    for place in maps:
        point.append(list(coord[place]))

    # Here we create marker for each capital
    tooltip = "Click me!"
    for idx in range(len(maps) - 1):
        folium.Marker(
            point[idx],
            popup = f"{maps[idx]}",
            tooltip = f"{maps[idx]}"
        ).add_to(peta)
    
    folium.PolyLine(point, color = "blue", weight = 3, opacity = 1).add_to(peta)    # This will add each point location and draw the line to connect each point location

    # Save the map
    peta.save(URL_PETA)


def main():
    """This is the main function to do all the function"""
    maps, coord = map_coordinate(URL_KOTA, URL_TSP)     # 1. We need to run the map_coordinate func to generate the mapping and the lat long for each city
    draw_maps(maps, coord)                              # 2. Here we run the draw_map function. Obviously to draw all the point in the maps

if __name__ == "__main__":
    main()