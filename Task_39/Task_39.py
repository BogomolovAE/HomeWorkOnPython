# 39(2). Создайте программу для игры в ""Крестики-нолики"". Игра реализуется в терминале,
# игроки ходят поочередно, необходимо вывести карту(как удобнее, можно например в виде 
# списка, внутри которого будут 3 списка по 3 элемента, каждый из которого обозначает 
# соответсвующие клетки от 1 до 9), сделать проверку не занята ли клетка, на которую
# мы хотим поставить крестик или нолик, и проверку на победу( стоят ли крестики или 
# нолик в ряд по диагонали, вертикали, горизонтали)
from graphics import *
class Game:


    def __init__(self,gridsize) :
        self.gridSize=gridsize
        self.grid=[]
        self.currentPlayer=0
        self.round=1        
        self.display=Display(self)
        self.winCondition=3 #number of cells that must be filled with symbol to win
    #Players
        self.player1=Player(self.display.player1Color,"Cross".lower(),self.display,input('Insert name of Player 1: '))
        self.player2=Player(self.display.player2Color,"Circle",self.display,input('Insert name of Player 2: '))
        self.display.ShowNames(self)
        self.currentPlayer=self.player1
        self.NewRound()  


    def ChangePlayer(self):
        if self.currentPlayer==self.player1:
            self.currentPlayer=self.player2
        else: self.currentPlayer=self.player1 


    def Action(self,event):
        if event == "Return" and  self.grid[self.display.currentSelection['y']][self.display.currentSelection['x']].symbol==0:
            self.numberOfTurn+=1
            self.grid[self.display.currentSelection['y']][self.display.currentSelection['x']].Fill(self)

            if self.WinCheck():
                self.currentPlayer.AddScore(self)
                self.display.window.getKey()
                self.RemoveFinishLine()
                self.round+=1
                self.ChangePlayer()
                self.NewRound()
                self.Play()
            self.ChangePlayer()
            
            self.grid[self.display.currentSelection['y']][self.display.currentSelection['x']].Select(self)
            if self.numberOfTurn==self.gridSize**2:
                self.display.window.getKey()
                self.round+=1
                self.NewRound()
                self.Play()
 
        else: self.Move(event)
        self.Play()
 

    def NewRound(self):
        self.numberOfTurn=0

    #Object Deleting
        if len(self.grid)>0:
            for i in range(self.gridSize-1,-1,-1):
                for j in range(self.gridSize-1,-1,-1):
                    del self.grid[i][j]
            self.display.Close()      
            self.display=Display(self)
            self.display.ShowNames(self)
        self.display.currentSelection={'x':0,'y':0}

    #Game Field erasing
        while len(self.grid)>0: 
            self.grid.pop()

    #Creatiing new Game Field
        for i in range(self.gridSize):
            self.grid.append([])
            for j in range(self.gridSize):
                    self.grid[i].append(Cell(Point(self.display.firstCellCoordinate[0]+j*self.display.cellSize,
                                                    self.display.firstCellCoordinate[1]+i*self.display.cellSize),
                                                Point(self.display.firstCellCoordinate[0]+(j+1)*self.display.cellSize,
                                                    self.display.firstCellCoordinate[1]+(i+1)*self.display.cellSize),
                                                self.display))
        
        self.grid[self.display.currentSelection['y']][self.display.currentSelection['x']].Unselect(self.display)
        self.grid[self.display.currentSelection['y']][self.display.currentSelection['x']].Select(self)
 

    def Move(self, event):
        self.grid[self.display.currentSelection['y']][self.display.currentSelection['x']].Unselect(self.display)
        if event== "Right":
            self.display.currentSelection['x']+=1
        if  self.display.currentSelection['x']>=len(self.grid[self.display.currentSelection['y']]):
                self.display.currentSelection['x']=0
        elif event== "Left":
            self.display.currentSelection['x']-=1
            if  self.display.currentSelection['x']<0:
                self.display.currentSelection['x']=len(self.grid[self.display.currentSelection['y']])-1
        elif event== "Down":
                self.display.currentSelection['y']+=1
                if  self.display.currentSelection['y']>=len(self.grid):
                    self.display.currentSelection['y']=0
        elif event== "Up":
                self.display.currentSelection['y']-=1
                if  self.display.currentSelection['y']<0:
                    self.display.currentSelection['y']=len(self.grid)-1  
        self.grid[self.display.currentSelection['y']][self.display.currentSelection['x']].Select(self)
 

    def Play(self):
        self.Action(self.display.window.getKey())
            
 
    def WinCheck(self):
        numberOfSymbol=0

    # Row (for last filled symbol)
        for x in range(0,len(self.grid[self.display.currentSelection['y']])):
            if type(self.grid[self.display.currentSelection['y']][x].symbol)==type(self.currentPlayer.marker):
                numberOfSymbol+=1
            else:
                # numberOfSymbol=0
                break
        if numberOfSymbol==self.gridSize or numberOfSymbol==self.winCondition:
            self.DrawFinishLine(1)
            return True
        
        numberOfSymbol=0 
    # Column (for last filled symbol)
        for y in range(0,len(self.grid)):
            if type(self.grid[y][self.display.currentSelection['x']].symbol)==type(self.currentPlayer.marker):
                numberOfSymbol+=1
            else:
                # numberOfSymbol=0
                break
        if numberOfSymbol==self.gridSize or numberOfSymbol==self.winCondition:
            self.DrawFinishLine(2)
            return True
 
        numberOfSymbol=0
    # First digonal
        if self.display.currentSelection['x']==self.display.currentSelection['y']:
            for j in range(len(self.grid)):
                if type(self.grid[j][j].symbol)==type(self.currentPlayer.marker):
                    numberOfSymbol+=1
                else:
                    # numberOfSymbol=0
                    break
            if numberOfSymbol==self.gridSize or numberOfSymbol==self.winCondition:
                self.DrawFinishLine(3)
                return True  
 
        numberOfSymbol=0
    # Second digonal
        if self.display.currentSelection['y']==self.gridSize-1-self.display.currentSelection['x']:
            for y in range(len(self.grid)):
                if type(self.grid[y][len(self.grid)-1-y].symbol)==type(self.currentPlayer.marker):
                    numberOfSymbol+=1
                else:
                    # numberOfSymbol=0
                    break
            if numberOfSymbol==self.gridSize or numberOfSymbol==self.winCondition:
                self.DrawFinishLine(4)
                return True  
        return False
 

    def DrawFinishLine(self,type):
        if type==1:
            self.line=Line(Point(self.display.firstCellCoordinate[0]-self.display.taleSize,
                            (2*self.display.currentSelection['y']+1)*self.display.cellSize//2
                            +self.display.firstCellCoordinate[1]),
                      Point(self.display.firstCellCoordinate[0]+self.gridSize*self.display.cellSize+self.display.taleSize,
                            (2*self.display.currentSelection['y']+1)*self.display.cellSize//2
                            +self.display.firstCellCoordinate[1]))
            self.line=Line(Point(self.display.firstCellCoordinate[0]-self.display.taleSize,
                            (2*self.display.currentSelection['y']+1)*self.display.cellSize//2
                            +self.display.firstCellCoordinate[1]),
                      Point(self.display.firstCellCoordinate[0]+self.gridSize*self.display.cellSize+self.display.taleSize,
                            (2*self.display.currentSelection['y']+1)*self.display.cellSize//2
                            +self.display.firstCellCoordinate[1]))            
            
        elif type==2:
            self.line=Line(Point((2*self.display.currentSelection['x']+1)*self.display.cellSize//2
                            +self.display.firstCellCoordinate[0],
                            self.display.firstCellCoordinate[1]-self.display.taleSize),
                     Point((2*self.display.currentSelection['x']+1)*self.display.cellSize//2
                            +self.display.firstCellCoordinate[0],
                            self.display.firstCellCoordinate[1]+self.gridSize*self.display.cellSize+self.display.taleSize))
          
        elif type==3:
            self.line=Line(Point(self.display.firstCellCoordinate[0]-round(2**0.5/2)*self.display.taleSize,
                            self.display.firstCellCoordinate[1]-round(2**0.5/2)*self.display.taleSize),
                      Point(self.display.firstCellCoordinate[0]+round(2**0.5/2)*self.display.taleSize+self.gridSize*self.display.cellSize,
                            self.display.firstCellCoordinate[1]+round(2**0.5/2)*self.display.taleSize+self.gridSize*self.display.cellSize))            
 
        else:
            self.line=Line(Point(self.display.firstCellCoordinate[0]+round(2**0.5/2)*self.display.taleSize+self.gridSize*self.display.cellSize,
                            self.display.firstCellCoordinate[1]-round(2**0.5/2)*self.display.taleSize),
                      Point(self.display.firstCellCoordinate[0]-round(2**0.5/2)*self.display.taleSize,
                            self.display.firstCellCoordinate[1]+round(2**0.5/2)*self.display.taleSize+self.gridSize*self.display.cellSize))            
 
        self.line.draw(self.display.window)
 
 
    def RemoveFinishLine(self):
        self.line.undraw()

        
        
