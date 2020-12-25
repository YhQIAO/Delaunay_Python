from PointClass import Point

class Triangle():
    p1 = Point(0,0)
    p2 = Point(0,0)
    p3 = Point(0,0)

    edge12 = False
    edge13 = False
    edge23 = False
    index = 0

    def __init__(self,P1,P2,P3):
        self.p1 = P1
        self.p2 = P2
        self.p3 = P3