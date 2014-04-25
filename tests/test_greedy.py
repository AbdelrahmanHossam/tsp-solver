from unittest import TestCase

from tsp_solver import greedy

def make_dist_matrix( n, default, ijd_tuples ):
    """Utility function to make square distance matrices"""
    dist = [ [default for j in xrange(n)]
             for i in xrange(n)]
    for i,j,d in ijd_tuples:
        dist[i][j] = d
        dist[j][i] = d
    return dist

class TestGreedy( TestCase ):
    def test_empty_graph(self):
        distances = []
        vertices = greedy.solve_tsp( distances )
        self.assertListEqual( vertices, [] )

    def test_single_vertes(self):
        vs = greedy.solve_tsp( [[1]] )
        self.assertListEqual( vs, [0] )

    def test_two_vertices(self):
        dist = [[0, 1],
                [1, 0]]
        vs = greedy.solve_tsp( dist )
        self.assertListEqual( vs, [0,1] )

    def test_three_vertices(self):
        #Make a simple matrix with 2 short paths: 0->2 and 2->1
        D = make_dist_matrix(3, 1000, [(0,2,5), (2,1,1)])
        vs = greedy.solve_tsp( D )
        self.assertListEqual( vs, [0,2,1] )

    def test_

class TestGreedyNumpy( TestCase ):
    def test_empty_graph(self):
        distances = []
        vertices = greedy.solve_tsp_numpy( distances )
        self.assertListEqual( vertices, [] )
    
