import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV

def plot_decision_regions(X, y, classifier, resolution=0.02):
plt.figure()
# setup marker generator and color map
markers = ('s', 'x', 'o', '^', 'v')
colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
cmap = ListedColormap(colors[:len(np.uniqueDa)])

# plot the decision surface
x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
np.arange(x2_min, x2_max, resolution))
Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
Z = Z.reshape(xx1.shape)
plt.contourf(xx1, xx2, Z, alpha=0.3, cmap=cmap)
plt.xlim(xx1.min(), xx1.max())
plt.ylim(xx2.min(), xx2.max())

# plot class examples
for idx, cl in enumerate(np.uniqueDa):
plt.scatter(x=X[y == cl, 0],
y=X[y == cl, 1],
alpha=0.8,
c=colors[idx],
marker=markers[idx],
label=cl)


# ucitaj podatke
data = pd.read_csv("Social_Network_Ads.csv")
print(data.info())

data.hist()
plt.show()

# dataframe u numpy
X = data[["Age","EstimatedSalary"]].to_numpy()
y = data["Purchased"].to_numpy()

# podijeli podatke u omjeru 80-20%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, stratify=y, random_state = 10)

# skaliraj ulazne velicine
sc = StandardScaler()
X_train_n = sc.fit_transform(X_train)
X_test_n = sc.transform((X_test))

# Model logisticke regresije
LogReg_model = LogisticRegression(penalty=None)
LogReg_model.fit(X_train_n, y_train)

# Evaluacija modela logisticke regresije
y_train_p = LogReg_model.predict(X_train_n)
y_test_p = LogReg_model.predict(X_test_n)

print("Logisticka regresija: ")
print("Tocnost train: " + "{:0.3f}".format((accuracy_score(y_train, y_train_p))))
print("Tocnost test: " + "{:0.3f}".format((accuracy_score(y_test, y_test_p))))

# granica odluke pomocu logisticke regresije
plot_decision_regions(X_train_n, y_train, classifier=LogReg_model)
plt.xlabel('x_1')
plt.ylabel('x_2')
plt.legend(loc='upper left')
plt.title("Tocnost: " + "{:0.3f}".format((accuracy_score(y_train, y_train_p))))
plt.tight_layout()
plt.show()

# inicijalizacija i ucenje KNN modela
KNN_model = KNeighborsClassifier ( n_neighbors = 5 )
KNN_model . fit ( X_train_n , y_train )
# inicijalizacija i ucenje SVM modela
SVM_model = svm . SVC (kernel ='rbf', gamma = 1 , C=0.1)
SVM_model . fit ( X_train_n , y_train )
# predikcija na skupu podataka za testiranje
y_test_p_KNN = KNN_model . predict ( X_test )
y_test_p_SVM = SVM_model . predict ( X_test )

#1
# Evaluacija modela knn
y_train_p = KNN_model.predict(X_train_n)
y_test_p = KNN_model.predict(X_test_n)

print("KNN: ")
print("Tocnost train: " + "{:0.3f}".format((accuracy_score(y_train, y_train_p))))
print("Tocnost test: " + "{:0.3f}".format((accuracy_score(y_test, y_test_p))))

# granica odluke pomocu knn
plot_decision_regions(X_train_n, y_train, classifier=KNN_model)
plt.xlabel('x_1')
plt.ylabel('x_2')
plt.legend(loc='upper left')
plt.title("Tocnost: " + "{:0.3f}".format((accuracy_score(y_train, y_train_p))))
plt.tight_layout()
plt.show()

#3
# Evaluacija modela svm
y_train_p = SVM_model.predict(X_train_n)
y_test_p = SVM_model.predict(X_test_n)

print("SVM: ")
print("Tocnost train: " + "{:0.3f}".format((accuracy_score(y_train, y_train_p))))
print("Tocnost test: " + "{:0.3f}".format((accuracy_score(y_test, y_test_p))))

print("train accuracy: " + "{:0.3f}".format((accuracy_score(y_train, y_train_p))))
print("test accuracy: " + "{:0.3f}".format((accuracy_score(y_test, y_test_p_SVM))))

#2
KNN_model2 = KNeighborsClassifier()
param_grid = {"n_neighbors": np.arange(1, 100)}
knn_gs = GridSearchCV(KNN_model2, param_grid, cv = 5 )
knn_gs.fit(X_train_n, y_train )
print (knn_gs.best_params_)

# unakrsna validacija
scores = cross_val_score(KNN2, X_train_n, y_train, cv=5)
print('cv_scores mean:{}'.format(np.mean(scores)))

#4
SVM_model2 = svm.SVC(kernel ="rbf", gamma = 1, C=0.1 )
param_grid = {"C": [10 , 100 , 100 ], "gamma": [10 , 1 , 0.1 , 0.01 ]}
svm_gscv = GridSearchCV( SVM_model2 , param_grid , cv =5 , scoring ="accuracy", n_jobs = -1 )
svm_gscv.fit( X_train_n , y_train )

# 1.1.
# za razliku od logisticke regresije, knn ima bolju tocnost(i sa skupom testiranja i treniranja), granica vise nije ravna linija vec zakrivljena i bolje odvaja podatke

# 1.2
# razlika kada upotrijebimo K=1 i K=100: granica s 1 izgelda ne definirano i raspisano, postoji puno "otoka"(tocnost je 0.994-dogada se overfitting)
# sa K=100  granica jedne klase je jako povucena u drugu klasu, vidi se iz samog grafa (tocnost je 0.787-dogada se underfitting)
print (svm_gscv.best_params_)
print (svm_gscv.best_score_)



# zadatak 3
# Kako promjena ovih hiperparametara utjece na granicu odluke te pogrešku na skupu podataka za testiranje? ˇ
# Mijenjajte tip kernela koji se koristi. Što primjecujete?

# za gama=0.1, C se mijenja
# smanjivanjem parametra C, crvena klasa se povecava, u ekstremnom slucaju za C=0.01 svi podaci pripadaju samo jednoj klasi
# povecanajem parametra C, na C=1000, vrlo je dobro definirana granica izmedu dvije klase, ali postoji i  prostor duge klase u kojem zapravo nema podataka
# ako koristimo C=100,00 granica je vrlo blizu savrsenosti

# za C=10, a gama se mijenja
# za gamma=0.001 granica je izgledom blizu pravca, dok za gamma=10: zaokruzuje se prostor oko podataka i nastaju otoci
# za gamma=1000, svaki podatak je otok za sebe i to u vrlo suzenom prostoru, najblizi podaci se spajaju u  zajednicki otok kad je gamma=100


# sto vise overfittamo podatke, kao npr za gamma=1000, tocnost na skupu za treniranje je oko 0.994,
# dok je za testni skup ona samo 0.650
# ako uzmemo gamma=1 i C=10, sto bi bio najbolji izbor za ovaj slucaj- tocnost skupa za treniranje je 0.922, a za test je 0.925, sto znaci da je granica odlicno postavljena
