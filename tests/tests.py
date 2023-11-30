from main import bob_prob, combinations, truncated_factorial, binomial_experiment
import unittest

class TestFunctions(unittest.TestCase):
    def test_bob_prob(self):
        result = bob_prob(6,10)
        self.assertEqual(result, [float(1/6),float(1/7),float(1/8),float(1/9),float(1/10)])
    
    def test_bob_prob_exception(self):
        self.assertRaises(Exception, bob_prob, (6,2))
    
    def test_combinations(self):
        # Calculate total number of bridge hands (13 cards) with regular deck of cards (52 cards) R= 635 013 559 600
        self.assertEqual(combinations(52,13), 635013559600)
    
    def test_truncated_factorial(self):
        # Let's truncate 6! up to 3, this means the we calculate 6*5*4*3 = 360
        self.assertEqual(truncated_factorial(3,6), 360)
    
    def test_binomial_experiment(self):
        # Get exactly 3 heads in 5 succesive coin toss R= 5/16
        self.assertEqual(binomial_experiment(3,5,0.5), float(5/16))
        

if __name__== '__main__':
    unittest.main()
