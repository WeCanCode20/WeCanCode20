import bs4
from bs4 import BeautifulSoup
import requests
import time

filename = '/home/pi/Documents/rain.log'

def getPoint():
    url='https://www.weather.gov/dvn/obsmapprecip'
    rainfall = 99.99 # this should come back if there is no datapoint
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    table = soup.find_all('table')
    data =str(table) # toss to a string, only need one line
    data2 = data.splitlines() # split it into lines
# now need to get only the point for Waterloo
    for line in data2:
        if 'Waterloo' in line:
            rain = line[30:len(line)] # just grab a chunk of the end
            rain2=rain.strip()        # then toss out the trash
            rainfall = float(rain2)  # make it a float
    return rainfall

# The function to write the data point to a file
# together with the epoch time (or maybe unix time...)
def writeData(point):
    f = open(filename, 'a')
    f.write(str(time.ctime()) + ',' + str(round(time.time())) + ',' + str(point) + '\n')


point = getPoint()
writeData(point)

