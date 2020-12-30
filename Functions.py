from PointClass import Point
import math
from matplotlib import pyplot as plt

def GetDistance(P1,P2):
    return math.sqrt((P1.x-P2.x)**2+(P1.y-P2.y)**2)

def getIndexOfMinDisPoint(p,pointList):
    dmin = 1e9
    minIndex = 0
    for i in range(0,len(pointList)):
        if GetDistance(pointList[i], p) < dmin\
                and GetDistance(pointList[i], p)!=0:
            dmin = GetDistance(pointList[i], p)
            minIndex = i
    return minIndex

def getIndexOfMinDisPointWithIgnoration(p,pointList,ignoreList):
    dmin = 1e9
    minIndex = 0
    for i in range(0,len(pointList)):
        if GetDistance(pointList[i], p) < dmin\
                and GetDistance(pointList[i], p)!=0\
                and i not in ignoreList:
            dmin = GetDistance(pointList[i], p)
            minIndex = i
    return minIndex

# 扩展k号三角形的方法
def find_Point_index(n,PointList,triangle):
    index = -1
    if n == 1:
        p1 = triangle.p1
        p2 = triangle.p2
        p3 = triangle.p3
    if n == 2: # 1---3
        p1 = triangle.p1
        p2 = triangle.p3
        p3 = triangle.p2
    if n == 3: # 1---3
        p1 = triangle.p2
        p2 = triangle.p3
        p3 = triangle.p1

    a = (p2.y - p1.y) / (p2.x - p1.x)
    b = (p1.x * p2.y - p2.x * p1.y) / (p2.x - p1.x)
    f = p3.y - a * p3.x + b
    if f < 0:
        label = -1
    else:
        label = 1
    da = GetDistance(p1,p2)
    angleMax = -1
    for i in range(0,len(PointList)):
        p = PointList[i]

        if p.x != p3.x and p.y != p3.y \
                and p.x != p1.x and p.y != p1.y \
                and p.x != p2.x and p.y != p2.y and\
                (p.y-a*p.x+b)*label < 0:
            db = GetDistance(p,p1)
            dc = GetDistance(p,p2)
            angle = math.acos(
                (db**2+dc**2-da**2) / (2*db*dc)
            )

            if angle > angleMax:
                angleMax = angle
                index = i

    return index

def isSame(p1,p2):
    if p1.x == p2.x and p1.y == p2.y:
        return True
    else:
        return False

# 判断一个三角形的变是否已经出现了两次
def isRepeat(p1,p2,triangleList):
    Sum = 0
    for tri in triangleList:
        if (isSame(p1,tri.p1) and isSame(p2,tri.p2))\
            or (isSame(p1,tri.p2) and isSame(p2,tri.p1))\
            or (isSame(p1,tri.p1) and isSame(p2,tri.p3))\
            or (isSame(p1,tri.p3) and isSame(p2,tri.p1))\
            or (isSame(p1,tri.p2) and isSame(p2,tri.p3))\
            or (isSame(p1,tri.p3) and isSame(p2,tri.p2)):
            Sum = Sum+1
    if Sum >=2:
        return True
    else:
        return False