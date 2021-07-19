		#Title   : k-means clustering
		

	import random
	def min(val,centroids):
	    diff=999
	    index=999

	    for i in range(len(centroids)):
		d=abs(val-centroids[i])
		if d<diff:
		    diff=d
		    index=i
	    return index

	num=input("Enter no of elements: ")   		#accept input array
	data=[]
	for i in range(num):
		data.append(input("Enter elements: "))
	print data
	k=input("Enter no of clusters: ")		# accept number of clusters
	rand=k
	centroids=[]
	clusters=[]
	new_cluster=[]
	while (rand>0):
	    x=random.randrange(1,num)			#decide the random centroids
	    if data[x] not in centroids:
		centroids.append(data[x])
		rand=rand-1
		sep=[]
		sep.append(data[x])
		clusters.append(sep)
		del sep
	print "the centroids are:",centroids

	flag=cmp(clusters,new_cluster)			#compare if new and previous clusters are equal
	while(flag!=0):					#if not form new clusters
	    for _ in centroids:				
		temp=[]
		new_cluster.append(temp)
	 	del temp

	    for val in data:				#compare the elemnet of array with the nearest centroid and form a new cluster
		index=min (val,centroids)
		print val,"belongs in cluster: ",index+1
		new_cluster[index].append(val)
	    print "clusters formed: ",new_cluster

	    flag=cmp(clusters,new_cluster)		#compare if new and previous clusters are equal
	    if flag==0:					#if equal exit
		break

	    del clusters[:]
	    for val in new_cluster:
		clusters.append(val)
	    del centroids[:]
	    del new_cluster[:]

	    for i in clusters:				#calculate the new average centroid from new cluster
		avg=0.0
		for val in i:
		    avg=avg+val
		avg=avg/len(i)
		centroids.append(avg)
	    print "new centroids are :",centroids

	print "The final clusters are as follows: "
	for a in new_cluster:
	    print a


	OUTPUT :

	[ccoew@localhost ~]$ python kmeans.py
	Enter no of elements: 10
	Enter elements: 11
	Enter elements: 22
	Enter elements: 33
	Enter elements: 44
	Enter elements: 55
	Enter elements: 66
	Enter elements: 77
	Enter elements: 88
	Enter elements: 99
	Enter elements: 101
	[11, 22, 33, 44, 55, 66, 77, 88, 99, 101]
	Enter no of clusters: 3
	the centroids are: [44, 77, 88]
	11 belongs in cluster:  1
	22 belongs in cluster:  1
	33 belongs in cluster:  1
	44 belongs in cluster:  1
	55 belongs in cluster:  1
	66 belongs in cluster:  2
	77 belongs in cluster:  2
	88 belongs in cluster:  3
	99 belongs in cluster:  3
	101 belongs in cluster:  3
	clusters formed:  [[11, 22, 33, 44, 55], [66, 77], [88, 99, 101]]
	new centroids are : [33.0, 71.5, 96.0]
	11 belongs in cluster:  1
	22 belongs in cluster:  1
	33 belongs in cluster:  1
	44 belongs in cluster:  1
	55 belongs in cluster:  2
	66 belongs in cluster:  2
	77 belongs in cluster:  2
	88 belongs in cluster:  3
	99 belongs in cluster:  3
	101 belongs in cluster:  3
	clusters formed:  [[11, 22, 33, 44], [55, 66, 77], [88, 99, 101]]
	new centroids are : [27.5, 66.0, 96.0]
	11 belongs in cluster:  1
	22 belongs in cluster:  1
	33 belongs in cluster:  1
	44 belongs in cluster:  1
	55 belongs in cluster:  2
	66 belongs in cluster:  2
	77 belongs in cluster:  2
	88 belongs in cluster:  3
	99 belongs in cluster:  3
	101 belongs in cluster:  3
	clusters formed:  [[11, 22, 33, 44], [55, 66, 77], [88, 99, 101]]
	The final clusters are as follows: 
	[11, 22, 33, 44]
	[55, 66, 77]
	[88, 99, 101]



