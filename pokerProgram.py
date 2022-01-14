from pathlib2 import Path
import pandas as pd
from handAnalysis import poker

path = Path('poker-hands.txt')
text = path.read_text()
text = text.replace(' ', ',')
path.write_text(text)

df = pd.read_csv('poker-hands.txt', header=None)

player1 = df.iloc[:, 0:5]
player2 = df.iloc[:, 5:10]

play1_wins = 0
play2_wins = 0
check1=[]
check2=[]
checkResult=[]
for i in range(df.shape[0]):
    player1_hand = player1.loc[i, :].values.tolist()
    player2_hand = player2.loc[i, :].values.tolist()
    result = poker([player1_hand, player2_hand])
    if result == player1_hand:
        play1_wins += 1
    else:
        play2_wins += 1

print('Player 1 won: {}'.format(play1_wins))
print('Player 2 won: {}'.format(play2_wins))