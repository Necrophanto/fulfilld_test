from main import bob_prob
import unittest

class TestBobProb(unittest.TestCase):
    def test1(self):
        result = bob_prob(6,10)
        self.assertEqual(result, [float(1/6),float(1/7),float(1/8),float(1/9),float(1/10)])
    
    def test2(self):
        self.assertRaises(Exception, bob_prob, (6,2))

if __name__== '__main__':
    unittest.main()
