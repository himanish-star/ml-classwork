import math, os, pandas as pd, numpy as np, matplotlib.pyplot as plt

'''Entropy(s) = - summation(p(log(p)))'''
'''Gain(s,a)  = Entropy(s) - summation(p(s/a)*Entropy(s/a))'''

def train(previous, attributes, dt, state):
    EntropyP = calc_entropy(previous)
    if not len(dt) or EntropyP == 0:
        if not previous[0]:
            print('AND'.join(state.split('AND')[:-1]), 'THEN play=no')
        else:
            print('AND'.join(state.split('AND')[:-1]), 'THEN play=yes')
        return
    Gains = []
    total = sum(previous)
    for attribute in attributes:
        vals = []
        for val in dataset[attribute].unique():
            posInst = len(dt.loc[(dt[attribute]==val) & (dt['play']=='yes')])
            negInst = len(dt.loc[(dt[attribute]==val) & (dt['play']=='no')])
            vals.append([posInst+negInst,[posInst,negInst]])
        Gains.append([attribute, EntropyP - sum([(c/total)*calc_entropy(insData) for c,insData in vals])])
    Gains = np.array(Gains)
    maxGain = max(Gains[:,1])
    selected_attributes = [sattr for sattr,gain in Gains if gain == maxGain]
    for sattr in selected_attributes:
        for val in dataset[sattr].unique():
            posInst = len(dt.loc[(dt[sattr]==val) & (dt['play']=='yes')])
            negInst = len(dt.loc[(dt[sattr]==val) & (dt['play']=='no')])
            new_dt = dt[dt[sattr]==val].drop(labels=[sattr],axis=1)
            train([posInst, negInst],(new_dt.columns[:-1]),new_dt, state + sattr + '=' + str(val) + ' AND ')

def calc_entropy(data):
    # print(data)
    total = sum(data)
    return -sum([(val/total) * math.log(val/total, 2) for val in data if val])

def calc_gain():
    pass

if __name__ == '__main__':
    dataset = pd.read_csv('play_tennis.csv')
    attributes = np.array(dataset.columns)[:-1]
    systemPos = len(dataset[dataset['play']=='yes'])
    systemNeg = len(dataset[dataset['play']=='no'])
    train([systemPos, systemNeg], attributes, dataset, 'IF ')
