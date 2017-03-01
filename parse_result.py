import numpy as np
import csv

# Parses CSV-formatted results into numpy arrays

def parse_result(fname):
  csvf = open(fname,'r')
  r = csv.reader(csvf)
  t = []
  for s in r:
    t = t + [[float(i) for i in s]]

  csvf.close()
  return np.array(t)
