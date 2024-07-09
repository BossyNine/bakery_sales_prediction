# Data Preparation

## General approach
**run**  
``` 
# ./run.sh
```
First, clean up the target directory and then run all scripts

1.  Merge data from the given files:
	- Kiwo.csv, Wetter.csv, and Umsatz.csv
	- Join to get all rows
	- Script `1_merge.py`
2. Data cleaning:
	- Remove all data without sales
	- Script `2_remove.py`
3. Fill gaps without information gain:
	- Zeroing all rows without *KiWo* data
	- Script `3_fill_kiwo.py`
4. Indentify missing data:
	- Split off rows that have no *Wettercode*
	- Script `4_split_missing.py`
5. Add *Ferientage* and *Feiertage*:
	- Add 1.0 for days when the data is in ferien.csv and/ or feiertag.csv
	- Script `5.1_add_FF_days.py`
6. Add weather data and break down the date:
	- *Wettercodes*:
		- Aggregate *Wettercodes* into *Wetterklassen* (logically chosen)  
		- Split off rows with classes having too few data points (threshold 1 %)
	- Add *Niederschlagsmenge* (external source)
	- Extract *Wochentag* and *Jahreszeit* from *Datum*
	- Add *Temperaturabweichung* (*positiv* and *negativ*) from *Durchschnitt der vorangegangenen Woche*
	- Notebook  `6_weather_parameters.ipynb `
7. Clean and encode dataset:
	- Delete unwanted columns  
	  Notebook  `7_data_transformation.ipynb `
	- One-Hot encoding for all categorical variables  
	  Notebook  `8_encoded_variables `
	- Split into training, validation (and test data)  
	  Notebook  `9_preparation_for_model.ipynb `
