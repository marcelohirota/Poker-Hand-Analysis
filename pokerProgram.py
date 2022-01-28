from pathlib2 import Path
import pandas as pd
from handAnalysis import poker

# prepare data to be load to the dataframe, adding ',' to  the empty spaces
path = Path('poker-hands.txt')
text = path.read_text()
text = text.replace(' ', ',')
path.write_text(text)


df = pd.read_csv('poker-hands.txt', header=None)

# dividing the dataframe in 2, first 5 components will be player 1 hand 
# and the rest will be player 2 hand
player1 = df.iloc[:, 0:5]
player2 = df.iloc[:, 5:10]

play1_wins = 0
play2_wins = 0
check1=[]
check2=[]
checkResult=[]

# checking each hand given and calling the analysis function
for i in range(df.shape[0]):
    # Appending the cards of each player into a list
    player1_hand = player1.loc[i, :].values.tolist()
    player2_hand = player2.loc[i, :].values.tolist()
    # Calling the analysis function
    result = poker([player1_hand, player2_hand])
    
    if result == player1_hand:
        play1_wins += 1
    else:
        play2_wins += 1

# Printing the result
print('Player 1 won: {} hands'.format(play1_wins))
print('Player 2 won: {} hands'.format(play2_wins))