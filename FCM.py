# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 19:45:52 2020

@author: QXRZDRAGON
"""

from numpy import *
import numpy as np
import matplotlib.pyplot as plt
def euclidean_distance(x1,x2,y1,y2):
    dist = sqrt((x2-x1)**2+(y2-y1)**2)
    return dist

def new_cluster(x1,x2,y1):
    new_cluster = (1/x1)/((1/x2)+(1/y1))
    return new_cluster

dataset = array([
        [1.0,2.0,3.0,4.0,5.0,6.0],
        [6.0,5.0,8.0,4.0,7.0,9.0],
     ])

cluster = array([
       [0.0,0.0,0.0,0.0,0.0,0.0],
        [0.0,0.0,0.0,0.0,0.0,0.0]
     ])

dist = array([
       [0.0,0.0,0.0,0.0,0.0,0.0],
        [0.0,0.0,0.0,0.0,0.0,0.0]
    ]) 

centroid = ([[2.41,4.86],
       [6.16,6.89]])  
    
w = 2 
iterasi = 0


print('Data yang dipakai: \n')
print('dataset: \n', dataset)
print('Centroid awal: \n', centroid[:][0],'\n',centroid[:][1])
print("\n\niterasi: ", iterasi+1)
for i in range(dataset.shape[1]):
        dist[0][i] = euclidean_distance(centroid[0][0], dataset[0][i], centroid[1][0], dataset[1][i])
        dist[1][i] = euclidean_distance(centroid[0][1], dataset[0][i], centroid[1][1], dataset[1][i])
        
print('Ecludian Distance: \n', dist)

for i in range(dist.shape[1]):
        cluster[0][i] = new_cluster(dist[0][i], dist[0][i], dist[1][i])
        cluster[1][i] = new_cluster(dist[1][i], dist[0][i],dist[1][i])
            
print('\nCluster: \n', cluster)

for i in range(dataset.shape[0]):
        for j in range(dataset.shape[1]):
            if cluster[0][j] == 1:        
                plt.scatter(dataset[0,j], dataset[1, j], c='red', s=50, alpha=0.5)
            else:
                plt.scatter(dataset[0,j], dataset[1, j], c='blue', s=50, alpha=0.5)
                
plt.scatter(centroid[0][0], centroid[1][0], c='green', s=50, alpha=0.5)
plt.scatter(centroid[0][1], centroid[1][1], c='purple', s=50, alpha=0.5)