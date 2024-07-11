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

Now, the code is in jupyter notebooks and they need to be run individually:

6.1 Add weather data:
	- Merge data from 5 and 5.1 again (to not loose missing values)
	- Add precipitation column
	- Notebook `6.1_weather_parameters.ipynb`

6.2 Missing value imputation:
	- Investigation of data to find missing values
	- Start with variable with least missing values
	- Impute cloudiness with 'mode' method
	- Impute temperature, windspeed, and precipitation with 'linear interpolation'
	- Find dependent variables for weathercode
	- Impute weathercode with KNN-method
	- Check for plausability
	- Notebook `6.2_missing_value_imputation.ipynb`

6.3 Combine weathercode into weatherclass:
	- Create new weather classes from the codes that summerize
	- Notebook `6.3_weather_class.ipynb`
	- (this step was excluded lateron)

6.4 Add variable temperature deviation:
	- Create rolling average over seven days
	- Calculate deviation of one day of the week's average before (positives, negatives, and absolute)
	- Create different new variable
	- Notebook `6.4_temperature_deviation.ipynb`

6.5 Add date-related variables:
	- Extract weekday, day of the month, month, and season from the date column
	- Notebook `6.5_date_variables.ipynb`

7. Data transformation:
	- Delete unwanted columns 
	- Notebook `7_data_transformation.ipynb`

8. Encoding of the variables:
	- One-Hot encoding for all categorical variables
	- Notebook `8_encoded_variables.ipynb`

9. Data preparation for the model:
	- Split into training, validation (and test data) 
	- Notebook `9_preparation_for_model.ipynb`
