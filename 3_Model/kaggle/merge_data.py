# merge wetter.csv, train.csv, kiwo.csv over 'Datum' keep all rows

import pandas as pd
from lib.weather_class import wc
from lib.tem_deriv import tempd
from lib.date_var import date_var
from lib.encode_variable import encode_id, encode_rev
import os
import shutil
from zipfile import ZipFile

# Download Dataset from Kaggle
os.system("kaggle competitions download -c bakery-sales-prediction-summer-24")

# unzip the dataset
with ZipFile("bakery-sales-prediction-summer-24.zip", 'r') as zipObj:
    zipObj.extractall()


eid = True
erev = True

# read data
wetter = pd.read_csv('wetter.csv', sep=',')
train = pd.read_csv('train.csv', sep=',')
kiwo = pd.read_csv('kiwo.csv', sep=',')
test  = pd.read_csv('test.csv', sep=',')

data = pd.concat([train, test], ignore_index=True)

# merge data
data = pd.merge(wetter, data, on='Datum', how='outer')
data = pd.merge(data, kiwo, on='Datum', how='outer')

 # fill in missing values for the columns 'KielerWoche' with 0.0
data['KielerWoche'] = data['KielerWoche'].fillna(0.0)

# add empty columns  'Ferientage' and 'Feiertage' to data
data['Ferientage'] = 0.0
data['Feiertage'] = 0.0

feiertage = pd.read_csv('./data/feiertage_sh_2013-2019.csv')
ferientage = pd.read_csv('./data/ferientage_sh_2013-2019.csv')

data.loc[data['Datum'].isin(feiertage['Feiertage_SH']), 'Feiertage'] = 1.0
data.loc[data['Datum'].isin(ferientage['Ferientage']), 'Ferientage'] = 1.0

# remove rows with 'Datum' < 2013-06-30
data = data[data['Datum'] > '2013-06-30'] 
data = wc(data)

data = tempd(data)

data = date_var(data)

prec = pd.read_csv('./data/wetter_kiel.csv', sep=',', na_values='-999', parse_dates=['MESS_DATUM'])
prec["MESS_DATUM"] = pd.to_datetime(prec["MESS_DATUM"])
prec.rename(columns={'MESS_DATUM': 'Datum', ' RSK': 'Niederschlag'}, inplace=True)
prec = prec[['Datum', 'Niederschlag']]
data = pd.merge(data, prec, on='Datum', how='left')

columns_to_drop = ['week', 'season_str', 'temp_7d_avg', 'warmer_than_week_before', 'colder_than_week_before']

data = data.drop(columns=columns_to_drop)

print(data.shape)

data = data.dropna()

print(data.shape)
if eid:
    data_id = encode_id(data)
    # save data
    data_id.to_csv('encoded_id.csv', index=False)
if erev:
    data = encode_rev(data)
    # drop rows with 'Umsatz' == 0
    data = data[data['Umsatz'] != 0]
    # save data
    data.to_csv('encoded_rev.csv', index=False)

if os.path.exists('./test.csv'):
    os.remove('./test.csv')
if os.path.exists('./train.csv'):
    os.remove('./train.csv')
if os.path.exists('./wetter.csv'):
    os.remove('./wetter.csv')
if os.path.exists('./bakery-sales-prediction-summer-24.zip'):
    os.remove('./bakery-sales-prediction-summer-24.zip')
if os.path.exists('./kiwo.csv'):
    os.remove('./kiwo.csv')
shutil.move('encoded_id.csv', '../encoded_id.csv')
shutil.move('encoded_rev.csv', '../encoded_rev.csv')
shutil.move('sample_submission.csv', '../sample_submission.csv')


print('Data merged and saved as data.csv')

