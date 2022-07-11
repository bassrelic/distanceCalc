from math import sqrt
from object import Object
from source import Source

class Sink(Object):
    def __init__(self, x, y, source1, source2):
        super().__init__(x, y)
        self.source1 = source1
        self.source2 = source2
        self.dist1 = 0
        self.dist2 = 0
        self.overDistance = False

    def calcDistances(self):
        diffx = self.x - self.source1.getPosx()
        diffy = self.y - self.source1.getPosy()
        self.dist1 = sqrt(pow(diffx, 2) + pow(diffy, 2))

        diffx = self.x - self.source2.getPosx()
        diffy = self.y - self.source2.getPosy()
        self.dist2 = sqrt(pow(diffx, 2) + pow(diffy, 2))

    def checkDistanceLimit(self, limit):
        dist = self.dist1 - self.dist2
        if (abs(dist) >= limit):
            self.overDistance = True

    def getOverDistance(self):
        return self.overDistance
