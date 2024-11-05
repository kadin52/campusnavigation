import googlemaps
import requests, json
api_key = 'AIzaSyCv56KyCK5WYIANBKS0ARzw_110e7H7fTc'
def get_coordinates(address):
    gmaps = googlemaps.Client(key=api_key)
    coords = gmaps.geocode(address)
    if coords:
        location = coords[0]['geometry']['location']
        lat = location['lat']
        lng = location['lng']
        return lat, lng
    else:
        print("Error")
        return 0,0

def calc_travel(coordinates, mode = 'walking'):
    gmaps = googlemaps.Client(key=api_key)
    #url = 'https://maps.googleapis.com/maps/api/distancematrix/json'
    # response = requests.get(url + 'origins = ' +source
    #                         +'&destination = ' +destination
    #                         +'&mode = ' + mode
    #                         +'&key = ' +api_key)
    travel_info = {}

    for i, source in enumerate(coordinates):
        for j, destination in enumerate(coordinates):
            #if i<j:
                response = gmaps.distance_matrix(origins=[source], destinations=[destination], mode=mode)
                if response['status'] == 'OK':
                    travel_time = response['rows'][0]['elements'][0]['duration']['value']
                    distance = response['rows'][0]['elements'][0]['distance']['value']
                    travel_info[(i,j)] = (travel_time,distance)
                    travel_info[(j, i)] = (travel_time,distance)
                else:
                    return -999
    return travel_info