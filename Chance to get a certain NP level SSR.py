# Chance to get a certain NP level SSR (ver 3)
import math
sq = int(input('SQs amount: '))
tix = int(input('Tickets number: '))
pulls = sq + tix*3
cards = pulls//30 * 11 
n = int(input('NP lvl: '))
if n == 1 and pulls >= 900:
    print('PITY')
else:
    total = 0
    x = 0
    for i in range(n):
        total += math.comb(cards, x) * ((99.2/100) ** (cards-x)) * ((0.8/100) ** x)
        x+=1
    print('Chance around:', round((1-total)*100,2), "%")