import math, os, pandas as pd, numpy as np, matplotlib.pyplot as plt
from graphviz import Digraph

'''Entropy(s) = - summation(p(log(p)))'''
'''Gain(s,a)  = Entropy(s) - summation(p(s/a)*Entropy(s/a))'''

dot = Digraph(comment = 'ID3 algo')
dot.format = 'png'

global_edges = []
special_edges = []

def plotTree(state, res):
    nodes = state.split()
    if not len(nodes):
        return
    nodes = [ nodes[i].split('=') for i in range(len(nodes)) if i%2]
    for i in range(len(nodes)-1):
        global_edges.append([nodes[i][0],nodes[i+1][0],nodes[i][1]])
    special_edges.append([nodes[-1][0],res,nodes[-1][1]])

def train(previous, attributes, dt, state):
    EntropyP = calc_entropy(previous)
    if not len(dt) or EntropyP == 0:
        if not previous[0]:
            print('AND'.join(state.split('AND')[:-1]), 'THEN play=no')
            plotTree(state,'no')
        else:
            print('AND'.join(state.split('AND')[:-1]), 'THEN play=yes')
            plotTree(state,'yes')
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

    global_edges = list(set([str(edge) for edge in global_edges]))

    for edge in global_edges:
        params = edge[1:-1].split(',')
        p = [p.strip()[1:-1] for p in params]
        dot.edge(p[0],p[1],label=p[2])

    unique_counter = 0
    for edge in special_edges:
        unique_counter += 1
        dot.node(str(unique_counter), edge[1])
        dot.edge(edge[0],str(unique_counter),label=edge[2])
    dot.render('id3-output.gv')
