import folium

def create_map(traffic_data):

    m = folium.Map(location=[17.3850,78.4867], zoom_start=13)

    locations = {
        "A":[17.3850,78.4867],
        "B":[17.3900,78.4900],
        "C":[17.3950,78.4800],
        "D":[17.3800,78.4750]
    }

    for key,value in traffic_data.items():

        folium.Marker(
            location=locations[key],
            popup=f"Vehicles: {value}",
            icon=folium.Icon(color="red")
        ).add_to(m)

    return m
