# Loading-user-datasets-in-Sklearn
In this example , you can find the easiest way to load your own CSV file as dataset into Sklearn.

In this exmaple i have used Gaussian Navie bayes classification, Genreally all the Sklearn classifiers need two CSV files.

First CSV file which is called the DATA.CSV - conatins the feature values in row wise, suppose you have taken humoments,histrograma nd mean as your feature,each feature should be appended one after the other in the row and next objects features in the corresponding coloumns .

Second CSV file contains the classes of each object whose features where extracted in the DATA.CSV in the corresponding rows and it is called the TARGET.CSV. 


eg.

DATA.CSV                                                                 TARGET.CSV

Feature vector                                                            Correspondng Class

20 30 40 1.22 3.444 5.666 77.88 544........                               0
45 23 45 1.55 12    12     43    54........                               0
35 55 12 4.7  23.6  23.6  23.6   65.7......                               1
34 55 22 11   23.6   56.7  65.6  43.1......                               2
