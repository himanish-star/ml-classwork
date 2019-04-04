import matplotlib.pyplot as plt
import numpy as np
from sklearn import svm

shapeShifter = 0

points = []
classValues = []
lastLinePtrSet = False
lastLinePtr = 0

def plotHyperplane():
    global points, classValues, lastLinePtr, lastLinePtrSet
    print(points, classValues)
    if lastLinePtrSet:
        lastLinePtr.remove()
    else:
        lastLinePtrSet = True
    tp = np.array(points)
    tc = np.array(classValues)
    clf = svm.SVC(kernel='linear', C = 1000000.0, gamma = 1.0)
    clf.fit(tp, tc)
    w = clf.coef_[0]
    a = -w[0]/w[1]
    xx = tp[:,0]
    yy = a * xx - clf.intercept_[0] / w[1]
    lastLinePtr, = plt.plot(xx, yy, 'k-')
    plt.draw()

def onclick(event):
    global shapeShifter, points, classValues
    print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          ('double' if event.dblclick else 'single', event.button,
           event.x, event.y, event.xdata, event.ydata))
    if shapeShifter % 2 is not 0:
        plt.plot(event.xdata, event.ydata, 'ro')
        points.append([event.xdata,event.ydata])
        classValues.append(0)
    else:
        plt.plot(event.xdata, event.ydata, 'gx')
        points.append([event.xdata,event.ydata])
        classValues.append(1)
    shapeShifter += 1
    print(points)
    print(classValues)
    if shapeShifter >= 2:
        plotHyperplane()
    plt.draw()

if __name__ == "__main__":
    fig, ax = plt.subplots()
    ax.set_xlim(left=0,right=100)
    ax.set_ylim(bottom=0,top=100)
    cid = fig.canvas.mpl_connect('button_press_event', onclick)
    plt.show()
