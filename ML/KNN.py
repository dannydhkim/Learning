import numpy as np
import matplotlib.pyplot as plt

class k_nearest_neighbors:
    def __init__(self, k):
        self.k = k
    
    def calculateDistance(x1, y1, x2, y2):
        return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    
    
    def nearestNeighbors():



def main():
    X = np.random.randint(20, size=50)
    y = np.random.randint(20, size=50)

    category = []
    for i in range(50):
        if X[i] < 10 and y[i] < 12.5:
            category.append(0)
        elif X[i] > 10 and y[i] < 12.5:
            category.append(1)
        else:
            category.append(2)

    cdict= {0:'red',1:'blue', 2:'green'}
    fig, ax = plt.subplots()
    for g in np.unique(category):
        ix = np.where(category == g)
        ax.scatter(X[ix], y[ix], c = cdict[g], label = g, s = 100)
    ax.legend()
    plt.show()

if __name__ == "__main__" : 
    main()
