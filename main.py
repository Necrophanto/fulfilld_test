#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint
import time
import sqlite3

"""
Problem Statement
You have two players, Bob and Alice, that take turns in rolling a fair k-sided die. Whoever rolls a
k first wins the game. The Python program should output the probability that Bob wins the
game for k = 6 thru 99. That is, the output will be an array of probabili8es where index 0 is the
probability when k = 6; index 1 when k = 7; etc.
"""



db = sqlite3.connect('test.db')

with db as conn:
    cursor = conn.cursor()
    # Create the table for the results
    cursor.execute("""CREATE TABLE IF NOT EXISTS results (
                dice_sides integer,
                rolls_qty integer,
                bob_wins integer,
                alice_wins integer,
                bobs_prob real
                )""")
    conn.commit()







def bob_rolls(sides: int):
    b_roll = randint(1,sides)
    return b_roll

def ali_rolls(sides: int):
    a_roll = randint(1,sides)
    return a_roll

def simulate_rolls(dice_sides: int, total_rolls: int):
    scores = {'Bob':0, 'Alice':0}
    for i in range(1,total_rolls+1):
        bob_w = bob_rolls(dice_sides)
        ali_w = ali_rolls(dice_sides)
        # print(i)
        if bob_w == dice_sides:
            scores["Bob"] += 1
        if ali_w == dice_sides:
            scores["Alice"] += 1
    
    return scores

# def quicker_simulation(rolls: int, sides: int):
#     b_wins = 0
#     a_wins = 0
#     for i in range(rolls):
#         bob = bob_rolls(sides)
#         if bob == sides:
#             b_wins += 1
#         ali = ali_rolls(sides)
#         if ali == sides:
#             a_wins += 1
#         # print(">>>",bob)
#     print(b_wins,"winned by Bob.", float(b_wins/events))
#     print(a_wins,"winned by Alice.", float(a_wins/events))
# quicker_simulation(events,dice_sides)
    

start = time.time()
# ----------------------------------------------------------------------------
# ToDo:
# | Run for 100, 1000, 10000, 100000, 1000000 
# | Build binomial definition 
# | Add bobs_prob field to table and recreate DB [DONE]
# | Add context manager for db connection [DONE]
events = 100000
# dice_sides = 10
# results = simulate_rolls(dice_sides,events)
# print(">>>>>", results)
# print(results['Bob']," winned by Bob.", f"Probability: {float(results['Bob']/events)}")
# print(results['Alice']," winned by Alice.", f"Probability: {float(results['Alice']/events)}")

# with conn as db_conn:
#     for s in range(6,100):
#         results = simulate_rolls(s,events)
#         # print(f"For {s} sided dice, Bob winned {results['Bob']} times.", f"Bob's probability of winning: {float(results['Bob']/events)}")
#         insertion = db_conn.execute(f"""INSERT INTO results(dice_sides, rolls_qty, bob_wins, alice_wins) 
#                                     VALUES ({s}, {events}, {results['Bob']}, {results['Alice']});""")

# with conn as db_conn:
#     test = db_conn.execute('DELETE FROM results;')
#     resultados = db_conn.execute('SELECT * from results;').fetchall()
#     print("<<<", resultados)

# ----------------------------------------------------------------------------
stop = time.time()
print(f"Elapsed time: {stop - start}.")


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
"""
