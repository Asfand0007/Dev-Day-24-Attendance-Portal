import math
from pyproj import Geod


def WGS84_Distance_Calc(fastLat, fastLng, usrLat, usrLng):
    #print("coordinates: ", fastLat, fastLng, usrLat, usrLng)   #debugging purposes
    geod = Geod(ellps='WGS84')
    dist = geod.inv(fastLng, fastLat, usrLng, usrLat)[2]        
    #print("distance: ", dist)
    return abs(dist)

