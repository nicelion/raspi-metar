# import urllib.request
# import xml.etree.ElementTree as ET

# response = urllib.request.urlopen('https://aviationweather.gov/adds/dataserver_current/httpparam?datasource=metars&requestType=retrieve&format=xml&mostRecentForEachStation=constraint&hoursBeforeNow=1.25&stationString=kgmu')
# html = response.read()

# root = ET.fromstring(html)


# for child in root:
#     print(child.tag, child.attrib)

import avwx
from avwx import Metar

try:

    kgsp = Metar("KSPn")
except avwx.exceptions.BadStation:
    print("there was an error")
