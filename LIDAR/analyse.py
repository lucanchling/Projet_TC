import matplotlib.pyplot as plt
plt.close()
file = 'data' 

# FOnction pour le jeu de data
def dataread(file):
    with open(file) as f:
        lines = f.readlines()
    return lines

# Fonction pour traiter la donnée --> ressort en float les différentes valeurs dans une liste
def dataprocess(data):
    del data[0],data[0],data[0]
    data1 = [] 
    for value in data:
        data1.append(value.split(' ')[0:-1])
    newdata = [list(map(float, l)) for l in data1] 
    return newdata

# Récupération & Traitement des données
data = dataprocess(dataread(file))
first = [v[0] for v in data]
second = [v[1] for v in data]
# Partie Affichage des données 
plt.figure()
plt.plot(first,second)
plt.title("Distance(Angle)")
plt.show()