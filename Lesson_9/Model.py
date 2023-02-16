import View
gameStatus='stop'
def GameRestart():
    global candys,maxCandyInTurn,currentPlayerNumber,gameStatus

    candys=221
    maxCandyInTurn=28
    currentPlayerNumber=1
    gameStatus='stop'

def GetCandys():
    return candys

def GetGameStatus():
    return gameStatus

def GameStart(gameWithHuman,message):
    GameRestart()
    global gameType,gameStatus
    gameStatus='proceed'
    gameType=gameWithHuman
    View.PrintMessage(message,f"Game rules: There is a {candys} candys on the table. Two players are playing making a move after each other. The first move is determined by random. In one move, you can pick up no more than {maxCandyInTurn} candies. All the opponent's candies go to the one who made the last move.")
    
    View.PrintMessage(message,f"Its turn of player №{currentPlayerNumber}")


def GameContinue(message):
    global candys,maxCandyInTurn,currentPlayerNumber
    if gameType==1:
        GameWithHuman(message)
    else:
        GameWithAI(message)

        
        
def GameWithHuman(message):
    global candys,maxCandyInTurn,currentPlayerNumber
    while True:
        try:
            currentCandys=int(message.text)
            break
        except Exception:
            View.PrintMessage(message,"You must input an integer number, try again")
            return 0
    if currentCandys>maxCandyInTurn:
        View.PrintMessage(message,"You must input an integer less than 29, try again")
        return 0
    else:
        candys-=currentCandys

        if candys<1:
            View.PrintMessage(message,f"Player №{currentPlayerNumber} WIN!")
            GameRestart()
            return 0
        View.PrintMessage(message,f"{candys} candys remain")
        if currentPlayerNumber==1: 
            currentPlayerNumber=2
        else: 
            currentPlayerNumber=1
        View.PrintMessage(message,f"Its turn of player №{currentPlayerNumber}")
        return currentCandys


def GameWithAI(message):
    global candys,maxCandyInTurn,currentPlayerNumber
    if GameWithHuman(message)==0:
        return
    currentCandys=candys-(maxCandyInTurn+1)*(candys//(maxCandyInTurn+1))
    candys-=currentCandys
    View.PrintMessage(message,f"Computer takes {currentCandys} -------> {candys} candys remain")   
    if candys<1:
        View.PrintMessage(message,f"Computer WIN!")
        GameRestart()
        return






