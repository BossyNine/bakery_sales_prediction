import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import sys

def main(input_path, output_path, convert_bewoelkung, scale_data):
    # load data
    data = pd.read_csv(input_path)
    
    # drop columns
    data = data.drop(columns=['Umsatz'])

    # rename column
    data = data.rename(columns={'Umsatz.1': 'Umsatz'})

    # conver 'Bewoelkung' into numerical values
    if convert_bewoelkung:
        try:
            data = pd.get_dummies(data, columns=['Bewoelkung'], drop_first=True, dtype=float)

        except Exception as _:
            print('Could not convert Bewoelkung into numerical values')
            print('try first flage set to False')

    # scale data
    if scale_data:
        try: 
            scaler = MinMaxScaler()
            data[['Temperatur', 'Niederschlag', 'Windgeschwindigkeit']] = scaler.fit_transform(data[['Temperatur', 'Niederschlag', 'Windgeschwindigkeit']])

        except Exception as _:
            print('Could not scale data')
            print('try second flag set to False')

    # save data
    data.to_csv(output_path, index=False)

if __name__ == '__main__':
    if len(sys.argv) < 3 and len(sys.argv) > 5:
        print('Usage: python final_prep.py <input_path> <output_path> <convert_bewoelkung> <scale_data>')
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]
    convert_bewoelkung = sys.argv[3]
    scale_data = sys.argv[4]

    main(input_path, output_path, convert_bewoelkung, scale_data)
