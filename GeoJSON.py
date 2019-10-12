import urllib.request, urllib.parse, urllib.error
import json
import ssl
import string
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import IFrame

#data location
serviceurl = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_week.geojson'

#request and open access to data, then read
uh = urllib.request.urlopen(serviceurl)
data = uh.read()

#refator data to json
try:
    js = json.loads(data)
except:
    js = None
#print(json.dumps(js, indent=4))

#parse needed data
count = js['metadata']['count'] #extract 'quake number
if count < 1:
    print("there have been no Significant Earthquakes reported within the last 7 days")
else:
    print("\n",count," Significant Earthquakes in the last 7 days:\n")
    earthquakes = [] #list of 'quakes
    maxmag = 0
    maxlat = 0
    maxlong = 0
    mags = [] #list of magnitudes
    locs = [] #list of locations
    
    #get coordinates for each 'quake
    i = 0
    while i < count:
        location = js['features'][i]['properties']['place']
        latlong = js['features'][i]['geometry']['coordinates']
        mag = js['features'][i]['properties']['mag']
        locs.append(location)
        mags.append(mag)
        
        #cast coordinates to strings
        long = latlong[0]
        long = str(long)
        long = long.strip()
        lat = latlong[1]
        lat = str(lat)
        lat = lat.strip()
        
        #find greatest magnitude
        if mag > maxmag:
            maxmag = mag
            maxlat = lat
            maxlong = long
            
        #output results for every earthquake found
        print(location)
        print("lat: ",lat,", long: ",long, ", magnitude: ",mag,"\n")
        i+=1
if count > 0:
    print("Greatest magnitude: ",maxmag)

y_pos = np.arange(len(locs)) #sort and get amount of bars
plt.barh(y_pos, mags, align='center', alpha=0.5) #set scalar, max, align and step
plt.yticks(y_pos, locs) #set y axis by location

plt.xlabel('Magnitude')
plt.title('Magnitude of each significant earthquake in the last 7 days\n')
plt.show()

print("lat: ",maxlat,", long: ",maxlong, ", magnitude: ",maxmag,"\n")
api = "ENTER KEY HERE" #key for embeded usage
url = "https://www.google.com/maps/embed/v1/place?key="+api+"&q="+maxlat+","+maxlong+"&zoom=12&maptype=satellite"
IFrame(url, width=600, height=450) #viewport window