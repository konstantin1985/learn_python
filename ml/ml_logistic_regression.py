

# MAIN SOURCE:
# http://www.data-mania.com/blog/logistic-regression-example-in-python/

# USEFUL LINKS:
#
# 1) How to save seaborn boxplot 
# https://stackoverflow.com/questions/35839980/how-to-save-picture-boxplot-seaborn
#
# 2) Small introduction to pandas
# http://pythonforengineers.com/introduction-to-pandas/
#
# 3) sklearn.cross_validation.train_test_split
# https://stackoverflow.com/questions/28064634/random-state-pseudo-random-numberin-scikit-learn
#

# GENERAL INFORMATION:


import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib
import matplotlib.pyplot as plt
import sklearn

from pandas import Series, DataFrame
from pylab import rcParams
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics 
from sklearn.metrics import classification_report


# Finds each null value in the Age variable and for
# each null checks the value of Pclass and assigns age
# value according to the average age of passengers in
# that class 
def age_approx(cols):
    Age = cols[0]
    Pclass = cols[1]
    
    if pd.isnull(Age):
        if Pclass == 1:
            return 37
        elif Pclass == 2:
            return 29
        else:
            return 24
    else:
        return Age



print('Start of the program')

# Read CSV (comma-separated) file into DataFrame
# and assign column names
print(20 * '=' + '0' + 20 * '=')
url = 'https://raw.githubusercontent.com/BigDataGal/Python-for-Data-Science/master/titanic-train.csv'
titanic = pd.read_csv(url)
titanic.columns = ['PassengerId','Survived','Pclass','Name','Sex','Age','SibSp','Parch','Ticket','Fare','Cabin','Embarked']
print(titanic.head(1))

# Easily check missing values
print(20 * '=' + '1' + 20 * '=')
print(titanic.isnull().sum())

# Drop irrelevant data
print(20 * '=' + '2' + 20 * '=')
titanic_data = titanic.drop(['PassengerId','Name','Ticket','Cabin'], 1)
print(titanic.head(1))

# Look at how passenger age is related to their ticket class
# The younger the passenger is, the more likely it's in the 
# lower class
print(20 * '=' + '3' + 20 * '=')
a = sb.boxplot(x='Pclass', y='Age', data=titanic_data, palette='hls')
a.get_figure().savefig('ax.png')

# Fill the absent Age fields
print(20 * '=' + '4' + 20 * '=')
# For pandas objects, the indexing operator [] only accepts
# colname or list of colnames to select column(s).
# axis: 1 or 'columns': apply function to each row
titanic_data['Age'] = titanic_data[['Age', 'Pclass']].apply(age_approx, axis=1)
print(titanic_data.isnull().sum())

# Drop two records with null embarked value
print(20 * '=' + '5' + 20 * '=')
# inplace : boolean, default False 
# If True, do operation inplace and return None.
# Drop entries with any or all data missing.
titanic_data.dropna(inplace=True)
print(titanic_data.isnull().sum())

# The next thing we need to do is reformat our variables so that
# they work with the model. Specifically, we need to reformat the
# Sex and Embarked variables into numeric variables.
print(20 * '=' + '6' + 20 * '=')
# Convert categorical variable into dummy/indicator variables
# drop_first : bool, default False
# Whether to get k-1 dummies out of k categorical levels by removing the first level.
gender = pd.get_dummies(titanic_data['Sex'], drop_first=True)
print(gender.head(2))
embark_location = pd.get_dummies(titanic_data['Embarked'], drop_first=True)
print(embark_location.head(2))
print(titanic_data.head(2))

# Drop old 'Sex' and 'Embarked' columns and add new columns
print(20 * '=' + '7' + 20 * '=')
# axis : int or axis name
# Whether to drop labels from the index (0 / 'index') or columns (1 / 'columns').
titanic_data.drop(['Sex', 'Embarked'],axis=1,inplace=True)
print(titanic_data.head(2))
# axis : {0/'index', 1/'columns'}, default 0. 
# The axis to concatenate along
titanic_dmy = pd.concat([titanic_data,gender,embark_location],axis=1)
print(titanic_dmy.head(2))

# Checking for independence between features
print(20 * '=' + '8' + 20 * '=')
a = sb.heatmap(titanic_dmy.corr())
a.get_figure().savefig('ax2.png')

# Fare and Pclass are not independent of each other, so I am going to drop these.
# QUESTION: don't understand why he dropped BOTH of them.
print(20 * '=' + '9' + 20 * '=')
titanic_dmy.drop(['Fare', 'Pclass'],axis=1,inplace=True)
print(titanic_dmy.head(2))

# Checking that your dataset size is sufficient. We have 6 predictive
# features that remain. The rule of thumb is 50 records per feature...
# so we need to have at least 300 records in this dataset.
print(20 * '=' + '10' + 20 * '=')
print(titanic_dmy.info())

# Create training and test sets
print(20 * '=' + '11' + 20 * '=')
X = titanic_dmy.ix[:,(1,2,3,4,5,6)].values
y = titanic_dmy.ix[:,0].values                          # Survived

# from sklearn
# If you use random_state=some_number, then you can guarantee that the
# output of Run 1 will be equal to the output of Run 2, i.e. your split
# will be always the same. 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3,
                                                    random_state=25)

# Training logistic regression
print(20 * '=' + '12' + 20 * '=')
LogReg = LogisticRegression()
LogReg.fit(X_train, y_train)

# Checking logistic regression
print(20 * '=' + '13' + 20 * '=')
y_pred = LogReg.predict(X_test)

# https://en.wikipedia.org/wiki/Confusion_matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)

# OUTPUT:
# [[137  27]
#  [ 34  69]]

# The results from the confusion matrix are telling us that 137 and 69
# are the number of correct predictions. 34 and 27 are the number of
# incorrect predictions.

# From sklearn
print(classification_report(y_test, y_pred))

# OUTPUT:
#             precision    recall  f1-score   support
#
#          0       0.80      0.84      0.82       164
#          1       0.72      0.67      0.69       103
#
#avg / total       0.77      0.77      0.77       267


print('End of the program')
