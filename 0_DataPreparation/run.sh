#!/bin/sh
# run the python scripts in ./
pushd ../sourcedata/cleaned_data/
echo 'Removing Data'
rm -r * 
echo 'Returning'
popd

echo 'Merge Data'
python3 ./1_merge.py
echo 'Removing Rows'
sleep 1
python3 ./2_remove.py
echo 'Filling KiWo Data'
sleep 1
python3 ./3_fill_kiwo.py
echo 'Splitting Data'
sleep 1
python3 ./4_split_missing.py
