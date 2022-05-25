import string,sys,os
from PIL import Image
from PIL.ExifTags import TAGS

import folium
import pandas
import csv

directory = "D:/Projects/han/Python/py/TESTIMAGES"
gpsInfoFile = "D:/Projects/han/Python/py/gpsInfo.txt"
saveMapFile = "D:/Projects/han/Python/py/00Map.html"


def writeGPSText(gpsInfo):

    with open(gpsInfoFile, 'a', encoding='utf-8', newline='') as f:
        f.write(gpsInfo+"\n")


def getGPSInfo(directory):
    for root, dir, files in os.walk(directory):
        for fp in files:
            if ".JPG" in fp.upper():
                # open a file and extract exif
                fn = root+'/'+fp
                print(fn)

                try:
                    i = Image.open(fn)
                    info = i._getexif()
                    exif={}

                    for tag, value in info.items():
                        decoded = TAGS.get(tag, tag)
                        #print(tag, value)
                        exif[decoded]=value
                    # from the exif data, extract gps
                    exifGPS = exif['GPSInfo']
                    latData = exifGPS[2]
                    lonData = exifGPS[4]
                    #print(exifGPS)

                    # calculate the lat / long
                    latDeg = latData[0][0] / float(latData[0][1])
                    latMin = latData[1][0] / float(latData[1][1])
                    latSec = latData[2][0] / float(latData[2][1])
                    lonDeg = lonData[0][0] / float(lonData[0][1])
                    lonMin = lonData[1][0] / float(lonData[1][1])
                    lonSec = lonData[2][0] / float(lonData[2][1])

                    # correct the lat/lon based on N/E/W/S
                    Lat = (latDeg + (latMin + latSec/60.0)/60.0)

                    if exifGPS[1] == 'S': Lat = Lat * -1
                    Lon = (lonDeg + (lonMin + lonSec/60.0)/60.0)

                    if exifGPS[3] == 'W': Lon = Lon * -1

                    # print file
                    msg1 = fn+" located at "+str(Lat)+","+str(Lon)
                    msg = fp+","+ str(Lat) +","+ str(Lon)
                    #print(msg)
                    writeGPSText(msg)
                except:
                    pass


def markerMap():

    data = pandas.read_csv(gpsInfoFile)

    name = list(data["name"])
    print(name)
    lat = list(data["lat"])
    print(lat)
    lon = list(data["lon"])
    print(lon)

    def color_producer():
          return 'red'

    map = folium.Map(location=[38.58,-99.09], zoom_start=3)

    for nm,lt,ln in zip(name,lat,lon):
        print(nm, lt, ln)
        folium.Marker(location=[lt,ln],popup=nm,
         icon=folium.Icon(color=color_producer())).add_to(map)

    map.save(saveMapFile)


def main():
    os.chdir(directory)

    if os.path.isfile(directory+"/"+gpsInfoFile):
        fp = os.remove(directory+"/"+gpsInfoFile)

    writeGPSText("name,lat,lon")

    getGPSInfo(directory)



if __name__ == '__main__':
    main()
    markerMap()

    print("Success !!!!!")