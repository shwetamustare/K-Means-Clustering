	#Title:K-means clustering (multiple attributes)	

	import sys
	import csv
	from scipy.spatial import distance
	import numpy as np
	import random
	import math

	X = 0
	Y = 1
	def loadCsv(filename):            
	    #np.loadtxt(file_,dtype=object)        #Reading the csv file
	    lines = csv.reader(open(filename, "rb"))
	    dataset = list(lines)
	    print "Height,Weight,FootSize"
	    for i in range(len(dataset)):
		dataset[i] = [float(x) for x in dataset[i]]
		print dataset[i]
	    return dataset

	def get_first(k, points):           #function to return mean points/values
	    return points[0:k]

	def cost(centroids, clusters):      #determining euclidean distance for each value in cluster to another cluster
	    cost = 0

	    for i in range(len(centroids)):
		centroid = centroids[i]
		cluster = clusters[i]
		for point in cluster:
		    cost += (distance.euclidean(centroid, point))**2

	    return math.sqrt(cost)

	def compute_centroids(clusters):    #function for creation of centroids
	    centroids = []

	    for cluster in clusters:
		centroids.append(np.mean(cluster, axis=0))

	    return centroids

	def kmeans(k, centroids, points, method, iter):         #Iterations performed to sort into correct clusters
	    clusters = [[] for i in range(k)]

	    for i in range(len(points)):
		point = points[i]
		belongs_to_cluster = closest_centroid(point, centroids)
		clusters[belongs_to_cluster].append(point)

	    new_centroids = compute_centroids(clusters)

	    if not equals(centroids, new_centroids):
		print "Iteration " + str(iter) + ". Cost [k=" + str(k) + ", " + method + "] = " + str(cost(new_centroids, clusters))

		clusters = kmeans(k, new_centroids, points, method, iter+1)
		print ""
		print "Intermediate clusters:"
		for i in range (0,k):
			print "Cluster",i
			print clusters[i]
	    return clusters

	def closest_centroid(point, centroids):             #actual comparison to check distance from each cluster
	    min_distance = float('inf')
	    belongs_to_cluster = None
	    for j in range(len(centroids)):
		centroid = centroids[j]
		dist = distance.euclidean(point, centroid)
		if dist < min_distance:
		    min_distance = dist
		    belongs_to_cluster = j
	    return belongs_to_cluster



	def equals(points1, points2):               #function to check if cluster formed from each cluster is the same as the one in the previous iteration
	    if len(points1) != len(points2):
		return False

	    for i in range (len(points1)):
		point1 = points1[i]
		point2 = points2[i]
		if point1[X] != point2[X] or point1[Y] != point2[Y]:
		    return False
	    
	    return True

	if __name__ == "__main__":                  #main function 
	    
	    filename=raw_input ("Enter the name of your csv file ")
	    dataset = loadCsv(filename)
	    k = input("Enter number of clusters you want: ")
	    # k-means picking the first k points as centroids
	    centroids = get_first(k, dataset)
	    clusters = kmeans(k, centroids, dataset, "first", 1)
	    print("")
	    print "Final Clusters are: "
	
	    for ii in range(0,k):
		print "Cluster ",ii
		print "is",clusters[ii]



	'''
	OUTPUT:
	[ccoew@localhost ~]$ python k.py
	Enter the name of your csv file input.csv
	Height,Weight,FootSize
	[185.0, 72.0, 7.0]
	[170.0, 56.0, 2.0]
	[168.0, 60.0, 6.0]
	[179.0, 68.0, 8.0]
	[182.0, 72.0, 9.0]
	[188.0, 77.0, 10.0]
	[180.0, 71.0, 12.0]
	[180.0, 70.0, 6.0]
	[183.0, 84.0, 5.0]
	[180.0, 88.0, 4.0]
	[180.0, 67.0, 13.0]
	[177.0, 76.0, 9.0]
	Enter number of clusters you want: 5
	Iteration 1. Cost [k=5, first] = 18.9164831122
	Iteration 2. Cost [k=5, first] = 16.2157331009
	Iteration 3. Cost [k=5, first] = 14.1480269531

	Intermediate clusters:
	Cluster 0
	[[188.0, 77.0, 10.0], [183.0, 84.0, 5.0], [180.0, 88.0, 4.0]]
	Cluster 1
	[[170.0, 56.0, 2.0]]
	Cluster 2
	[[168.0, 60.0, 6.0]]
	Cluster 3
	[[185.0, 72.0, 7.0], [179.0, 68.0, 8.0], [182.0, 72.0, 9.0], [180.0, 71.0, 12.0], [180.0, 70.0, 6.0], [180.0, 67.0, 13.0]]
	Cluster 4
	[[177.0, 76.0, 9.0]]

	Intermediate clusters:
	Cluster 0
	[[188.0, 77.0, 10.0], [183.0, 84.0, 5.0], [180.0, 88.0, 4.0]]
	Cluster 1
	[[170.0, 56.0, 2.0]]
	Cluster 2
	[[168.0, 60.0, 6.0]]
	Cluster 3
	[[185.0, 72.0, 7.0], [179.0, 68.0, 8.0], [182.0, 72.0, 9.0], [180.0, 71.0, 12.0], [180.0, 70.0, 6.0], [180.0, 67.0, 13.0]]
	Cluster 4
	[[177.0, 76.0, 9.0]]

	Intermediate clusters:
	Cluster 0
	[[188.0, 77.0, 10.0], [183.0, 84.0, 5.0], [180.0, 88.0, 4.0]]
	Cluster 1
	[[170.0, 56.0, 2.0]]
	Cluster 2
	[[168.0, 60.0, 6.0]]
	Cluster 3
	[[185.0, 72.0, 7.0], [179.0, 68.0, 8.0], [182.0, 72.0, 9.0], [180.0, 71.0, 12.0], [180.0, 70.0, 6.0], [180.0, 67.0, 13.0]]
	Cluster 4
	[[177.0, 76.0, 9.0]]

	Final Clusters are: 
	Cluster  0
	is [[188.0, 77.0, 10.0], [183.0, 84.0, 5.0], [180.0, 88.0, 4.0]]
	Cluster  1
	is [[170.0, 56.0, 2.0]]
	Cluster  2
	is [[168.0, 60.0, 6.0]]
	Cluster  3
	is [[185.0, 72.0, 7.0], [179.0, 68.0, 8.0], [182.0, 72.0, 9.0], [180.0, 71.0, 12.0], [180.0, 70.0, 6.0], [180.0, 67.0, 13.0]]
	Cluster  4
	is [[177.0, 76.0, 9.0]]
	[ccoew@localhost ~]$ 

	'''
