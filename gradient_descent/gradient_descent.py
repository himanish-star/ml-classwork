import numpy as np
import matplotlib.pyplot as plt

learning_rate = 0.3

def gradient_descent(x, y, b0, b1):
    y_calc = b0 + b1*x;

    n = len(y)

    error_b0 = sum(y_calc - y)/n
    error_b1 = sum((y_calc - y)*x)/n

    print((sum((y_calc-y)**2))/n)

    b0 -= error_b0
    b1 -= error_b1
    return b0 , b1

def regression_plot(counter, coords):
    for coord in coords:
        plt.plot(coord[0], coord[1], 'y.')


    x = np.array([coord[0] for coord in coords])
    y = np.array([coord[1] for coord in coords])

    b0 = 0
    b1 = 0

    while counter > 0:
        counter -= 1
        b0, b1 = gradient_descent(x, y, b0, b1)
        line, = plt.plot(x, b0 + b1*x, 'g')
        plt.pause(0.2)
        if counter != 0:
            line.remove()


    plt.show()

    # while counter--:
    #     gradient_descent(x, y, b0, b1)


def main():
    # generate random data
    coords = np.random.randn(50,2)
    regression_plot(10, coords)

if __name__ == '__main__':
    main()
