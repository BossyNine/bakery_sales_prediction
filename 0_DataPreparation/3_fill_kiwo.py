# import ../sourcedata/cleaned_data/2_merged_data_cleaned.csv and fill in missing values for the columns 'KielerWoche' with 0.0

import pandas as pd

def main():
    
    # read in the data
    data = pd.read_csv('../sourcedata/cleaned_data/2_merged_data_cleaned.csv')

    # fill in missing values for the columns 'KielerWoche' with 0.0
    data['KielerWoche'] = data['KielerWoche'].fillna(0.0)

    # write the data to a new csv file
    data.to_csv('../sourcedata/cleaned_data/3_fill_kiwo.csv', index=False)

    # print the first 5 rows of the data
    print(data.head())

if __name__ == '__main__':
    main()
