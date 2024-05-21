# import from ../sourcedata/cleaned_data/3_fill_kiwo.csv and make a new csv with only rows missing values in 'Wettercode'

import pandas as pd

def main():
    
    # Read the data
    data = pd.read_csv('../sourcedata/cleaned_data/3_fill_kiwo.csv')

    # Split the data
    missing = data[data['Wettercode'].isnull()]
    has_wettercode = data[data['Wettercode'].notnull()]

    # Save the data
    missing.to_csv('../sourcedata/cleaned_data/4_missing_wettercode.csv', index=False)
    has_wettercode.to_csv('../sourcedata/cleaned_data/4_has_wettercode.csv', index=False)

    #print the first 5 rows of the new csv
    print(missing.head())


if __name__ == '__main__':
    main()
