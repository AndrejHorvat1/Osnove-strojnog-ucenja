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

input_variables=['Fuel Consumption City (L/100km)',
                 'Fuel Consumption Hwy (L/100km)',
                 'Fuel Consumption Comb (L/100km)',
                 'Fuel Consumption Comb (mpg)',
                 'Engine Size (L)',
                 'Cylinders']

output_variables=['CO2 Emissions (g/km)']
x=data[input_variables].to_numpy()
y=data[output_variables].to_numpy()

X_train , X_test , y_train , y_test = train_test_split (x , y , test_size = 0.2 , random_state =1 )


plt.scatter(X_train[:,3], y_train, c='blue', s=2)
plt.scatter(X_test[:,3], y_test, c='red', s=2)
plt . show ()

sc = MinMaxScaler ()
X_train_n = sc . fit_transform ( X_train )
X_test_n = sc . transform ( X_test )

plt.hist(X_train[:,3], bins=20)
plt.show()
plt.hist(X_train_n[:,3], bins=20)
plt.show()


linearModel = lm . LinearRegression ()
linearModel . fit ( X_train_n , y_train )

print(linearModel.coef_)

y_test_p = linearModel . predict ( X_test_n )

plt.scatter(y_test_p, y_test, c='blue' )


MSE=metrics.r2_score(y_test, y_test_p)
print(MSE)

#smanjivanjem ulaznih parametara smanjuje se r2 score