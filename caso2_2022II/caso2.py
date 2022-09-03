#%% 
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.dates as mdates
import seaborn as sns
# %%
data = pd.read_csv('dataCaso2.txt' , sep = "\t\t")
data = data.columns
# %%

#Se leen los datos
data = open('dataCaso2.txt').read().split("   ")

data = [float(x)  for x in data  if bool(x)]

#%%

distribucion = { i : data.count(i) for i in list(set(data)) }

distribucionRelativa = { i : data.count(i)/len(data) for i in list(set(data)) }

distribucionRelativa_Series = pd.Series(distribucionRelativa)





# %%
fig , ax = plt.subplots()
plt.bar(distribucionRelativa_Series.index , distribucionRelativa_Series.values)