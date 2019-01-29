import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt

""" code for plotting Anscombe's datasets"""

def draw_model(set):
    x = np.array(set['x'])
    y = np.array(set['y'])

    mx = np.mean(x)
    my = np.mean(y)

    n = np.size(x)
    xy = np.sum(x*y) - n*mx*my
    xx = np.sum(x*x) - n*mx*mx
    b1 = xy/xx
    b0 = my - b1*mx
    plt.plot(x,b0+b1*x)

def plot(sets):
    for set in sets:
        plt.plot(set['x'], set['y'], 'o')
        draw_model(set)
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
