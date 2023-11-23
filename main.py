#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Problem Statement
You have two players, Bob and Alice, that take turns in rolling a fair k-sided die. Whoever rolls a
k first wins the game. The Python program should output the probability that Bob wins the
game for k = 6 thru 99. That is, the output will be an array of probabili8es where index 0 is the
probability when k = 6; index 1 when k = 7; etc.
"""
def bob_prob(min_sides: int, max_sides: int) -> list:
    # Bob's chance to win are 1/k given a k-sided dice, then for each dice we gather this chances in a list
    if max_sides < min_sides or min_sides < 6:
        raise Exception("A dice shuould have at least 6 sides, and the maximum number of sides should be greater than the minimum number of sides")
    else:
        bob_res = [(1/i) for i in range(min_sides,max_sides+1)]
        
    return bob_res

# I will not use this since the chances are 1/2 for each one the result will be the same
# def ali_prob() -> list:
#     ali_res = [i for i in range(6,100)]
#     return ali_res

def main(args):
    # Here the chances for Bob to win is 1/2 since he's playing with Alice, thus Bob's chances should be multiplied by 1/2
    result = map(lambda x: x*0.5, bob_prob(6,99))
    
    return list(result)


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
