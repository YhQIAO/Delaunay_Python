import matplotlib.pyplot as plt
import numpy as np
from PointClass import Point
import PointClass
import Functions
from Triangle import Triangle

from scipy.spatial import Delaunay

num = 20

randX = 100*np.random.rand(num)
randY = 100*np.random.rand(num)
K = -1
L = -1
PointList = []
t1 = []
t2 = []
t3 = []
triangleList = []

for i in range (0,num):
    p = Point(randX[i],randY[i])
    p.index = i
    PointList.append(p)

# 随机选取一个点，找出与之最近的一个点作为初始基线
initPoint = PointList[1]
t1.append(initPoint)

t2.append(PointList[
              Functions.getIndexOfMinDisPoint(t1[0],PointList)])
plt.plot([t1[0].x,t2[0].x],[t1[0].y,t2[0].y])

# 获取这两个点的中点
middlePoint = Point((t1[0].x+t2[0].x)/2.0, (t1[0].y+t2[0].y)/2.0)
# 剩余点到这个中点最小距离的点
t3.append(
    PointList[
        Functions.getIndexOfMinDisPointWithIgnoration(
        middlePoint,PointList,[t1[0].index,t2[0].index])
    ]
)
plt.subplot(1,2,1)
plt.plot([t1[0].x,t3[0].x],[t1[0].y,t3[0].y],'b')
plt.plot([t3[0].x,t2[0].x],[t3[0].y,t2[0].y],'b')
#------------到这里完成第一个三角形的创建---------------------
L = 0
K = 0
tri0 = Triangle(t1[0],t2[0],t3[0])
tri0.index = 0
triangleList.append(tri0)

for i in range(0,1000):
    # 注意索引与数量之间相差1
    if not triangleList[K].edge12:
        index = Functions.find_Point_index(1,PointList,triangleList[K])
        if index != -1: #拓展
            L = L+1
            t1.append(triangleList[K].p1)
            t2.append(triangleList[K].p2)
            t3.append(PointList[index])
            plt.plot([t1[L].x, t3[L].x], [t1[L].y, t3[L].y])
            plt.plot([t3[L].x, t2[L].x], [t3[L].y, t2[L].y])

            tri = Triangle(t1[L],t2[L],t3[L])
            tri.edge12 = True
            triangleList.append(tri)

    if not triangleList[K].edge13:
        index = Functions.find_Point_index(2, PointList, triangleList[K])
        if index != -1:  # 拓展
            L = L + 1
            t1.append(triangleList[K].p1)
            t2.append(triangleList[K].p3)
            t3.append(PointList[index])
            plt.plot([t1[L].x, t3[L].x], [t1[L].y, t3[L].y])
            plt.plot([t3[L].x, t2[L].x], [t3[L].y, t2[L].y])

            tri = Triangle(t1[L], t2[L], t3[L])
            tri.edge12 = True
            triangleList.append(tri)

    if not triangleList[K].edge23:
        index = Functions.find_Point_index(3, PointList, triangleList[K])
        if index != -1:  # 拓展
            L = L + 1
            t1.append(triangleList[K].p2)
            t2.append(triangleList[K].p3)
            t3.append(PointList[index])
            plt.plot([t1[L].x, t3[L].x], [t1[L].y, t3[L].y])
            plt.plot([t3[L].x, t2[L].x], [t3[L].y, t2[L].y])

            tri = Triangle(t1[L], t2[L], t3[L])
            tri.edge12 = True
            triangleList.append(tri)
    K = K+1


for p in PointList:
    plt.scatter(p.x,p.y)

plt.subplot(1,2,2)
for p in PointList:
    plt.scatter(p.x,p.y)
plt.scatter(p.x,p.y)

ma = np.zeros((num,2))
ma[:,0] = randX
ma[:,1] = randY

tri = Delaunay(ma)
plt.triplot(ma[:,0], ma[:,1], tri.simplices.copy())
plt.plot(ma[:,0], ma[:,1], 'o')
plt.show()