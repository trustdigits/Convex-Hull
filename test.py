import pylab as pl
import sys
import  mathlib, geometry
import numpy as np

points_set = [[2,3],[10,7],[-4,9],[0,18],[25,17],[-5,14],[-6,1],[-1,4],[-2,12],[1,10],[-4,13],[11,10],[17,15],
              [2,14],[16,16],[18,2],[20,19],[-7,18],[-6,2],[-1,-1],[-5,10],[10,10],[-4,-4],[14,12],[16,14],[6,13],[12,15],[1,2],[16,1]]

pl.scatter([X[0] for X in points_set],[X[1] for X in points_set])
hull = geometry.convexHull(points_set)
full = geometry.full_hull(hull)
pl.scatter([X[0] for X in full],[X[1] for X in full], c='r')

pl.show()

 
    
