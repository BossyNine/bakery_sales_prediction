## Script to Create New Features Based on Weather Data (Pauline)

Additionally, precipitation data is used from the weather station in Kiel Holtenau. Delete this folder as soon as the script is incorporated into the other folders! (I just don't want to break anything in the other sections, and I'm still figuring things out!)

## Edit (Jonna): 
### Ultra cool ideas and approaches for the various variables! Notes on what should be adopted or adjusted:

- Brilliant use of precipitation data! Perhaps combine it with the weather codes? (i.e., interpreting what the codes mean? And: could the precipitation data replace the weather codes if they are missing, but all other data is available?)
- The encoding of dates into weekdays is fantastic! (Make sure the date column is in datetime format beforehand)
- The idea of using averages over several days is excellent for filling gaps.
- It is also great for filtering out particularly cold or warm days. A 7-day average might be good, but perhaps a longer period, like 4 weeks, could be better? Or how much the temperature deviates from the monthly or even seasonal average? Seasons are definitely a good criterion.

### Next Steps:
1. Research if the weather codes correspond to a specific amount of precipitation.
2. Think of and experiment with categories to classify the weather codes.
3. Then calculate the regression line and experiment with categories. Also, represent the relationship between the categories/variables? And determine the importance of each variable.
