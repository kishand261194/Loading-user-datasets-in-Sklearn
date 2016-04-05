import csv
import numpy as np
from sklearn.naive_bayes import GaussianNB
import sklearn

csv = np.genfromtxt ('target.csv', delimiter=",")  #laoding from the target csv file
target = csv[:,0]

y=[int(i)for i in target]
Y=np.array(y)                               #very important shd be conterveted to NUMPY.ARRAY()
import csv
with open('data.csv', 'rb') as f:           #loading the data csv file        
    reader = csv.reader(f)
    lst = list(reader)
    x = [[(float(j)) for j in i] for i in lst]
    x = [np.array(i) for i in x]            #very import making it into NUMPY.ARRAY()   
X=np.array(x)



clf = GaussianNB()
clf.fit(X,Y)
print clf.predict([X[30]])
