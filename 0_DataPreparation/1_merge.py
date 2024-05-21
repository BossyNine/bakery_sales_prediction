# import 3 csv files from ../sourcedata/ into pandas dataframes

import pandas as pd
import os
import numpy as np

def main():
    # Set the path to the sourcedata directory
    sourcedata_dir = os.path.join(os.path.dirname(__file__), '..', 'sourcedata')

    # Read the csv files into pandas dataframes
    df1 = pd.read_csv(os.path.join(sourcedata_dir, 'wetter.csv'))
    df2 = pd.read_csv(os.path.join(sourcedata_dir, 'kiwo.csv'))
    df3 = pd.read_csv(os.path.join(sourcedata_dir, 'umsatzdaten.csv'))

    # merge all 3 dfs into one keep all entries from all 3 dfs
    df = pd.merge(df1, df2, how='outer', on='Datum')
    df = pd.merge(df, df3, how='outer', on='Datum')

    # save the merged dataframe to a csv file in ../sourcedata/cleaned_data/
    df.to_csv(os.path.join(sourcedata_dir, 'cleaned_data', '1_merged_data.csv'), index=False)

    # print the first 5 rows of the merged dataframe
    print(df.head())

if __name__ == '__main__':
    main()