class Display():
    def __init__(self,game):
        self.cellSize=50
        self.symbolSize=self.cellSize//3
        self.symbolBorder=2
        self.defaultBorderWidth=1
        self.defaultBorderColor="black" 
        self.selectionBorderWidth=3
        self.player1Color="red"
        self.player2Color="blue"
        self.returnSize=20 
        self.taleSize=7
        self.labelText="Cross-Circles. Game № "+str(game.round)
        self.window=GraphWin("New Game", 400+self.cellSize*(game.gridSize-3),
                                         300+self.cellSize*(game.gridSize-3))
        self.firstCellCoordinate=((self.window.width-self.cellSize*game.gridSize)//2,60) #x,y
        label = Text(Point( self.firstCellCoordinate[0]+game.gridSize*self.cellSize//2, 
                            self.firstCellCoordinate[1]//2), self.labelText)
        label.draw(self.window)
    def ShowNames(self,gameproperties):
            gameproperties.player1.Show_Name(Point(self.firstCellCoordinate[0]//2,self.firstCellCoordinate[1]),self)
    
            gameproperties.player2.Show_Name(Point(3*self.firstCellCoordinate[0]//2+gameproperties.gridSize*
                                        self.cellSize,self.firstCellCoordinate[1]),self)
    def Close(self):
        self.window.close()


    
class Player():
    def __init__(self,playerColor,playerMarker,gameProperties,Name):
        self.color=playerColor
        self.nameText=Name
        if playerMarker=='Cross'.lower():
            self.marker=GameCross((40,40),gameProperties)
            self.nameText+=" (X)"
        else:
            self.marker=GameCircle((40,40),gameProperties)
            self.nameText+=" (O)"
        self.scoreValue=0
 

    def get_Color(self):
        return self.color
 

    def get_Marker(self):
        return self.marker
 

    def Show_Name(self,point,gameProperties):
        self.point=point
        self.name=Text(point,self.nameText)
        self.name.setTextColor(self.color)
        self.name.draw(gameProperties.window)
        self.score=Text(Point(self.point.x,self.point.y+gameProperties.returnSize),self.scoreValue)
        self.score.setTextColor(self.color)
        self.score.draw(gameProperties.window)
 

    def AddScore(self,gameProperties):
        self.score.undraw()
        self.scoreValue+=1
        self.score.setText(self.scoreValue)
        self.score.draw(gameProperties.display.window)
 


class Cell(Rectangle):
    def __init__(self,Point1,Point2,gameProperties):
        super().__init__(Point1,Point2)        
        super().setOutline(gameProperties.defaultBorderColor)
        super().setWidth(gameProperties.defaultBorderWidth)
        super().draw(gameProperties.window)
        self.point1=Point1
        self.point2=Point2
        self.symbol=0
        self.midlePoint=(self.point1.x+gameProperties.cellSize//2,self.point1.y+gameProperties.cellSize//2)
   
 
    def Select(self,gameProperties):
        self.undraw()
        self.setOutline(gameProperties.currentPlayer.color)
        self.setWidth(gameProperties.display.selectionBorderWidth)
        self.draw(gameProperties.display.window)
 

    def Unselect(self,gameProperties):
        #unselection function
        self.undraw()
        self.setOutline(gameProperties.defaultBorderColor)
        self.setWidth(gameProperties.defaultBorderWidth)
        self.draw(gameProperties.window)
 

    def Fill(self,gameProperties):
        self.symbol=gameProperties.currentPlayer.marker.__class__(self.midlePoint,gameProperties.display)
        self.symbol.draw(gameProperties.display.window)
        
 

class GameCross ():
# delete int()
    def __init__(self, point,gameProperties):
        self.line1=Line(Point(point[0]-int(round(gameProperties.symbolSize*2**(0.5)/2)),
                              point[1]-int(round(gameProperties.symbolSize*2**(0.5)/2))),
                        Point(point[0]+int(round(gameProperties.symbolSize*2**(0.5)/2)),
                              point[1]+int(round(gameProperties.symbolSize*2**(0.5)/2))))
        self.line2=Line(Point(point[0]-int(round(gameProperties.symbolSize*2**(0.5)/2)),
                              point[1]+int(round(gameProperties.symbolSize*2**(0.5)/2))),
                        Point(point[0]+int(round(gameProperties.symbolSize*2**(0.5)/2)),
                              point[1]-int(round(gameProperties.symbolSize*2**(0.5)/2))))
    
    def draw (self,window):
        self.line1.draw(window)
        self.line2.draw(window)
 
class GameCircle(Circle):
    def __init__(self,point,gameProperties):
        super().__init__(Point(point[0],point[1]),gameProperties.symbolSize)
 
# win = GraphWin("new window", 400, 300)
game=Game(int(input("Input size of field: ")))
game.Play()
# propertys
 
 
