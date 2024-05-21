# import ../sourcedata/merged_data.csv, remove lines with missing data in 'Umsatz' column and save
# the cleaned data to ../sourcedata/cleaned_data/1_merged_data_cleaned.csv

import pandas as pd
def main():
    
    # Load data
    data = pd.read_csv('../sourcedata/cleaned_data/1_merged_data.csv')

    # Remove lines with missing data in 'Umsatz' column
    data = data.dropna(subset=['Umsatz'])

    # Save cleaned data
    data.to_csv('../sourcedata/cleaned_data/2_merged_data_cleaned.csv', index=False)

    # show first 5 lines of cleaned data
    print(pd.read_csv('../sourcedata/cleaned_data/2_merged_data_cleaned.csv').head())

if __name__ == '__main__':
    main()  
