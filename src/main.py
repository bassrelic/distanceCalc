from hashlib import new
import numpy as np
import matplotlib.pyplot as plt
from source import Source
from sink import Sink

source1 = Source(0, 20)
source2 = Source(0, 25)

sourceListx = []
sourceListy = []

sourceListx.append(source1.getPosx())
sourceListx.append(source2.getPosx())
sourceListy.append(source1.getPosy())
sourceListy.append(source2.getPosy())

limit = 10.92

sinkList = []

for x in range(0, 10):
    for y in range(0, 50):
        sinkList.append(Sink(x, y, source1, source2))

for item in sinkList:
    item.calcDistances()
    item.checkDistanceLimit(limit)

sourceListUnderLimx = [None]
sourceListUnderLimy = [None]
sourceListOverLimx = [None]
sourceListOverLimy = [None]

for item in sinkList:
    if item.getOverDistance() is False:
        sourceListUnderLimx.append(item.getPosx())
        sourceListUnderLimy.append(item.getPosy())
    else:
        sourceListOverLimx.append(item.getPosx())
        sourceListOverLimy.append(item.getPosy())

plt.scatter(sourceListUnderLimx, sourceListUnderLimy)
plt.scatter(sourceListOverLimx, sourceListOverLimy, c='#ff7f0e')
plt.scatter(sourceListx, sourceListy, c='#FF0000')
plt.show()