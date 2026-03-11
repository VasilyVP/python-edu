import numpy as np
from scipy.spatial import KDTree

# from scipy.spatial import  Delaunay, ConvexHull
# import matplotlib.pyplot as plt
from scipy.spatial.distance import euclidean, cityblock

""" points = np.array([[2, 4], [3, 4], [3, 0], [2, 2], [4, 1]])
simplices = Delaunay(points).simplices

plt.triplot(points[:, 0], points[:, 1], simplices)
plt.scatter(points[:, 0], points[:, 1], color="r")
plt.show() """

""" points = np.array(
    [[2, 4], [3, 4], [3, 0], [2, 2], [4, 1], [1, 2], [5, 0], [3, 1], [1, 2], [0, 2]]
)
hull = ConvexHull(points)
hull_points = hull.simplices

plt.scatter(points[:, 0], points[:, 1])
for simplex in hull_points:
    plt.plot(points[simplex, 0], points[simplex, 1], "k-")

plt.show() """

# KDTree for nearest neighbor search
points = [(1, -1), (2, 3), (-2, 3), (2, -3)]
kdtree = KDTree(points)
res = kdtree.query((1, 1))
print(res)

# Calculate the Euclidean distance between two points
point1 = (1, -1)
point2 = (2, 3)
distance = euclidean(point1, point2)
print(distance)

# Calculate the Manhattan distance between two points
p1 = (1, 0)
p2 = (10, 2)
res = cityblock(p1, p2)
print(res)
