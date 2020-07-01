import math
import cv2
import numpy as np
path = "./outTask/"

class Point:
    x = 0
    y = 0
    v = 0
    def __init__(self, x, y, v):
        self.x = x
        self.y = y
        self.v = v
    def __sub__(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


def softmax(array):
    sumExps = sum([math.exp(point.v) for point in array])
    print(sumExps)
    counter = 0

    return [math.exp(num.v) / sumExps for num in array]
file_ = open(f"{path}{1}_{1}_Out.txt", 'r')

def getData(pathToData):
    rawData = open(pathToData, 'r').read()
    result = []

    for nums in rawData.split("\n"):
        data = nums.split()
        if len(data) > 5:
            data = list(map(float, [data[num] for num in range(1, 6, 2)]))
            result.append(Point(data[0], data[1], data[2]))
    return result


def getPlot(path, n, m):
    r = getData(path)
    maxX = -10000
    maxY = -10000
    minX = 10000000
    minY = 10000000
    for point in r:
        if point.y > maxY:
            maxY = point.y
        if point.x > maxX:
            maxX = point.x
        if point.y < minY:
            minY = point.y
        if point.x < minX:
            minX = point.x
    print(softmax(r))
    print(maxX, maxY, minX, minY)
    pic = []
    for i in range(math.floor(maxY - minY) + 1):
        pic.append([])
        for j in range(math.floor(maxX - minX) + 1):
            pic[-1].append([19, 0, 0])

    print(len(pic))
    for point in r:
        print(math.floor(point.y - minY))
        print(math.floor(point.x - minX))
        print(maxX, minX, point.x)
        pic[math.floor(point.y - minY)][math.floor(point.x - minX)] = [int(math.floor(255 - 255 * point.v)), 0,
                                                                   int(math.floor(255 * point.v)), ]
    pic = np.array(pic)
    cv2.imwrite(f"task{n}{m}.bmp", pic)
for i in range(1, 4):
    for j in range(1, 7):
        getPlot(f"{path}task{i}_{j}_Out.txt", i, j)
