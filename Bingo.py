import random as rd
import numpy as np
import itertools

def bingo_card():
    
    x1 = [1,1,1,2,2,2,2,2,2]
    rd.shuffle(x1)

    raw_bingo_card = [rd.sample(range(1,10),x1[0]),rd.sample(range(10,20),x1[1]),rd.sample(range(20,30),x1[2]),
                      rd.sample(range(30,40),x1[3]),rd.sample(range(40,50),x1[4]),rd.sample(range(50,60),x1[5]),
                      rd.sample(range(60,70),x1[6]),rd.sample(range(70,80),x1[7]),rd.sample(range(80,91),x1[8])]
    
    bingo_card = list(itertools.chain(*raw_bingo_card))
    
    return bingo_card


def bingo_draw():
    
    draw = rd.sample(range(1,91),90)
    
    return draw


def all_players(players):
    
    all_cards = []
    
    for i in range(1,players+1):
        all_cards.append(bingo_card())
        
    
    return all_cards
        

def winner_time(num_players):
    
    x = 0
    
    players_playing = all_players(num_players)
    
    for i in bingo_draw():
        
        x += 1
        for sub in players_playing: #https://www.geeksforgeeks.org/python-remove-given-element-from-list-of-lists/
            sub[:] = [ele for ele in sub if ele != i] 
        
        for y in players_playing:
            if len(y) == 0:
                return x
 
 
 
 winner_time(10000)
 
 
