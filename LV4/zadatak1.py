from sklearn import datasets
from sklearn . model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib . pyplot as plt
from sklearn . preprocessing import MinMaxScaler
from sklearn . preprocessing import OneHotEncoder
import sklearn . linear_model as lm
from sklearn import metrics
data=pd.read_csv('data_C02_emission.csv')


# podaci iz drugacijih datoteka se mogu ucitati i s:
# somedata = datasets.name_of_dataset()
# df = pd.DataFrame(data=somedata.data, columns=somedata.feature_names)
# df['target'] = somedata.target
# df.to_csv('somedata.csv', index=False)
# print(df.info)


# drop sve kategoriske velicine tj one s tekstom
data = data.drop(["Make", "Model"], axis=1)

input_variables=['Fuel Consumption City (L/100km)',
                 'Fuel Consumption Hwy (L/100km)',
                 'Fuel Consumption Comb (L/100km)',
                 'Fuel Consumption Comb (mpg)',
                 'Engine Size (L)',
                 'Cylinders']

output_variables=['CO2 Emissions (g/km)']
x=data[input_variables].to_numpy()
y=data[output_variables].to_numpy()
#a
X_train , X_test , y_train , y_test = train_test_split (x , y , test_size = 0.2 , random_state =1 )

#b
plt.scatter(X_train[:,3], y_train, c='blue', s=2)
plt.scatter(X_test[:,3], y_test, c='red', s=2)
plt . show ()
#c
sc = MinMaxScaler ()
X_train_n = sc . fit_transform ( X_train )
X_test_n = sc . transform ( X_test )

plt.hist(X_train[:,3], bins=20)
plt.show()
plt.hist(X_train_n[:,3], bins=20)
plt.show()

plt.figure()
plt.title('Podaci prije skaliranja')
plt.hist(X_train[:, 0])
plt.figure()
plt.title('Podaci nakon skaliranja')
plt.hist(X_train_n[:, 0])
plt.show()

#d
linearModel = lm . LinearRegression ()
linearModel . fit ( X_train_n , y_train )

print(linearModel.coef_)

y_test_p = linearModel . predict ( X_test_n )

plt.scatter(y_test_p, y_test, c='blue' )
# e
lr = LinearRegression()
lr.fit(X_train_n, y_train)  # i ovdje se isto koristi skalirani ulazni podaci

# Predviđanje izlaznih vrijednosti na skupu za testiranje koji je skaliran
y_test_pred = lr.predict(X_test_n)

# Prikaz dijagrama raspršenja
plt.scatter(y_test, y_test_pred, s=4, c='r')
plt.xlabel('Stvarne vrijednosti')
plt.ylabel('Procijenjene vrijednosti')
plt.title('Dijagram raspršenja stvarnih i procijenjenih vrijednosti')
plt.show()


# f
# predikcija izlazne velicine na skupu podataka za testiranje
y_test_p = linearModel.predict(X_test_n)
# evaluacija modela na skupu podataka za testiranje pomocu MAE
MAE = mean_absolute_error(y_test, y_test_p)
MSE = mean_squared_error(y_test, y_test_pred)
RMSE = math.sqrt(MSE)
R2 = r2_score(y_test, y_test_pred)
MAPE = mean_absolute_percentage_error(y_test, y_test_p)


# Ispisivanje rezultata
print("Srednja apsolutna greška (MAE):", MAE)
print("Srednja apsolutna postotna greška (MAPE):", MAPE)
print("Srednja kvadratna greška (MSE):", MSE)
print("Korijen iz srednje kvadratne pogreške:", RMSE)
print("Koeficijent determinacije (R2):", R2)


# g
# promjenom broja ulaznih parametara mijenjaju se i metrike. R2 koeficijent se priblizava 1 s povecanjem broja ulaznih velicina, dok se ostale metrike smanjuju
# mape, mpe i mse(greske) se smanjuju povecanjem broja ulaznih velicina,a a korijen iz srednje kvadatne pogreške(RMSE) se povecava


MSE=metrics.r2_score(y_test, y_test_p)
print(MSE)

#smanjivanjem ulaznih parametara smanjuje se r2 score
