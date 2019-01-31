import pandas as pd
import numpy as np

def find_s(classData):
    H = ['N'] * 17

    for index in classData.index:
        data = classData.loc[index]
        for colNum in range(0, len(classData.columns) - 1):
            if H[colNum] == 'N':
                H[colNum] = data[classData.columns[colNum]]
            elif H[colNum] == '?':
                pass
            elif H[colNum] != data[classData.columns[colNum]]:
                H[colNum] = '?'
    return H

def main():
    zooData = pd.read_csv('zoo_data.csv', header=None)
    zooData.columns = ['name', 'hair', 'feathers', 'eggs', 'milk', 'airborne', 'aquatic', 'predator', 'toothed', 'backbone', 'breathes', 'venomous', 'fins', 'legs', 'tails', 'domestic', 'catsize', 'type']

    classifiedSet = []

    for i in range(1,8):
        classData = zooData[zooData['type']==i]
        H = find_s(classData)
        classifiedSet.append(H)

    classifiedData = {}

    for colNum in range(0, len(zooData.columns) - 1):
        classifiedData[zooData.columns[colNum]] = [h[colNum] for h in classifiedSet]

    classifiedData = pd.DataFrame(classifiedData, index=['mammal', 'fish', 'reptile', 'fish', 'amphibians', 'insect', 'other'])
    classifiedData = classifiedData[['name', 'hair', 'feathers', 'eggs', 'milk', 'airborne', 'aquatic', 'predator', 'toothed', 'backbone', 'breathes', 'venomous', 'fins', 'legs', 'tails', 'domestic', 'catsize']]

    classifiedData.to_csv('classifiedData.csv')


if __name__ == '__main__':
    main()
