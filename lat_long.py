from math import sin, cos, sqrt, atan2, radians
import math as mth

# approximate radius of earth in km
R = 6373.0

lat1 = 37.8403
lat2 = 37.8402
lon1 = -122.2934
lon2 = -122.2934

def distance (latitud1, longitud1, latitud2, longitud2):

    lat1 = latitud1
    lon1 = longitud1
    lat2 = latitud2
    lon2 = longitud2
    a = mth.cos(mth.radians(90-lat1))
    b = mth.cos(mth.radians(90-lat2))
    c = mth.sin(mth.radians(90-lat1))
    d = mth.sin(mth.radians(90-lat2))
    e = mth.cos(mth.radians(lon1-lon2))

    distance = R * mth.acos( a * b + c * d * e )
    return distance
