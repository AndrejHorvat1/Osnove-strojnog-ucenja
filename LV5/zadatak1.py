import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

from sklearn . linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn . metrics import accuracy_score, precision_score, recall_score


X, y = make_classification(n_samples=200, n_features=2, n_redundant=0, n_informative=2,
random_state=213, n_clusters_per_class=1, class_sep=1)

# train test split
X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.2, random_state=5)

colors = ['pink', 'purple']
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train,
cmap=matplotlib.colors.ListedColormap(colors, name='purple'))
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test, marker='x',cmap=matplotlib.colors.ListedColormap(colors, name='pink'))
plt.xlabel('x1')
plt.ylabel('x2')
plt.title("Podaci za učenje i podaci za testiranje")
cbar = plt.colorbar(ticks=[0, 1])
plt.show()

# b
LogRegression_model = LogisticRegression()
LogRegression_model . fit(X_train, y_train)

# c
bias = LogRegression_model.intercept_
coefs = LogRegression_model.coef_
print(coefs.shape)
a = -coefs[0, 0]/coefs[0, 1]
c = -bias/coefs[0, 1]
x1x2min = X_train.min().min()-0.5
x1x2max = X_train.max().max()+0.5
xd = np.array([x1x2min, x1x2max])
yd = a*xd + c
plt.plot(xd, yd, linestyle='--')
plt.fill_between(xd, yd, x1x2min, color='red', alpha=0.2) # 1
plt.fill_between(xd, yd, x1x2max, color='blue', alpha=0.2) # 0
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train,
cmap=matplotlib.colors.ListedColormap(colors), edgecolor="white")
plt.xlim(x1x2min, x1x2max)
plt.ylim(x1x2min, x1x2max)
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('Podaci za treniranje i granica odluke')
cbar = plt.colorbar(ticks=[0, 1])
plt.show()


# d
y_test_p = LogRegression_model.predict(X_test)
# matrica zabune
cm = confusion_matrix(y_test, y_test_p)
print( "Matrica zabune  , cm")
disp = ConfusionMatrixDisplay(confusion_matrix(y_test, y_test_p))
disp.plot(cmap='pink')
plt.show()

print( "Tocnost"  , accuracy_score(y_test, y_test_p))
print( "Preciznost"  , precision_score(y_test, y_test_p))
print( "Odziv"  , recall_score(y_test, y_test_p))

# e
colors2 = ['black', 'green']
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test == y_test_p, cmap=matplotlib.colors.ListedColormap(
colors2))
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('Dobro i loše klasificirani primjeri')
cbar = plt.colorbar(ticks=[0, 1])
cbar.ax.set_yticklabels(['Netočno', 'Točno'])
plt.show()