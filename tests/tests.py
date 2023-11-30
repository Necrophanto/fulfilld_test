from main import bob_prob
import unittest

class TestBobProb(unittest.TestCase):
    def test1(self):
        result = bob_prob(6,10)
        self.assertEqual(result, [float(1/6),float(1/7),float(1/8),float(1/9),float(1/10)])
    
    def test2(self):
        self.assertRaises(Exception, bob_prob, (6,2))
        
"""
print("<<<<",combinations(52,13)) # Total bridge hands (13 cards) with regular deck of cards (52 cards)
print(combinations(1,1))
print(">>>", truncated_factorial(40,52)/math.factorial(13))  #truncated_factorial(1,13))
print("<<<.>>>", binomial_experiment(1,1,(1/6)))
print("<<<.>>>", binomial_experiment(2,5,0.1))
print("<<<.>>>", binomial_experiment(3,5,0.5)) # Get exactly 3 heads in 5 coin toss
"""

if __name__== '__main__':
    unittest.main()
