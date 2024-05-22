# import ../sourcedata/feiertage_sh_2013-2018.csv and ../sourcedata/ferientage_sh_2013-2018.csv
# format colum to datetime

import pandas as pd
import os

def main():
    
    # load data
    path = os.path.join('..', 'sourcedata', 'feiertage_sh_2013-2018.csv')
    feiertage = pd.read_csv(path, sep=';')

    path = os.path.join('..', 'sourcedata', 'ferientage_sh_2013-2018.csv')
    ferientage = pd.read_csv(path, sep=';')

    # format column to format yyyy-mm-dd from dd.mm.yy 
    

    feiertage['Feiertage_SH'] = pd.to_datetime(feiertage['Feiertage_SH'], format='%d.%m.%y')
    ferientage['Ferientage'] = pd.to_datetime(ferientage['Ferientage'], format='%d.%m.%y')

    # save data
    path = os.path.join('..', 'sourcedata', 'cleaned_data', 'feiertage_sh_2013-2018.csv')
    feiertage.to_csv(path, index=False)

    path = os.path.join('..', 'sourcedata', 'cleaned_data', 'ferientage_sh_2013-2018.csv')
    ferientage.to_csv(path, index=False)

    #print first rows
    print(feiertage.head())
    print(ferientage.head())


if __name__ == '__main__':
    main()
