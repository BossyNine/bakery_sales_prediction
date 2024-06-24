# import packages
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.impute import KNNImputer

weather_code_descriptions = {
    0: "Bewoelkungsentwicklung nicht beobachtet",
    3: "Zunehmende Bewoelkung",
    5: "Trockener Dunst",
    10: "Feuchter Dunst",
    17: "Gewitter mit hoerbarem Donner, aber kein Niederschlag an der Station",
    20: "Spruehregen oder Schneegriesel hat aufgehoert",
    21: "Regen hat aufgehoert",
    22: "Schneefall hat aufgehoert",
    28: "Nebel hat sich aufgeloest",
    45: "Nebel, Himmel ist nicht erkennbar, Nebel unveraendert",
    49: "Nebel mit Reifbildung, Himmel ist nicht erkennbar",
    53: "Durchgehender maeßiger und nicht gefrierender Spruehregen",
    61: "Durchgehender leichter und nicht gefrierender Regen",
    63: "Durchgehender maeßiger nicht gefrierender Regen",
    65: "Durchgehender starker und nicht gefrierender Regen",
    68: "Leichter Schneeregen",
    69: "Maeßiger oder starker Schneeregen",
    71: "Durchgehender leichter Schneefall",
    73: "Durchgehender maeßiger Schneefall",
    75: "Durchgehender starker Schneefall",
    77: "Schneegrieseln mit oder ohne Nebel",
    79: "Eiskoerner (gefrorene Regentropfen)",
    95: "Leichtes oder maeßiges Gewitter mit Regen oder Schnee"
}
def get_weather_description(code):
    return weather_code_descriptions.get(code, "Description not available")

# new classes for weathercodes in a dictionary:
new_weather_code_descriptions = {
    0 : "nicht_beobachtet",
    1 : "Wolken",
    2 : "Dunst_oder_Nebel",
    3 : "sich_ankuendigender_Regen",
    4 : "Gewitter",
    5 : "Boeen_und_Sturm",
    6 : "Niederschlag_nass_leicht", # Regen # leicht # inkl. 'Niederschlag hat aufgehört', weil es ja nicht den ganzen Tag lang 'aufgehört' haben kann, sondern dann vermutlich vorher geregnet hat
    7 : "Niederschlag_nass_stark", # mäßiger oder starker Regen
    8 : "Niederschlag_trocken", # Schnee; leichtes oder mäßiges Schneetreiben
    9 : "Schneesturm_Hagel", # starkes Schneefegen
    10 : "Sandsturm"
}

# Define lists of codes for each weather class
nicht_beobachtet =  [0] # 0
Wolken = [1, 2, 3] # 1
Dunst_oder_Nebel = [4, 5, 6, 7, 8, 9, 10, 11, 12, 28, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49] # 2
sich_ankuendigender_Regen = [14, 15, 16] # 3
Gewitter = [13, 17, 29, 91, 92, 93, 94, 95, 96, 97, 98, 99] # 4
Boeen_und_Sturm = [18, 19] # 5
Niederschlag_nass_leicht = [20, 21, 23, 24, 25, 27, 50, 51, 56, 58, 60, 61, 66, 68, 80, 83, 87] # 6
Niederschlag_nass_stark = [52, 53, 54, 55, 57, 59, 62, 63, 64, 65, 67, 69, 81, 82, 84, 88] # 7
Niederschlag_trocken = [22, 26, 36, 38, 70, 71, 72, 73, 74, 75, 77, 78, 85, 86] # 8
Schneesturm_Hagel = [37, 39, 76, 79, 89, 90] # 9
Sandsturm = [30, 31, 32, 33, 34, 35] # 10


def wc(df):
    value_counts = df['Wettercode'].value_counts().sort_index()

    # Create a combined dictionary for mapping original codes to new numeric codes
    weather_code_mapping = {}

    # Combine the lists and dictionary
    weather_classes = {
    "nicht_beobachtet" : nicht_beobachtet,
    "Wolken" : Wolken,
    "Dunst_oder_Nebel" : Dunst_oder_Nebel,
    "sich_ankuendigender_Regen" : sich_ankuendigender_Regen,
    "Gewitter" : Gewitter,
    "Boeen_und_Sturm" : Boeen_und_Sturm,
    "Niederschlag_nass_leicht" : Niederschlag_nass_leicht,
    "Niederschlag_nass_stark" : Niederschlag_nass_stark,
    "Niederschlag_trocken" : Niederschlag_trocken,
    "Schneesturm_Hagel" : Schneesturm_Hagel,
    "Sandsturm" : Sandsturm
    }



    # Iterate over the new_weather_code_descriptions to build the mapping dictionary
    for new_code, description in new_weather_code_descriptions.items():
        if description in weather_classes:
            for code in weather_classes[description]:
                weather_code_mapping[code] = new_code

    df['Wetterklasse'] = df['Wettercode'].map(weather_code_mapping)

    # Find a frequency threshold for frequent classes (which ones to include?) to reduce noise (small object numbers per class might be too little to include into the model --> find threshold)

    return df

if __name__ == "__main__":
    df = pd.read_csv('data.csv')
    wc(df).to_csv('data1.csv', index=False)