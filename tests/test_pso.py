import unittest
from pso import pso_simple
from pso.cost_functions import dixonPriceFunc, zakharovFunc  
from random import uniform


class test_all(unittest.TestCase):

    def test_dixonPriceFunc(self):
        x0 = [uniform(-10, 10) for x in range(20)]
        bounds = [(-10, 10)] * 20  
        opt = pso_simple.minimize(dixonPriceFunc, x0, bounds, num_particles=171, maxiter=400, verbose=True)
        self.assertLess(dixonPriceFunc(opt[1]), dixonPriceFunc(x0))

    def test_zakharovFunc(self):
        x0 = [uniform(-5, 10) for x in range(20)]
        bounds = [(-5, 10)] * 20  
        opt = pso_simple.minimize(zakharovFunc, x0, bounds, num_particles=178, maxiter=400, verbose=True)
        self.assertLess(zakharovFunc(opt[1]), zakharovFunc(x0))

if __name__ == '__main__':
    unittest.main()
