import sys
import numpy as np
from rplidar import RPLidar,RPLidarException
import matplotlib.pyplot as plt
from math import cos,sin,pi
import time

######################
# Commandes à tapper #
######################
# ls /dev | grep ttyUSB
# sudo chmod 666 /dev/ttyUSB0

PORT_NAME = '/dev/ttyUSB0'

def run(path):
    '''Fonction Test --> Pour voir comment marche l'acquisition de la data'''
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

def GetData(lidar):
    '''Permet d'avoir les coordonnées cartésiennes (X,Y) de la data du LIDAR'''
    # Récupération de la data
    scan = RPLidar.iter_scans(lidar,'express',5000,5)
    
    print('Got %d measures', len(scan))

    # Conditionnement de la data    
    Angle = [scan[j][1] for j in range(len(scan))]
    Distance = [scan[j][2] for j in range(len(scan))]
    
    # Convertion en coordonnées cartésiennes
    X = [Distance[i]*cos(Angle[i]*pi/180) for i in range(len(scan))]
    Y = [Distance[i]*sin(Angle[i]*pi/180) for i in range(len(scan))]

    return X,Y

def test(lidar):
    scan = RPLidar.iter_scans(lidar,'express',5000,5)
    print(scan)

def affiche(X,Y):
    '''Permet l'affichage de la data'''
    plt.figure()
    plt.scatter(X,Y)
    plt.ion()
    plt.draw()
    plt.pause(1)
    plt.close()


def analyse1(lidar):
    '''Première approche --> récup + affichage de la data'''
    for i, scan in enumerate(RPLidar.iter_scans(lidar,'express',5000,5)):
        print('%d: Got %d measures' % (i, len(scan)))
        #data.append([[scan[j][1] for j in range(len(scan))],[scan[j][2] for j in range(len(scan))]])      
        #Angle = data[i][0]
        #Distance = data[i][1]
        
        Angle = [scan[j][1] for j in range(len(scan))]
        Distance = [scan[j][2] for j in range(len(scan))]
        
        X = [Distance[i]*cos(Angle[i]*pi/180) for i in range(len(scan))]
        Y = [Distance[i]*sin(Angle[i]*pi/180) for i in range(len(scan))]

        
        # print("X : ",X)
        # print("Y : ",Y)



        # plt.figure()
        # plt.scatter(X,Y)
        # # plt.show()
        # plt.ion()
        # plt.draw()
        # plt.pause(1)
        # plt.close()

        if i == 100:
           break

#run('./examples/data')
lidar = RPLidar(PORT_NAME)
data = []

# RPLidar.stop(lidar)
# time.sleep(3)
# RPLidar.start(lidar,'express')
# for i in range(5):
#     test(lidar)
#     time.sleep(3)
   
# with open('datalidar.txt','w') as f:
#         f.writelines(["%s\n" % item  for item in data])
#         f.close()
# except ValueError:
#     print('Issue : Value Error')
#     analyse1(lidar)
# except RPLidarException:
#     print('Issue : RPlidar Error')
#     analyse1(lidar)

