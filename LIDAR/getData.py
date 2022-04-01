from multiprocessing.connection import wait
import sys
import numpy as np
from rplidar import RPLidar,RPLidarException
import matplotlib.pyplot as plt
from math import cos,sin,pi
import time
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

def analyse(lidar):
    for i, scan in enumerate(lidar.iter_scans('express')):
        print('%d: Got %d measures' % (i, len(scan)))
        data.append([[scan[j][1] for j in range(len(scan))],[scan[j][2] for j in range(len(scan))]])
        Angle = data[i][0]
        Distance = data[i][1]
        X = [Distance[i]*cos(Angle[i]*pi/180) for i in range(len(scan))]
        Y = [Distance[i]*sin(Angle[i]*pi/180) for i in range(len(scan))]
        # plt.figure()
        # plt.scatter(X,Y)
        # #plt.show()
        # plt.ion()
        # plt.draw()
        # plt.pause(1)
        # X,Y,Angle,Distance = [],[],[],[]
        #plt.close()

        if i == 50:
           break

#run('./examples/data')
lidar = RPLidar(PORT_NAME)
data = []
try:
    analyse(lidar)
   
# with open('datalidar.txt','w') as f:
#         f.writelines(["%s\n" % item  for item in data])
#         f.close()
except ValueError:
    print('Issue : Value Error')
    analyse(lidar)
except RPLidarException:
    print('Issue : RPlidar Error')
    analyse(lidar)

