import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    confidenceFactors = np.array([0.002 , 0.008 , 0.02 , 0.08 , 0.1 , 0.2 , 0.3 , 0.4 , 0.5])
    accuracy = np.array([77.9221, 77.9221, 76.6234, 76.6234, 75.3247, 75.3247, 75.974, 74.026, 74.026])
    plt.plot(accuracy,confidenceFactors,'k-')
    plt.ylabel('confidenceFactors')
    plt.xlabel('accuracy')
    plt.show()
