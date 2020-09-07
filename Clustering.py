import numpy as np
import csv
import math
import sys


np.random.seed(100)

def getdata(file):
    array = []
    with open(file,'r') as f:
        next(f)
        reader = csv.reader(f)
        for row in reader:
            array.append([])  # array = [[row1], [row2]] 2D array
            array[-1]= list(np.fromstring(row[0], dtype=float, sep=' '))
    return array
    # print(array)

def get_maxmin(a):# to specify centroide value
    maxvalue=a.max(axis=0)
    minvalue=a.min(axis=0)
    return maxvalue,minvalue

def euclideanDist(a,b): # (trainig,test)
    d = 0.0
    for i in range(len(a)-1):
        d += pow((float(a[i])-float(b[i])),2)
    d = math.sqrt(d)
    return d

def main():
    args = {'trainingF': sys.argv[1],'K':sys.argv[2]}
    data = getdata(args['trainingF'])
    k=int(args['K'])

    # 1-randomly initialize centroids
    maxv, minv = get_maxmin(np.array(data))  # maxv is the maximal values of all columns maxv = [33, 12.3, 13.5,..], minv = [0.4,0.3, 0.7,..]
    centroids ={}
    for i in range(k):
        array=[]
        for j in range(13):# len attributes=13
            array.append(np.random.uniform(minv[j], maxv[j]))
            centroids[i+1] = array



    # 2-calculate the distance between centroid and all nodes
    # for each node n:
    #     calculate the distance between n and all centroids
    #     assign n to the cluster with the smallest distance

    for Z in range(3):#  how many time implement to get the new centroids
        clusterLab=[]
        for i in range(len(data)):
            array = []
            node = data[i]
            for j in range(k):
                cen = centroids[j+1]
                dist = euclideanDist(node,cen)
                array.append(dist)
                # print(array)
            index = array.index(min(array))
            cluster = index+1
            clusterLab.append(cluster)
        # 3-update all centroids:  average all nodes within one cluster to find new centroid
        # for each node n: # find out the nodes that belong to the cluster c
        #     if cluster label of n == 1:
        #            add n to sum1  # sum1 is the summation of nodes belong to cluster 1
        #     elif cluster label of n == 2:
        #           add n to sum2
        #     else:
        #           add n to sum3
        # average the sum1, sum2, sum3 respectively to get the new three centroids
        # reapet step 2
        sum = []
        count = [0]*k
        for iter in range(k):
            sum.append([])  # sum = [[sum1, [], []]
            sum[iter]=np.array([0]*13)# empty array * size

        for j in range(89):#len data=89
            for iter in range(k):
                if clusterLab[j]==(iter+1):
                    sum[iter] = sum[iter]+ data[j][:13]# ignore last column (is class label)
                    count[iter] +=1
        #  report the number of instances in each cluster
        print('Node number at each Clusters at the %s-th iteration'%Z)
        for iter in range(k):
            print("Cluster%s: %s" % (iter+1,count[iter]))
            # average the sum1, sum2, sum3 respectively to get the new three centroids
            centroids[iter+1] = sum[iter]/count[iter]
            for node in range(89):# len data
                if clusterLab[node]==(iter+1):
                    print("Node Class Label:{}".format((data[node][-1])))
                    continue


if __name__ == '__main__':
    main()