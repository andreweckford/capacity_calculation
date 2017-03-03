# requires some editing prior to release
rm result-ChR2-1.csv 2>/dev/null
touch result-ChR2-1.csv
~/anaconda/bin/python3 capacity_calculation.py ChR2 0.02 20000.0 200 1 0.94 >> result-ChR2-1.csv
~/anaconda/bin/python3 capacity_calculation.py ChR2 0.1 20000.0 200 1 0.94 >> result-ChR2-1.csv
~/anaconda/bin/python3 capacity_calculation.py ChR2 0.02 20000.0 200 1 0.945 >> result-ChR2-1.csv
~/anaconda/bin/python3 capacity_calculation.py ChR2 0.1 20000.0 200 1 0.945 >> result-ChR2-1.csv
~/anaconda/bin/python3 capacity_calculation.py ChR2 0.02 20000.0 200 1 0.95 >> result-ChR2-1.csv
~/anaconda/bin/python3 capacity_calculation.py ChR2 0.1 20000.0 200 1 0.95 >> result-ChR2-1.csv
rm result-ChR2-2.csv 2>/dev/null
touch result-ChR2-2.csv
~/anaconda/bin/python3 capacity_calculation.py ChR2 0.02 20000.0 200 1 0.955 >> result-ChR2-2.csv
~/anaconda/bin/python3 capacity_calculation.py ChR2 0.1 20000.0 200 1 0.955 >> result-ChR2-2.csv
~/anaconda/bin/python3 capacity_calculation.py ChR2 0.02 20000.0 200 1 0.96 >> result-ChR2-2.csv
~/anaconda/bin/python3 capacity_calculation.py ChR2 0.1 20000.0 200 1 0.96 >> result-ChR2-2.csv
~/anaconda/bin/python3 capacity_calculation.py ChR2 0.02 20000.0 200 1 0.965 >> result-ChR2-2.csv
~/anaconda/bin/python3 capacity_calculation.py ChR2 0.1 20000.0 200 1 0.965 >> result-ChR2-2.csv
rm result-ChR2-3.csv 2>/dev/null
touch result-ChR2-3.csv
~/anaconda/bin/python3 capacity_calculation.py ChR2 0.02 20000.0 200 1 0.97 >> result-ChR2-3.csv
~/anaconda/bin/python3 capacity_calculation.py ChR2 0.1 20000.0 200 1 0.97 >> result-ChR2-3.csv
~/anaconda/bin/python3 capacity_calculation.py ChR2 0.02 20000.0 200 1 0.975 >> result-ChR2-3.csv
~/anaconda/bin/python3 capacity_calculation.py ChR2 0.1 20000.0 200 1 0.975 >> result-ChR2-3.csv
~/anaconda/bin/python3 capacity_calculation.py ChR2 0.02 20000.0 200 1 0.98 >> result-ChR2-3.csv
~/anaconda/bin/python3 capacity_calculation.py ChR2 0.1 20000.0 200 1 0.98 >> result-ChR2-3.csv
rm result-ChR2-4.csv 2>/dev/null
touch result-ChR2-4.csv
~/anaconda/bin/python3 capacity_calculation.py ChR2 0.02 20000.0 200 1 0.985 >> result-ChR2-4.csv
~/anaconda/bin/python3 capacity_calculation.py ChR2 0.1 20000.0 200 1 0.985 >> result-ChR2-4.csv
~/anaconda/bin/python3 capacity_calculation.py ChR2 0.02 20000.0 200 1 0.99 >> result-ChR2-4.csv
~/anaconda/bin/python3 capacity_calculation.py ChR2 0.1 20000.0 200 1 0.99 >> result-ChR2-4.csv
~/anaconda/bin/python3 capacity_calculation.py ChR2 0.02 20000.0 200 1 0.995 >> result-ChR2-4.csv
~/anaconda/bin/python3 capacity_calculation.py ChR2 0.1 20000.0 200 1 0.995 >> result-ChR2-4.csv

rm result.csv 2>/dev/null
cat result-ChR2-1.csv result-ChR2-2.csv result-ChR2-3.csv result-ChR2-4.csv > result.csv

~/anaconda/bin/python3 GapComparisonFigure.py
