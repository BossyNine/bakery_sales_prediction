# add two columns one 'Feiertage' and one 'Ferientage' to ../sourcedata/cleaned_data/4_has_wettercode.csv and ../sourcedata/cleaned_data/4_missing_wettercode.csv and zero the values

import pandas as pd
import numpy as np
import os

from pandas.core.indexes.base import F

def main():

    # read in the data
    data = pd.read_csv('../sourcedata/cleaned_data/4_has_wettercode.csv', sep=',')
    data_missing = pd.read_csv('../sourcedata/cleaned_data/4_missing_wettercode.csv', sep=',')
    feiertage = pd.read_csv('../sourcedata/cleaned_data/feiertage_sh_2013-2018.csv')
    ferientage = pd.read_csv('../sourcedata/ferientage_sh_2013-2018.csv')

    # add the columns
    data['Feiertage'] = 0.0
    data['Ferientage'] = 0.0
    data_missing['Feiertage'] = 0.0
    data_missing['Ferientage'] = 0.0

    # make an python array from dataset feiertage
    feiertage = feiertage['Feiertage_SH'].values
    print(feiertage)

    for datum in feiertage:
        for i, row in data.iterrows():
            if row['Datum'] == datum:
                data.at[i, 'Feiertage'] = 1.0
                continue


    # print rows of data where Feiertage is 1.0
    print(data.loc[data['Feiertage'] == 1.0])
    
    # make same with ferientage
    ferientage = ferientage['Ferientage'].values
    print(ferientage)

    for datum in ferientage:
        for i, row in data.iterrows():
            if row['Datum'] == datum:
                data.at[i, 'Ferientage'] = 1.0
                continue


    data.to_csv('../sourcedata/cleaned_data/5_has_wettercode.csv', sep=',', index=False)
    data_missing.to_csv('../sourcedata/cleaned_data/5_missing_wettercode.csv', sep=',', index=False)

if __name__ == '__main__':
    main()
