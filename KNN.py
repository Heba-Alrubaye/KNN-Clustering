import sys
import csv
import operator
import math
import numpy as np


#getdata() function definition
def getdata(file):
    array = []
    with open(file,'r') as f:
        next(f)
        reader = csv.reader(f)
        for row in reader:
            array.append([])#2D array
            array[-1]= list(np.fromstring(row[0], dtype=float, sep=' '))
    return array


def euclideanDist(a, b,r):  # (trainig,test,dif(max-min))
    d = 0.0
    for i in range(len(a)-1):
        d += pow((float(a[i])-float(b[i])),2)/r[i]
    d = math.sqrt(d)
    return d

def calculateR(a):# Normalization
    maxvalue=a.max(axis=0)
    minvalue=a.min(axis=0)
    dif=maxvalue-minvalue
    dif=pow(dif,2)
    return dif

#KNN prediction and model training
def knn_predict(test_data, train_data,r,k_value):
    for i in test_data:
        eu_Distance =[]
        knn = []
        Class_1 = 0
        Class_2 = 0
        Class_3 = 0
        for j in train_data:
            eu_dist = euclideanDist(j,i,r)
            eu_Distance.append((j[-1], eu_dist))
        eu_Distance.sort(key = operator.itemgetter(1))#arrange according to 2nd elemnts in tuple
        knn = eu_Distance[:k_value]
        for k in knn:
            if k[0] ==1:
                Class_1 += 1
            elif k[0]==2:
                Class_2 +=1
            else:
                Class_3+=1
        Classarray = [(1,Class_1),(2,Class_2),(3,Class_3)]
        Classarray.sort(reverse = True,key=operator.itemgetter(1))
        index = Classarray[0]
        ClassLabl = index[0]
        i.append(ClassLabl)
        print(i)


#Accuracy calculation function
def accuracy(test_data):
    correct = 0
    for i in test_data:
        if i[-1] == i[-2]:
            correct += 1
    accuracy = float(correct)/len(test_data) *100  #accuracy
    return accuracy

def main():
    args = {'trainingF': sys.argv[1], 'testingF': sys.argv[2], 'K':sys.argv[3]}
    training_data = getdata(args['trainingF'])
    R_sqr = calculateR(np.array(training_data))
    test_data = getdata(args['testingF'])
    k=int (args['K'])
    knn_predict(test_data, training_data, R_sqr, k)
    print("Accuracy : ", accuracy(test_data))

if __name__ == '__main__':
    main()