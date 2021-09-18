import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import mode

class k_nearest_neighbors():
    def __init__(self, k):
        self.k = k
    
    def calculateDistance(self,x1, y1, x2, y2):
        return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    
    def nearestNeighbors(self, data, target):
        distances = {}
        for i in range(data.shape[1]):
            distances[self.calculateDistance(target[0],target[1],data[0][i],data[1][i])] = (i, data[2][i])
        self.neighbors = []
        votes = []
        for key in sorted(distances.keys())[:self.k]:
            self.neighbors.append((distances[key][0], key))
            votes.append(distances[key][1])
        most_voted = mode(votes)
        return self.neighbors, most_voted[0][0]

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
    
    target_X = input("X")
    target_y = input("y")
    target = [float(target_X),float(target_y)]
    data = np.array((X,y,category))

    cdict= {0:'red',1:'blue', 2:'green'}
    fig, ax = plt.subplots()
    for g in np.unique(category):
        ix = np.where(category == g)
        ax.scatter(X[ix], y[ix], c = cdict[g], label = g, s = 100)
    ax.legend()
    plt.show()

    model = k_nearest_neighbors(3)
    _, target_label = model.nearestNeighbors(data, target)
    print(target, 'categorized as:', target_label)

    ax.scatter(target[0], target[1], target_label)
    plt.show()

if __name__ == "__main__" : 
    main()

