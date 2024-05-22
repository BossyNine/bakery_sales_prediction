import pandas as pd

def main():
    # Read in the data
    data = pd.read_csv('../sourcedata/cleaned_data/4_has_wettercode.csv', sep=',')
    data_missing = pd.read_csv('../sourcedata/cleaned_data/4_missing_wettercode.csv', sep=',')
    feiertage = pd.read_csv('../sourcedata/cleaned_data/feiertage_sh_2013-2018.csv')
    ferientage = pd.read_csv('../sourcedata/cleaned_data/ferientage_sh_2013-2018.csv')

    # Add the columns
    data['Feiertage'] = 0.0
    data['Ferientage'] = 0.0
    data_missing['Feiertage'] = 0.0
    data_missing['Ferientage'] = 0.0

    # Convert 'Datum' columns to datetime
    data['Datum'] = pd.to_datetime(data['Datum'], format='%Y-%m-%d')
    data_missing['Datum'] = pd.to_datetime(data_missing['Datum'], format='%Y-%m-%d')
    feiertage_dates = pd.to_datetime(feiertage['Feiertage_SH'], format='%Y-%m-%d').values
    ferientage_dates = pd.to_datetime(ferientage['Ferientage'], format='%Y-%m-%d').values

    # Update 'Feiertage' column
    data.loc[data['Datum'].isin(feiertage_dates), 'Feiertage'] = 1.0
    data_missing.loc[data_missing['Datum'].isin(feiertage_dates), 'Feiertage'] = 1.0

    # Update 'Ferientage' column
    data.loc[data['Datum'].isin(ferientage_dates), 'Ferientage'] = 1.0
    data_missing.loc[data_missing['Datum'].isin(ferientage_dates), 'Ferientage'] = 1.0

    # Debugging: Check if updates were made
    print(f"Data with Feiertage set to 1.0:\n{data[data['Feiertage'] == 1.0]}")
    print(f"Data with Ferientage set to 1.0:\n{data[data['Ferientage'] == 1.0]}")

    # Save the updated data to new CSV files
    data.to_csv('../sourcedata/cleaned_data/5_has_wettercode.csv', sep=',', index=False)
    data_missing.to_csv('../sourcedata/cleaned_data/5_missing_wettercode.csv', sep=',', index=False)

if __name__ == '__main__':
    main()

