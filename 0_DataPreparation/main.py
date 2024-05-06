# import 3 csv files from ../sourcedata/ into pandas dataframes

import pandas as pd
import os


def main():
    # Set the path to the sourcedata directory
    sourcedata_dir = os.path.join(os.path.dirname(__file__), '..', 'sourcedata')

    # Read the csv files into pandas dataframes
    df1 = pd.read_csv(os.path.join(sourcedata_dir, 'wetter.csv'))
    df2 = pd.read_csv(os.path.join(sourcedata_dir, 'kiwo.csv'))
    df3 = pd.read_csv(os.path.join(sourcedata_dir, 'umsatzdaten.csv'))

    # join dataframes

    df = pd.merge(df1, df2, on='Datum')
    df = pd.merge(df, df3, on='Datum')

    # print the first 5 rows of the dataframe
    print(df.head())


if __name__ == '__main__':
    main()
