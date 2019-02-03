import pandas as pd
import numpy as np


def acceptingIt(g,trainingSet):
    result = True
    for i in range(len(g)):
        if g[i] != '?' and g[i] != trainingSet[i]:
            result = False
            break
    return result

def hypothesis_print(i, g, s, type, t):
    print('T'+str(i)+' = ',t, type)
    print('G'+str(i)+' = ',g)
    print('S'+str(i)+' = ',s)
    print('\n')

def generateS(trainingSet,s):
    for i in range(0,len(s)):
        if s[i] == 'phi':
            s[i] = trainingSet[i]
        elif s[i] != trainingSet[i]:
            s[i] = '?'
    return s

def minAttr(elem):
    count = 0
    for e in elem:
        if e != '?':
            count +=1
    # print('sort', elem, count)
    return count

def removeDuplicates(gSet):
    if not len(gSet):
        return gSet

    positionsUsed = [0] * len(gSet[0])
    new_g = []
    gSet.sort(key = minAttr)
    for g in gSet:
        accept = True
        for pos in range(len(g)):
            if g[pos]!='?' and positionsUsed[pos]==1:
                accept = False
                break
        if accept:
            new_g.append(g)
            for pos in range(len(g)):
                if g[pos] != '?':
                    positionsUsed[pos] = 1
    return new_g

def generateG(s, gSet, trainingSet):
    new_g = []
    for g in gSet:
        if not acceptingIt(g, trainingSet):
            new_g.append(g)
        else:
            for i in range(len(g)):
                if g[i] == '?' and s[i] != trainingSet[i] and s[i] != '?':
                    tg = [elem for elem in g]
                    tg[i] = s[i]
                    new_g.append(tg)
    new_g = removeDuplicates(new_g)
    return new_g

def compare(g,s):
    result = True
    for i in range(0,len(g)):
        if g[i] != '?' and g[i] != s[i]:
            result = False
            break
    return result

def run_iterations(data, g, s):
    hypothesis_print(0,g,s,'none','none')
    for iterationCount in range(0,len(data)):
        trainingSet = data[iterationCount]
        if trainingSet[-1]=='Yes':
            '''Positive training set'''
            trainingSet=trainingSet[:-1]
            s = generateS(trainingSet,s)
            new_g = []
            for i in range(0,len(g)):
                result = compare(g[i],s)
                if result:
                    new_g.append(g[i])
            g = new_g
            hypothesis_print(iterationCount+1, g, s, 'Positive', trainingSet)
        else:
            '''Negative training set'''
            trainingSet = trainingSet[:-1]
            g = generateG(s,g,trainingSet)
            hypothesis_print(iterationCount+1, g, s, 'Negative', trainingSet)

def main():
    data = np.array(pd.read_csv('data2.csv', header=None))

    print(data, '\n')
    g = ['?'] * (len(data[0,:])-1)
    s = ['phi'] * (len(data[0,:])-1)
    run_iterations(data, [g], s)

if __name__ == '__main__':
    main()
