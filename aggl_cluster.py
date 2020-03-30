
#%%
#import csv
import pandas as pd 

data = pd.read_csv('fifa20.csv')
data.head()

#%%
#choose data that we will use

dt = data[['age','overall']]

#%%
#drop row that contains NaN values

dt.dropna()

#%%
#dataframe to list

dt_ready = dt.values.tolist()

#%%
#agglomorative clustering process
#I use sklearn library for this assigment

from sklearn.cluster import AgglomerativeClustering

cluster = AgglomerativeClustering(n_clusters = 4)
cluster.fit(dt_ready)
cluster.labels_

# %%
#show clusters 
import matplotlib.pyplot as plt

plt.scatter(dt['age'],dt['overall'],c=cluster.labels_,cmap='rainbow')
plt.title('FIFA 20 Clustering')
plt.xlabel('age')
plt.ylabel('overall')
plt.show()

# %%
