import pandas as pd

data = pd.read_csv('data_C02_emission.csv')


data['Fuel Type'] = data['Fuel Type'].astype("category")
data['Transmission'] = data['Transmission'].astype("category")
data['Vehicle Class'] = data['Vehicle Class'].astype("category")
data['Model'] = data['Model'].astype("category")
data['Make'] = data['Make'].astype("category")


#a)
print(len(data))
print(data.info())
print(data.describe())
data.dropna(axis=0)
data.drop_duplicates()
data = data.reset_index(drop=True)

#b)
print(data.sort_values(by=['Fuel Consumption City (L/100km)']).head(3)[['Make','Model','Fuel Consumption City (L/100km)']])
print(data[['Make', 'Model', 'Fuel Consumption City (L/100km)']
           ].iloc[data['Fuel Consumption City (L/100km)'].argsort().tail(3)])



#c)
engineRestrictedData = data[(data['Engine Size (L)'] >=2.5) & data["Engine Size (L)"]<= 3.5]
print(len(engineRestrictedData))

print(engineRestrictedData['CO2 Emissions (g/km)'])


#d)
Audi = data[(data['Make'] == "Audi")]
print(len(Audi))
print(Audi[(Audi['Cylinders'] == 4)]['CO2 Emissions (g/km)'])


#e)
cylinders = data.groupby('Cylinders')
print(cylinders.size())
print(cylinders['CO2 Emissions (g/km)'].mean())


#f)
diesel_cars = data[(data['Fuel Type'] == 'D')]
benz_cars = data[(data['Fuel Type'] == 'X')]

print(diesel_cars['Fuel Consumption City (L/100km)'].mean())
print(benz_cars['Fuel Consumption City (L/100km)'].mean())
print(diesel_cars['Fuel Consumption City (L/100km)'].median())
print(benz_cars['Fuel Consumption City (L/100km)'].median())


#g)
cylinder4_and_diesel = data[(data['Cylinders'] == 4) & (data['Fuel Type'] == 'D')]
print(cylinder4_and_diesel.sort_values(by = 'Fuel Consumption City (L/100km)').tail(1)[['Make','Model','Fuel Consumption City (L/100km)']])


#h)
manual = data[(data['Transmission'].str.contains("M",case = False))]
manual = manual.reset_index(drop = True)
print(len(manual))


#i)
print(data.corr(numeric_only=True))
