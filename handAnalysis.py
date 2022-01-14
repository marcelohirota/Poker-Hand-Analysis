def poker(hands):
    scores = [(i, score(hand)) for i, hand in enumerate(hands)]
    winner = sorted(scores , key=lambda x:x[1])[-1][0]
    return hands[winner]
    
def score(hand):
    values = '23456789TJQKA'
    rcounts = {values.find(r): ''.join(hand).count(r) for r, nsuit in hand}.items()
    score, values = zip(*sorted((cnt, rank) for rank, cnt in rcounts)[::-1])
    if len(score) == 5:
        if values[0:2] == (12, 3): 
            values = (3, 2, 1, 0, 1)
        straight = values[0] - values[4] == 4 # same suit
        flush = len({suit for nsuit, suit in hand}) == 1 # same suit
        score = ([(1,), (3,1,1,1)], [(3,1,1,2), (5,)])[flush][straight]
        
    return score, values