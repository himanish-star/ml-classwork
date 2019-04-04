import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

'''linear points'''

points = [
        [1.8145161290322562, 60],
        [47.58064516129032, 60],
        [96.16935483870968, 60],
        [50.0, 60],
        [94.35483870967741, 60],
        [52.41935483870968, 60],
        [92.13709677419355, 60],
        [54.03225806451613, 60],
        [90.52419354838709, 60],
        [56.653225806451616, 60],
        [89.11290322580645, 60],
        [58.87096774193549, 60],
        [86.89516129032258, 60],
        [60.88709677419355, 60],
        [84.4758064516129, 60],
        [63.30645161290323, 60],
        [82.25806451612902, 60],
        [64.51612903225806, 60],
        [81.04838709677419, 60],
        [66.73387096774194, 60],
        [79.23387096774194, 60],
        [69.55645161290322, 60],
        [76.81451612903226, 60],
        [72.78225806451613, 60],
        [75.20161290322581, 60],
        [45.564516129032256, 60],
        [4.43548387096774, 60],
        [43.346774193548384, 60],
        [6.854838709677416, 60],
        [40.927419354838705, 60],
        [8.669354838709676, 60],
        [38.70967741935483, 60],
        [12.5, 60],
        [35.483870967741936, 60],
        [17.741935483870964, 60],
        [33.46774193548387, 60],
        [21.9758064516129, 60],
        [31.85483870967742, 60],
        [25.403225806451612, 60],
        [29.83870967741935, 60],
        [27.21774193548387, 60]
    ]


types = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

def transform():
    global points, types
    tp = np.array(points)
    tt = np.array(types)
    centerX = [sum(tp[:,0])/len(tp)] * len(tp)
    centerY = [sum(tp[:,1])/len(tp)] * len(tp)
    zc = (tp[:,0]-centerX)**2 + (tp[:,1]-centerY)**2

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for i in range(len(tp)):
        if int(tt[i]) is 0:
            ax.plot([tp[i,0]],[tp[i,1]],[zc[i]],c='r',marker='o')
        else:
            ax.plot([tp[i,0]],[tp[i,1]],[zc[i]],c='g',marker='x')
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    plt.show()


if __name__ == "__main__":
    global points, types
    tp = np.array(points)
    tt = np.array(types)
    for i in range(len(tp)):
        if int(tt[i]) is 0:
            plt.plot([tp[i,0]],[tp[i,1]],c='r',marker='o')
        else:
            plt.plot([tp[i,0]],[tp[i,1]],c='g',marker='x')
    plt.show()
    transform()