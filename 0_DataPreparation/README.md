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