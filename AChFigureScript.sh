rm result-ACh-1.csv 2>/dev/null
touch result-ACh-1.csv
~/anaconda/bin/python3 capacity_calculation.py ACh 0.02 20000.0 500 1 0.65 >> result-ACh-1.csv
~/anaconda/bin/python3 capacity_calculation.py ACh 0.02 20000.0 500 1 0.66 >> result-ACh-1.csv
~/anaconda/bin/python3 capacity_calculation.py ACh 0.02 20000.0 500 1 0.67 >> result-ACh-1.csv
~/anaconda/bin/python3 capacity_calculation.py ACh 0.02 20000.0 500 1 0.68 >> result-ACh-1.csv
~/anaconda/bin/python3 capacity_calculation.py ACh 0.02 20000.0 500 1 0.69 >> result-ACh-1.csv
~/anaconda/bin/python3 capacity_calculation.py ACh 0.02 20000.0 500 1 0.7 >> result-ACh-1.csv
~/anaconda/bin/python3 capacity_calculation.py ACh 0.02 20000.0 500 1 0.71 >> result-ACh-1.csv
~/anaconda/bin/python3 capacity_calculation.py ACh 0.02 20000.0 500 1 0.72 >> result-ACh-1.csv
~/anaconda/bin/python3 capacity_calculation.py ACh 0.02 20000.0 500 1 0.73 >> result-ACh-1.csv
rm result-ACh-2.csv 2>/dev/null
touch result-ACh-2.csv
~/anaconda/bin/python3 capacity_calculation.py ACh 0.02 20000.0 500 1 0.74 >> result-ACh-2.csv
~/anaconda/bin/python3 capacity_calculation.py ACh 0.02 20000.0 500 1 0.75 >> result-ACh-2.csv
~/anaconda/bin/python3 capacity_calculation.py ACh 0.02 20000.0 500 1 0.76 >> result-ACh-2.csv
~/anaconda/bin/python3 capacity_calculation.py ACh 0.02 20000.0 500 1 0.77 >> result-ACh-2.csv
~/anaconda/bin/python3 capacity_calculation.py ACh 0.02 20000.0 500 1 0.78 >> result-ACh-2.csv
~/anaconda/bin/python3 capacity_calculation.py ACh 0.02 20000.0 500 1 0.79 >> result-ACh-2.csv
~/anaconda/bin/python3 capacity_calculation.py ACh 0.02 20000.0 500 1 0.8 >> result-ACh-2.csv
~/anaconda/bin/python3 capacity_calculation.py ACh 0.02 20000.0 500 1 0.81 >> result-ACh-2.csv
~/anaconda/bin/python3 capacity_calculation.py ACh 0.02 20000.0 500 1 0.82 >> result-ACh-2.csv
rm result-ACh-3.csv 2>/dev/null
touch result-ACh-3.csv
~/anaconda/bin/python3 capacity_calculation.py ACh 0.02 20000.0 500 1 0.83 >> result-ACh-3.csv
~/anaconda/bin/python3 capacity_calculation.py ACh 0.02 20000.0 500 1 0.84 >> result-ACh-3.csv
~/anaconda/bin/python3 capacity_calculation.py ACh 0.02 20000.0 500 1 0.85 >> result-ACh-3.csv
~/anaconda/bin/python3 capacity_calculation.py ACh 0.02 20000.0 500 1 0.86 >> result-ACh-3.csv
~/anaconda/bin/python3 capacity_calculation.py ACh 0.02 20000.0 500 1 0.87 >> result-ACh-3.csv
~/anaconda/bin/python3 capacity_calculation.py ACh 0.02 20000.0 500 1 0.88 >> result-ACh-3.csv
~/anaconda/bin/python3 capacity_calculation.py ACh 0.02 20000.0 500 1 0.89 >> result-ACh-3.csv
~/anaconda/bin/python3 capacity_calculation.py ACh 0.02 20000.0 500 1 0.9 >> result-ACh-3.csv
~/anaconda/bin/python3 capacity_calculation.py ACh 0.02 20000.0 500 1 0.91 >> result-ACh-3.csv
rm result-ACh-4.csv 2>/dev/null
touch result-ACh-4.csv
~/anaconda/bin/python3 capacity_calculation.py ACh 0.02 20000.0 500 1 0.92 >> result-ACh-4.csv
~/anaconda/bin/python3 capacity_calculation.py ACh 0.02 20000.0 500 1 0.93 >> result-ACh-4.csv
~/anaconda/bin/python3 capacity_calculation.py ACh 0.02 20000.0 500 1 0.94 >> result-ACh-4.csv
~/anaconda/bin/python3 capacity_calculation.py ACh 0.02 20000.0 500 1 0.95 >> result-ACh-4.csv
~/anaconda/bin/python3 capacity_calculation.py ACh 0.02 20000.0 500 1 0.96 >> result-ACh-4.csv
~/anaconda/bin/python3 capacity_calculation.py ACh 0.02 20000.0 500 1 0.97 >> result-ACh-4.csv
~/anaconda/bin/python3 capacity_calculation.py ACh 0.02 20000.0 500 1 0.98 >> result-ACh-4.csv
~/anaconda/bin/python3 capacity_calculation.py ACh 0.02 20000.0 500 1 0.99 >> result-ACh-4.csv

rm result.csv 2>/dev/null
cat result-ACh-1.csv result-ACh-2.csv result-ACh-3.csv result-ACh-4.csv > result-ACh.csv
~/anaconda/bin/python3 AChFigure.py
