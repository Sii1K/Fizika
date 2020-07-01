import math

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

def findMin(point, arrayPoints):
    result = sorted(arrayPoints, key=lambda x: point.x - x.x)
    minV = 10000000
    minP = Point(0, 0, 0)
    maxP = Point(0, 0, 0)
    maxV = -10000000
    for i in result:
        if minV != 10000000 and maxV != -10000000:
            return [minP, maxP]
        if point.x < i.x:
            minV = i.x
            minP = i
        if point.x > i.x:
            maxV = i.x
            maxP = i

def findMinY(point, arrayPoints):
    result = sorted(arrayPoints, key=lambda x: point.y - x.y)
    minV = 10000000
    minP = Point(0, 0, 0)
    maxP = Point(0, 0, 0)
    maxV = -10000000
    for i in result:
        if minV != 10000000 and maxV != -10000000:
            return [minP, maxP]
        if point.y < i.y:
            minV = i.y
            minP = i
        if point.y > i.y:
            maxV = i.y
            maxP = i

def getValues(filePath):
    file = open(filePath, 'r')
    rawData = file.read().split('\n')[9:]
    data = [x.split() for x in rawData]
    for i in data:
        try:
            i[2] = i[2].split('-')[0]
        except:
            print(i)
        arr = []
        for i in data:
            print(i)
            try:
                arr.append(Point(float(i[0]), float(i[1]), float(i[2])))
            except:
                pass
        return arr

def total():
    for taskn in range(1, 4):
        for i in range(1, 7):
            arr = getValues(f"task{taskn}_{i}.txt")
            fileOut = open(f"./outTask/task{taskn}_{i}_Out.txt", 'w')
            for value in arr:
                buffer = findMin(value, arr)
                buffery = findMinY(value, arr)
                try:
                    value_ = Point(buffer[0].x, buffer[0].y, math.sqrt((buffer[0].v - buffer[1].v) ** 2 + (buffery[0].v - buffery[1].v) ** 2))
                    print(f"x: {value_.x}\ty: {value_.y}\t E: {value_.v}", file=fileOut)
                except:
                    pass
if __name__ == "__main__":
    total()
