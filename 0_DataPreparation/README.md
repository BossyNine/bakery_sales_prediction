# Data Preparation

## Vorgehen
**run**  
``` 
# ./run.sh
```
Räumt zuerst die Target-Dir auf und lässt danach alle Skripts laufen.

1.  Merge der Daten aus den vorgebenden Dateien
	- Kiwo.csv, Wetter.csv und Umsatz.csv
	- Join um alle Rows zu erhalten
	- Skript `1_merge.py`
2. Bereinigung der Daten
	- Entfernen aller Daten ohne Umsatz
	- Skript `2_remove.py`
3. Leerstellen füllen ohne Informationsgewinn
	- zeroing aller Rows ohne KiWo Daten
	- Skript `3_fill_kiwo.py`
4. Finden der Daten die fehlen
	- split-off der Rows, die keinen Wettercode haben
	- Skript `4_split_missing.py`
5. Hinzufügen der Ferien- und Feiertage
	- add 1.0 für Tage wenn Datum in ferien.csv und feiertag.csv
	- Skript `5.1_add_FF_days.py`
6. Hinzufügen von Wetterdaten und aufschlüsseln des Datums
	- Wettercodes: 	- Wettercodes in Wetterklassen aggregieren (selbst logisch gewählt)
					- split-off der rows mit Klassen mit zu wenig Datenpunkten (threshold 1%)
	- add Niederschlagsmenge (external source)
	- extract Wochentag und Jahreszeit aus Datum
	- add Temperaturabweichung (positiv und negativ) vom Durchschnitt der vorangegangenen Woche
	- Notebook  `6_weather_parameters.ipynb `

7. Datensatz aufräumen und codieren
	- delete unwanted columns
	  Notebook  `7_data_transformation.ipynb `
	- One-Hot encoding für alle kategoriellen Variablen
	  Notebook  `8_encoded_variables `
	- Split in Training, Validierung (und Testdaten)
	  Notebook  `9_preparation_for_model.ipynb `



**was bisher zu kurz kommt: handling missing values! und data cleaning**