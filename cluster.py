import random
import math

#
#   Example code for the k-means clustering algorithm.
#
#   Author: Chris Leckie 
#
#   Starts by assigning points at random to clusters,
#   and calculates the "centre of gravity" (centroid)
#   of each cluster, based on the mean of the points
#   assigned to that cluster.
#
#   Then for a fixed number of iterations the algorithm
#   repeats (1) reassigning each point to
#   the nearest cluster using the updated cluster centroids,
#   and (2) updating each cluster centroid based on the
#   corresponding points that are now members of that cluster.
#

data = [(6,8), (9,8), (9,9), (8,5), (7,6), (6,9), (5, 7), (8, 8), (9, 5)]


def k_means(points, k_clusters, max_iterations=4):

    iterations = 0
    memberships = [random.randrange(0, k_clusters) for p in points]
    centroids = update_centroids(points, memberships, k_clusters)

    while iterations < max_iterations:
        memberships = update_memberships(points, centroids)
        centroids = update_centroids(points, memberships, k_clusters)
        iterations += 1
        print(iterations)
        for c in centroids:
            print(c)

    return memberships, centroids

def update_centroids(points, memberships, k_clusters):
    centroids = []
    for k in range(k_clusters):
        x = 0
        y = 0
        n = 0
        for i in range(len(points)):
            if memberships[i] == k:
                n += 1
                x += points[i][0]
                y += points[i][1]
        if n > 0:
            x = x / n
            y = y / n
        centroids.append((x,y))
    return centroids

def update_memberships(points, centroids):
    memberships = []
    for p in range(len(points)):
        nearest_distance = distance(points[p], centroids[0])
        nearest_centroid = 0
        for c in range(1,len(centroids)):
            d = distance(points[p], centroids[c])
            if d < nearest_distance:
                nearest_centroid = c
                nearest_distance = d
        memberships.append(nearest_centroid)
    return memberships

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + \
                                 (p1[1] - p2[1])**2)

#
#   Generate a random set of n points corresponding to
#   Gaussian distributions centred on the given centroids
#   with the given standard deviation.
#   This can be used to test our k-means clustering algorithm.
#

def rand_data(centroids, stddev, n):
    memberships = [random.randrange(0, len(centroids)) for p in range(n)]
    points = []
    for m in memberships:
        point = []
        centroid = centroids[m]
        for d in range(len(centroid)):
            point.append(random.normalvariate(centroid[d], stddev))
        points.append(tuple(point))
    return points

big_data = rand_data([(5,2),(8,7),(3,6)],0.5,300)
