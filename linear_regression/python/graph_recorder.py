import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt

""" code for plotting Anscombe's datasets"""

def plot(sets):
    for set in sets:
        plt.plot(set['x'], set['y'], 'o')
        plt.show()


def main():
    dataset = pd.read_csv('anscombes dataset.csv')
    datasets = []
    for c in range(0,len(dataset.columns),2):
        datasets.append(dataset[[dataset.columns[c], dataset.columns[c+1]]])
        datasets[c//2].columns=['x','y']
    plot(datasets)

if __name__ == '__main__':
    main()
