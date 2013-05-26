import unittest


import pylab as pl

import geometry
import numpy as np

class TestSequenceFunctions(unittest.TestCase): #subclass unittest.TestCase

    def testFullHull2(self):
        
        points_set = [[2,3],[10,7],[-4,9],[0,18],[25,17],[-5,14],[-6,1],[-1,4],[-2,12],[1,10],[-4,13],[11,10],[17,15],
                      [2,14],[16,16],[18,2],[20,19],[-7,18],[-6,2],[-1,-1],[-5,10],[10,10],[-4,-4],[14,12],[16,14],[6,13],[12,15],[1,2],[16,1]]

        pl.scatter([X[0] for X in points_set],[X[1] for X in points_set])
        hull = geometry.convexHull(points_set)
        full = geometry.full_hull(hull)
        pl.scatter([X[0] for X in full],[X[1] for X in full], c='r')

        pl.show()
 
        self.assertMatrixEqual(full,[[-7, 18], [-6, 1], [-6, 18], [-5, -2], [-5, 18], [-4, -4], [-4, 18], [-3, -4], [-3, 18], [-2, -4], [-2, 18],
                                     [-1, -4], [-1, 18], [0, -3], [0, 18], [1, -3], [1, 18], [2, -3], [2, 18], [3, -3], [3, 18], [4, -2], [4, 18], [5, -2],
                                     [5, 18], [6, -2], [6, 18], [7, -2], [7, 18], [8, -1], [8, 18], [9, -1], [9, 18], [10, -1], [10, 18], [11, -1], [11, 18],
                                     [12, 0], [12, 18], [13, 0], [13, 18], [14, 0], [14, 18], [15, 0], [15, 18], [16, 1], [16, 18], [17, 1], [17, 18], [18, 2],
                                     [18, 18], [19, 4], [19, 18], [20, 6], [20, 19], [21, 8], [21, 18], [22, 10], [22, 18], [23, 12], [23, 17], [24, 14],
                                     [24, 17], [25, 17]])

    def assertMatrixAlmostEqual(self, mat1, mat2, tol):
        """
        Assert if two matrices are almost equal
        """
        self.assertEqual((len(mat1[0]),len(mat2[0])), (len(mat1[1]),len(mat2[1])))
        for i in range(len(mat1)):
            for a, b in zip(mat1[i], mat2[i]):
                 self.assertAlmostEqual(a, b, tol)


    def assertMatrixEqual(self, mat1, mat2):
        """
        Assert if two matrices are almost equal
        """
        self.assertEqual((len(mat1[0]),len(mat1[1])), (len(mat2[0]),len(mat2[1])))
        for i in range(len(mat1)):
            for a, b in zip(mat1[i], mat2[i]):
                 self.assertEqual(a, b)
                 
if __name__ == '__main__':
    unittest.main()
 
    
