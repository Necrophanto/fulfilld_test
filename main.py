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

# # --- Uncomment this section to create the DB and the results table ---
# with db as conn:
#     cursor = conn.cursor()
#     cursor.execute("""CREATE TABLE IF NOT EXISTS results (
#                 dice_sides integer,
#                 rolls_qty integer,
#                 bob_wins integer,
#                 alice_wins integer,
#                 bobs_prob real
#                 )""")
#     conn.commit()


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
        if bob_w == dice_sides:
            scores["Bob"] += 1
        if ali_w == dice_sides:
            scores["Alice"] += 1    
    return scores

    

start = time.time()
# -------------------------------------- BINOMIAL EXPERIMENT SIMULTAION --------------------------------------

# # --- This block simulates the rolls of the dices and inserts the results into the DB ---
# events = [100, 1000, 10000, 100000, 1000000]
# # Takes up to 2 minutes to complete the simulation using a nested for cycle, 
# # and takes up to half a minute to re-run it with a single value for the total number of rolls (events) and a single for loop
# with db as db_conn:
#     for e in events:  # This loop should be eliminated if we assign a single value for 'events' variable
#         for s in range(6,100):
#             results = simulate_rolls(s,e)
#             # print(f"For {s} sided dice, Bob winned {results['Bob']} times.", f"Bob's probability of winning: {float(results['Bob']/events)}")
#             b_prob = float(results['Bob']/e)
#             insertion = db_conn.execute(f"""INSERT INTO results(dice_sides, rolls_qty, bob_wins, alice_wins, bobs_prob) 
#                                         VALUES ({s}, {e}, {results['Bob']}, {results['Alice']}, {b_prob});""")

# # --- Block to check DB contains and/or delete previous results (if needed) ---
# with db as db_conn:
# #     delete = db_conn.execute('DELETE FROM results;')
#     resultados = db_conn.execute('SELECT * from results WHERE dice_sides=6 OR dice_sides=99 ORDER BY dice_sides ASC;').fetchall()
#     print("<<<", resultados)

# --- Binomial definition ---
"""
Definition: For experiments that involves two possible results (success and failure), we can calculate the probability for 'x' succesful results 
in the next 'n' executions, given a 'p' probability of success and a 'q' probability of failure, we cauculate that with the expression:
        b(x; n, p) = (nCx)*((p**x)*(q**(n-x)))
Where nCx is the total possible combinations in which the success event x can occur in the nex n executions, that can be calculated with factorials:
        nCx = (n!)/(x!*(n-x)!)
Where the ! symbol reffers the factorial function
"""
import math

def truncated_factorial(start: int, stop: int):
    fact = 1
    for num in range(start, stop + 1):
        fact *= num
    return fact


def combinations(n:int, x:int):
    """For nCm -> n = n ; m = x"""
    discard = n - x
    top = truncated_factorial(discard+1, n)
    bottom = math.factorial(x)
    result = top/bottom
    return int(result)

def binomial_experiment(x:int, n: int, p: float):
    """Non acummulative version for:
    b(x; n, p) = (nCx)*( (p**x) * (q**(n-x)) )
    where:
    (nCx)      = combinations_part
    (p**x)     = success_part
    (q**(n-x)) = failure_part
    """
    q = 1 - p
    combinations_part = combinations(n, x)
    success_part = p**x
    q_power = n - x
    failure_part = q**q_power
    result = combinations_part * success_part * failure_part
    return result

# ----- Comparison of experiment VS simulation results -----
# For a 6 sided dice the probability that Bob wins is 1/6, thus the experiment for 1 success in the next executions will be:
bobs_probability_1 = 1/6
qty_success = 1
qty_executions = 1
# For a 99 sided dice the probability that Bob wins is 1/99:
bobs_probability_2 = 1/99
print("\n-------------------------------------- FOR A 6 SIDED DICE SCENARIO: --------------------------------------\n")
print("Bob's Porbability according to binomial experiment: ", binomial_experiment(qty_success, qty_executions, bobs_probability_1))
with db as db_conn:
    resultados = db_conn.execute('SELECT dice_sides, rolls_qty, bob_wins, bobs_prob FROM results WHERE dice_sides=6;').fetchall()
    print("Bob's results in the different simulations: \n", resultados)

print("\n-------------------------------------- FOR A 99 SIDED DICE SCENARIO: --------------------------------------\n")
print("Bob's Porbability according to binomial experiment: ", binomial_experiment(qty_success, qty_executions, bobs_probability_2))
with db as db_conn:
    resultados = db_conn.execute('SELECT dice_sides, rolls_qty, bob_wins, bobs_prob FROM results WHERE dice_sides=99;').fetchall()
    print("Bob's results in the different simulations: \n", resultados)

# -------------------------------------- -------------------------------------- --------------------------------------



# #----- This section is keep because it was the original solution, it will have only one correction -----
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
    # result = map(lambda x: x*0.5, bob_prob(6,99))
    print("\n-------------------------------------- MAIN FUNCTION RESULTS FOR 6 AND 99 SIDED DICES: --------------------------------------\n")
    results = bob_prob(6,99)  # <- This is the correction, no longer multiplying for 1/2
    result = [results[0], results[-1]]
    return result


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

