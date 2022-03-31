#!/usr/bin/env python3
'''Records scans to a given file in the form of numpy array.
Usage example:

$ ./record_scans.py out.npy'''
import sys
import numpy as np
from rplidar import RPLidar,RPLidarException

PORT_NAME = '/dev/ttyUSB0'

def run(path):
    lidar = RPLidar(PORT_NAME)
    data = []
    try:
        print('Recording measurments... Press Crl+C to stop.')
        for scan in lidar.iter_scans():
            print(scan)
            #data.append(np.array(scan))
    except KeyboardInterrupt:
        print('Stoping.')
    lidar.stop()
    lidar.disconnect()
    np.save(path, np.array(data))
    
def AccessData(Data,NumMes):
    '''
    Permet de récupérer les données pour l'angle & la distance d'une certaine mesure
    Présentation : [[Angle],[Distance]]
    '''
    Angles = [Data[NumMes][i][1] for i in range(len(Data[0]))]   # Liste des Angles
    Distances = [Data[NumMes][i][2] for i in range(len(Data[0]))]    # Liste des distances
    return [Angles,Distances]

#run('./examples/data')
lidar = RPLidar(PORT_NAME)
data = []
try:
    for i, scan in enumerate(lidar.iter_scans()):
        print('%d: Got %d measures' % (i, len(scan)))
        data.append(scan)
        if i > 0:
            break
    #print(data)
    print(AccessData(data,0))

except ValueError:
    print('Issue : Value Error')
except RPLidarException:
    print('Issue : RPlidar Error')


