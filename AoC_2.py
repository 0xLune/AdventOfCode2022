import re

data = re.split('\n| ', open('/home/charles/Bureau/AoC_2_input.txt', 'r').read())

myPlays=[]
opponentPlays=[] 
myScore = 0
myRealScore = 0

for i in range(len(data)):
    if (i % 2) == 0:
        opponentPlays.append(data[i])
    else:
        myPlays.append(data[i])
    
del opponentPlays[len(opponentPlays)-1]

for i in range(len(myPlays)):
    if (myPlays[i] == 'X') and (opponentPlays[i] == 'A'):
        myScore=myScore+1+3
    elif (myPlays[i] == 'Y') and (opponentPlays[i] == 'A'):
        myScore=myScore+2+6
    elif (myPlays[i] == 'Z') and (opponentPlays[i] == 'A'):
        myScore=myScore+3+0
    elif (myPlays[i] == 'X') and (opponentPlays[i] == 'B'):
        myScore=myScore+1+0
    elif (myPlays[i] == 'Y') and (opponentPlays[i] == 'B'):
        myScore=myScore+2+3
    elif (myPlays[i] == 'Z') and (opponentPlays[i] == 'B'):
        myScore=myScore+3+6
    elif (myPlays[i] == 'X') and (opponentPlays[i] == 'C'):
        myScore=myScore+1+6
    elif (myPlays[i] == 'Y') and (opponentPlays[i] == 'C'):
        myScore=myScore+2+0
    elif (myPlays[i] == 'Z') and (opponentPlays[i] == 'C'):
        myScore=myScore+3+3

print(myScore)

for i in range(len(myPlays)):
    if (myPlays[i] == 'X') and (opponentPlays[i] == 'A'):
        myRealScore=myRealScore+0+3
    elif (myPlays[i] == 'Y') and (opponentPlays[i] == 'A'):
        myRealScore=myRealScore+3+1
    elif (myPlays[i] == 'Z') and (opponentPlays[i] == 'A'):
        myRealScore=myRealScore+6+2
    elif (myPlays[i] == 'X') and (opponentPlays[i] == 'B'):
        myRealScore=myRealScore+0+1
    elif (myPlays[i] == 'Y') and (opponentPlays[i] == 'B'):
        myRealScore=myRealScore+3+2
    elif (myPlays[i] == 'Z') and (opponentPlays[i] == 'B'):
        myRealScore=myRealScore+6+3
    elif (myPlays[i] == 'X') and (opponentPlays[i] == 'C'):
        myRealScore=myRealScore+0+2
    elif (myPlays[i] == 'Y') and (opponentPlays[i] == 'C'):
        myRealScore=myRealScore+3+3
    elif (myPlays[i] == 'Z') and (opponentPlays[i] == 'C'):
        myRealScore=myRealScore+6+1

print(myRealScore)

