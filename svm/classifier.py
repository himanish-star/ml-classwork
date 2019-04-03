import matplotlib.pyplot as plt
import numpy as np

shapeShifter = 0

def onclick(event):
    global shapeShifter
    print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          ('double' if event.dblclick else 'single', event.button,
           event.x, event.y, event.xdata, event.ydata))
    if shapeShifter % 2 is not 0:
        plt.plot(event.xdata, event.ydata, 'ro')
    else:
        plt.plot(event.xdata, event.ydata, 'gx')
    shapeShifter += 1
    plt.show()

if __name__ == "__main__":
    fig, ax = plt.subplots()
    cid = fig.canvas.mpl_connect('button_press_event', onclick)
    plt.show()
