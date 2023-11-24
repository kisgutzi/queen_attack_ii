# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 17:34:49 2023

@author: Johannesz
"""
import math
import os
import random
import re
import sys
from itertools import product

def queensAttack(n, k, r_q, c_q, obstacles):
    '''
    először kiküszöbölni az olyan potenciális hibákat amik 
    nincsenek benen a 'Constraints' részben
    '''
    #ha n kevesebb mint 2 akkor 0 az érték
    if n<2: 
        return 0
    else:
        #kivenni az ismétlődő obstacleket ha vannak
        o_unique = set([(row, col) for row,col in obstacles])
        #ez elvileg az összes relatív irányt megadja
        directions = set(product([-1, 0, 1], repeat=2)) - {(0, 0)}
        '''
        meg kell számolni, hogy hány lépést tud menni 
        (abszolút pozíció + relatív pozíció), úgy hogy nem ütközik 
        obstacle-be vagy nem ér el a tábla végéig
        '''
        count = 0
        for items in directions:
            #kezdő pozíció
            pos = tuple(map(sum,zip((r_q,c_q),items)))
            #addig lépkedjen amíg nem ér a tábla végére vagy ütközik obstacle-be
            while pos not in o_unique and 1 <= pos[0] <= n and 1 <= pos[1] <= n:
                #lépés utáni pozíció 
                pos = tuple(map(sum,zip(pos,items)))
                #minden lépés 1-el több opció
                count+=1
        return count
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
