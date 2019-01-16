import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt

""" code for plotting Anscombe's datasets"""

def main():
    with open('anscombes dataset.csv') as csv_file:
        csv_reader = csv.read(csv_file, delimiter = ',')
        print(csv_reader)    

if __name__ == 'main':
    main()
