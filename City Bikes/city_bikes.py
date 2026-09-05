def get_station_data(filename: str):
    dictionary = {}
    with open(filename) as new_file :
        for line in new_file :
            line = line.replace("\n" , "")
            separated = line.split(";")
            if separated[0] == "Longitude" :
                continue
            else :
                dictionary[separated[3]] = (float(separated[0]) , float(separated[1]))      
    return dictionary
def distance(stations: dict, station1: str, station2: str):
    import math
    long1 = stations[station1] 
    long2 = stations[station2] 
    x_km = ((long1[0]) - (long2[0])) * 55.26
    y_km = ((long1[1]) - (long2[1])) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km
def greatest_distance(stations: dict):
    listo = []
    indexo = 0
    powp1 = None
    powp2 = None
    for key , value in stations.items():
        listo.append(key)
    for places in listo :
        for items in listo :
            meow = distance(stations , places , items)
            if meow > indexo : 
                indexo = meow
                powp1 = places
                powp2 = items 
    return powp1 , powp2 , indexo


        