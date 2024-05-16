# statisctical analysis of the data in csv file using pandas path ../sourcedata/merge.csv

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the data from the csv file
data = pd.read_csv('../sourcedata/merge.csv')

# plot 'Temperatur' vs 'Umsatz' for 'Datum' '2014-06-21 to 2014-06-30'
data['Datum'] = pd.to_datetime(data['Datum'])
data = data.set_index('Datum')
data = data.loc['2014-06-21':'2014-06-30']
data.plot(y='Umsatz', x='Temperatur', style='o')
plt.title('Umsatz vs Temperatur')
plt.xlabel('Temperatur')
plt.ylabel('Umsatz')
plt.savefig('../results/plot1.png')
plt.show()  

