rm result-CaM-1.csv 2>/dev/null
touch result-CaM-1.csv
~/anaconda3/bin/python3 capacity_calculation.py CaM 0.002 10000.0 200 1 0.1 >> result-CaM-1.csv
~/anaconda3/bin/python3 capacity_calculation.py CaM 0.002 10000.0 200 1 0.2 >> result-CaM-1.csv
~/anaconda3/bin/python3 capacity_calculation.py CaM 0.002 10000.0 200 1 0.3 >> result-CaM-1.csv
~/anaconda3/bin/python3 capacity_calculation.py CaM 0.002 10000.0 200 1 0.4 >> result-CaM-1.csv
~/anaconda3/bin/python3 capacity_calculation.py CaM 0.002 10000.0 200 1 0.5 >> result-CaM-1.csv
rm result-CaM-2.csv 2>/dev/null
touch result-CaM-2.csv
~/anaconda3/bin/python3 capacity_calculation.py CaM 0.002 10000.0 200 1 0.6 >> result-CaM-2.csv
~/anaconda3/bin/python3 capacity_calculation.py CaM 0.002 10000.0 200 1 0.7 >> result-CaM-2.csv
~/anaconda3/bin/python3 capacity_calculation.py CaM 0.002 10000.0 200 1 0.8 >> result-CaM-2.csv
~/anaconda3/bin/python3 capacity_calculation.py CaM 0.002 10000.0 200 1 0.9 >> result-CaM-2.csv
rm result-CaM-3.csv 2>/dev/null
touch result-CaM-3.csv
~/anaconda3/bin/python3 capacity_calculation.py CaM 0.002 10000.0 200 1 0.42 >> result-CaM-3.csv
~/anaconda3/bin/python3 capacity_calculation.py CaM 0.002 10000.0 200 1 0.44 >> result-CaM-3.csv
~/anaconda3/bin/python3 capacity_calculation.py CaM 0.002 10000.0 200 1 0.46 >> result-CaM-3.csv
~/anaconda3/bin/python3 capacity_calculation.py CaM 0.002 10000.0 200 1 0.48 >> result-CaM-3.csv
~/anaconda3/bin/python3 capacity_calculation.py CaM 0.002 10000.0 200 1 0.52 >> result-CaM-3.csv
rm result-CaM-4.csv 2>/dev/null
touch result-CaM-4.csv
~/anaconda3/bin/python3 capacity_calculation.py CaM 0.002 10000.0 200 1 0.54 >> result-CaM-4.csv
~/anaconda3/bin/python3 capacity_calculation.py CaM 0.002 10000.0 200 1 0.56 >> result-CaM-4.csv
~/anaconda3/bin/python3 capacity_calculation.py CaM 0.002 10000.0 200 1 0.58 >> result-CaM-4.csv
~/anaconda3/bin/python3 capacity_calculation.py CaM 0.002 10000.0 200 1 0.62 >> result-CaM-4.csv
~/anaconda3/bin/python3 capacity_calculation.py CaM 0.002 10000.0 200 1 0.64 >> result-CaM-4.csv
rm result-CaM-5.csv 2>/dev/null
touch result-CaM-5.csv
~/anaconda3/bin/python3 capacity_calculation.py CaM 0.002 10000.0 200 1 0.32 >> result-CaM-5.csv
~/anaconda3/bin/python3 capacity_calculation.py CaM 0.002 10000.0 200 1 0.34 >> result-CaM-5.csv
~/anaconda3/bin/python3 capacity_calculation.py CaM 0.002 10000.0 200 1 0.36 >> result-CaM-5.csv
rm result-CaM-6.csv 2>/dev/null
touch result-CaM-6.csv
~/anaconda3/bin/python3 capacity_calculation.py CaM 0.002 10000.0 200 1 0.38 >> result-CaM-6.csv
~/anaconda3/bin/python3 capacity_calculation.py CaM 0.002 10000.0 200 1 0.66 >> result-CaM-6.csv
~/anaconda3/bin/python3 capacity_calculation.py CaM 0.002 10000.0 200 1 0.68 >> result-CaM-6.csv

rm result-CaM.csv 2>/dev/null
cat result-CaM-1.csv result-CaM-2.csv result-CaM-3.csv result-CaM-4.csv result-CaM-5.csv result-CaM-6.csv > result-CaM.csv

~/anaconda/bin/python3 CaMFigure.py
