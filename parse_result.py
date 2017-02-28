import numpy as np
import csv

def parse_result(fname):
  csvf = open(fname,'r')
  r = csv.reader(csvf)
  t = []
  for s in r:
    t = t + [[float(i) for i in s]]

  csvf.close()
  return np.array(t)
