import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

'''circular points'''

points = [
        [27.01612903225806, 75.00000000000001],
        [32.45967741935483, 69.04761904761905],
        [26.00806451612903, 69.04761904761905],
        [31.85483870967742, 64.44805194805195],
        [25.80645161290322, 62.012987012987026],
        [32.05645161290322, 59.30735930735932],
        [27.01612903225806, 55.519480519480524],
        [32.66129032258064, 55.519480519480524],
        [29.43548387096774, 49.02597402597404],
        [34.4758064516129, 52.54329004329006],
        [34.27419354838709, 46.59090909090909],
        [39.11290322580645, 52.002164502164504],
        [38.91129032258064, 46.32034632034633],
        [42.54032258064515, 53.084415584415595],
        [43.95161290322581, 46.32034632034633],
        [46.37096774193547, 56.33116883116884],
        [47.983870967741936, 50.37878787878789],
        [47.37903225806451, 61.47186147186149],
        [50.403225806451616, 59.036796536796544],
        [47.37903225806451, 67.6948051948052],
        [51.41129032258064,66.8831168831169],
        [47.37903225806451, 73.37662337662339],
        [50.0, 75.27056277056278],
        [44.35483870967741, 76.8939393939394],
        [43.95161290322581, 81.4935064935065],
        [40.927419354838705, 75.54112554112555],
        [36.89516129032258, 80.41125541125542],
        [37.096774193548384, 75.81168831168833],
        [32.86290322580645, 78.24675324675326],
        [34.27419354838709, 73.91774891774892],
        [40.7258064516129, 80.95238095238096],
        [33.46774193548387, 71.21212121212122],
        [30.241935483870964, 76.62337662337663],
        [46.16935483870968, 75.27056277056278],
        [48.38709677419355, 80.41125541125542]
    ]

types = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

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
