#################################################
# 15-112-n19: TERM PROJECT CODE
# Your Name: Zachary Zheng
# Your Andrew ID: zacharyz
# Your Section: C
#################################################

import random
import math

#################################################

#ALL THE CLASSES FOR THE GAME

#################################################

#helps draw the moving red and white edge line on the sides of the road
class SideRoad(object):
    def __init__(self, data, edge, color):
        self.edgeLen = data.height / 20
        self.edgeWidth = data.width / 60
        self.cx = (data.width / 4) - (self.edgeWidth / 2)
        self.cy = (self.edgeLen / 2) + edge * (self.edgeLen)
        self.speed = 20
        self.color = color
        
    def move(self):
        self.cy += self.speed
        
    def draw(self, canvas, data):
        x0 = self.cx - self.edgeWidth / 2
        y0 = self.cy - self.edgeLen / 2
        x1 = self.cx + self.edgeWidth / 2
        y1 = self.cy + self.edgeLen / 2
        canvas.create_rectangle(x0, y0, x1, y1, fill = self.color, width = 0)
        canvas.create_rectangle(x0 + self.edgeWidth + data.width / 2, y0, \
        x1 + self.edgeWidth + data.width / 2, y1, fill = self.color, width = 0)

#helps draw the lanes on the road
class Lane(object):
    def __init__(self, data, lane):
        self.laneLen = data.height / 8
        self.laneWidth = data.width / 60
        self.cx = data.width / 4 + data.width / 6
        self.cy = (self.laneLen / 2) + lane * (self.laneLen)
        self.speed = 20
    
    def move(self):
        self.cy += self.speed
        
    def draw(self, canvas, data):
        x0 = self.cx - self.laneWidth / 2
        y0 = self.cy - self.laneLen / 2
        x1 = self.cx + self.laneWidth / 2
        y1 = self.cy + self.laneLen / 2
        canvas.create_rectangle(x0, y0, x1, y1, fill = "white", width = 0)
        canvas.create_rectangle(x0 + self.laneWidth + data.width / 6, y0, \
        x1 + self.laneWidth + data.width / 6, y1, fill = "white", width = 0)
 
#helps draw the tree animations on the right and left of the screen
class RightTree(object):
    def __init__(self, data, tree, cx):
        treeDist = data.height / 4
        self.cx = cx
        self.cy = data.width * (6 / 64) + tree * treeDist
        self.r = data.width / 24 
        self.speed = 20  
    
    def move(self):
        self.cy += self.speed
        
    def draw(self, canvas, data):
        x0, y0 = self.cx - self.r, self.cy - self.r
        x1, y1 = self.cx + self.r, self.cy + self.r
        x2, y2 = self.cx - self.r / 2, self.cy + self.r / 2
        x3, y3 = self.cx + self.r / 2, self.cy + self.r + data.width / 64
        canvas.create_rectangle(x2, y2, x3, y3, fill = "brown", width = 0)
        canvas.create_oval(x0, y0, x1, y1, fill = "lime green", width = 0)
        
class LeftTree(object):
    def __init__(self, data, tree, cx):
        treeDist = data.height / 4
        self.cx = cx
        self.cy = data.width * (6 / 64) + tree * treeDist
        self.r = data.width / 24 
        self.speed = 20  
    
    def move(self):
        self.cy += self.speed
        
    def draw(self, canvas, data):
        x0, y0 = self.cx - self.r, self.cy - self.r
        x1, y1 = self.cx + self.r, self.cy + self.r
        x2, y2 = self.cx - self.r / 2, self.cy + self.r / 2
        x3, y3 = self.cx + self.r / 2, self.cy + self.r + data.width / 64
        canvas.create_rectangle(x2, y2, x3, y3, fill = "brown", width = 0)
        canvas.create_oval(x0, y0, x1, y1, fill = "lime green", width = 0)

#main class for the car that the user uses in the game
class Car(object):
    #takes in it's center location and it's current condition
    def __init__(self, data, cx, cy):
        self.cx = cx
        self.cy = cy
        self.speedX = 20
        self.speedY = 0
        self.health = 100
        self.bar = data.width / 12
        self.isInvincible = False
        self.isHealth = False
        self.isSlow = False
        self.isFuel = False
        
    def moveLeft(self):
        self.cx -= self.speedX
    
    def moveRight(self):
        self.cx += self.speedX
        
    def move(self):
        self.cy += self.speedY
        
    def drawMain(self, canvas, data):
        x0, y0 = self.cx - data.width / 24, self.cy - data.width / 24
        x1, y1 = x0 + data.width / 192, self.cy - data.width * (3 / 64)
        x2, y2 = self.cx + data.width / 24 - data.width / 192, y1
        x3, y3 = self.cx + data.width / 24, y0
        x4, y4 = x3, y3 + data.width / 12
        x5, y5 = x2, y2 + data.width * (3 / 32)
        x6, y6 = x1, y1 + data.width * (3 / 32)
        x7, y7 = x0, y0 + data.width / 12 
        canvas.create_polygon(x0, y0, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, \
        x6, y6, x7, y7, fill = "red", width = 0)
      
    def drawWindows(self, canvas, data):
        x0, y0 = self.cx - data.width / 30 + data.width / 192, self.cy
        x1, y1 = x0, y0 - data.width / 96
        x2, y2 = x1 + data.width / 96, y1 - data.width / 96
        x3, y3 = self.cx + data.width / 30 - data.width / 192 - data.width \
        / 96, y2
        x4, y4 = self.cx + data.width / 30 - data.width / 192, y1
        x5, y5 = x4, self.cy
        canvas.create_polygon(x0, y0, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, \
        fill = "light blue")
        x6, y6 = x0, self.cy + data.width / 48
        x7, y7 = x2, y6 + data.width / 96
        x8, y8 = x3, y7
        x9, y9 = x5, y6
        canvas.create_polygon(x6, y6, x7, y7, x8, y8, x9, y9, fill = \
        "light blue")
         
    def drawTires(self, canvas, data):
        canvas.create_rectangle(self.cx - data.width / 24 - data.width / 200, \
        self.cy - data.width / 32, self.cx - data.width /24, self.cy - \
        data.width / 64, fill = "black")
        canvas.create_rectangle(self.cx + data.width / 24 , self.cy - \
        data.width / 32, self.cx + data.width /24 + data.width / 200, \
        self.cy - data.width / 64, fill = "black")
        canvas.create_rectangle(self.cx + data.width / 24 + data.width / 200, \
        self.cy + data.width / 32, self.cx + data.width /24, self.cy + \
        data.width / 64, fill = "black")
        canvas.create_rectangle(self.cx - data.width / 24 , self.cy + \
        data.width / 32, self.cx - data.width /24 - data.width / 200, \
        self.cy + data.width / 64, fill = "black")
        
    def drawHeadlights(self, canvas, data):
        x0, y0 = self.cx - data.width / 30, self.cy - data.width * (3 / 64)
        x1, y1 = x0 + data.width / 64, y0 + data.width / 200
        x2, y2 = self.cx + data.width / 30, self.cy - data.width * (3 / 64)
        x3, y3 = x2 - data.width / 64, y2 + data.width / 200
        canvas.create_rectangle(x0, y0, x1, y1, fill = "light blue", width = 0)
        canvas.create_rectangle(x2, y2, x3, y3, fill = "light blue", width = 0)
    
    def drawHealthBar(self, canvas, data):
        if data.mode == "endless":
            x0, y0 = self.cx - data.width / 24, self.cy - data.width / 14
            x1, y1 = self.cx + data.width / 24, self.cy - data.width / 16
            canvas.create_rectangle(x0, y0, x1, y1, width = 2)
            if self.bar / (x1 - x0) >= 0.6:
                color = "green"
            elif self.bar / (x1 - x0) >= 0.3:
                color = "yellow"
            else:
                color = "red"
            canvas.create_rectangle(x0 + 1, y0 + 1, x0 + self.bar, y1 - 1, 
            fill = color, width = 0)

    def draw(self, canvas, data):
        self.drawMain(canvas, data)
        self.drawWindows(canvas, data)
        self.drawTires(canvas, data)
        self.drawHeadlights(canvas, data)
        self.drawHealthBar(canvas, data)
    
#inherits from the main car class and helps identify the moving obstacle cars
class ObstacleCar(Car):
    def __init__(self, data, cx, cy):
        super().__init__(data, cx, cy)
        self.speedX = random.randint(-1, 1)
        self.speedY = random.randint(data.levelSpd, data.levelSpd + 10)
        self.color = random.choice(["blue", "purple", "yellow", "green"])
        
    def move(self):
        self.cx += self.speedX
        self.cy += self.speedY

    def drawMain(self, canvas, data):
        x0, y0 = self.cx - data.width / 24, self.cy - data.width / 24
        x1, y1 = x0 + data.width / 192, self.cy - data.width * (3 / 64)
        x2, y2 = self.cx + data.width / 24 - data.width / 192, y1
        x3, y3 = self.cx + data.width / 24, y0
        x4, y4 = x3, y3 + data.width / 12
        x5, y5 = x2, y2 + data.width * (3 / 32)
        x6, y6 = x1, y1 + data.width * (3 / 32)
        x7, y7 = x0, y0 + data.width / 12 
        canvas.create_polygon(x0, y0, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, \
        x6, y6, x7, y7, fill = self.color, width = 0)
        
    def draw(self, canvas, data):
        self.drawMain(canvas, data)
        self.drawWindows(canvas, data)
        self.drawTires(canvas, data)
        self.drawHeadlights(canvas, data)
        
#class that helps create the coins on the road during the endless mode        
class Coin(object):
    def __init__(self, data, cx, cy):
        self.cx = cx
        self.cy = cy
        self.speed = 15
        self.innerR = data.width / 32
        self.outerR = data.width / 24
        #different point values have different chances of being generated
        self.randomAmount = random.choice([10, 10, 10, 10, 25, 25, 25, 50, 50, \
        100])
        
    def move(self):
        self.cy += self.speed
        
    def draw(self, canvas):
        canvas.create_oval(self.cx - self.outerR, self.cy - self.outerR, \
        self.cx + self.outerR, self.cy + self.outerR, fill = "gold", width = 0)
        canvas.create_oval(self.cx - self.innerR, self.cy - self.innerR, \
        self.cx + self.innerR, self.cy + self.innerR, fill = "goldenrod", 
        width = 0)
        canvas.create_text(self.cx, self.cy, text = "%d" % \
        (self.randomAmount), fill = "gold", font = "Times 20 bold")

#main class that keeps track of all the powerups (blue circles)
class PowerUps(object):
    def __init__(self, data, cx, cy):
        self.cx = cx
        self.cy = cy
        self.speed = 15
        self.innerR = data.width / 32
        self.outerR = data.width / 24
        
    def move(self):
        self.cy += self.speed
        
    def drawOuter(self, canvas, data):
        canvas.create_oval(self.cx - self.outerR, self.cy - self.outerR, \
        self.cx + self.outerR, self.cy + self.outerR, fill = "dodger blue", \
        width = 0)
        canvas.create_oval(self.cx - self.innerR, self.cy - self.innerR, \
        self.cx + self.innerR, self.cy + self.innerR, fill = "blue", 
        width = 0)
 
#invincibility powerup class that inherits from PowerUps       
class Invincibility(PowerUps):
    #reacts to the invincibility powerup by updating the cars status
    def reactToPowerUp(self, data, car):
        if abs(self.cx - car.cx) <= data.width / 24 + self.outerR \
        and abs(self.cy - car.cy) <= data.width * (3 / 64) + \
        self.outerR:
            car.isInvincible = True
            car.isHealth = False
            car.isSlow = False
            data.powerUps.remove(self)
    
    def draw(self, canvas, data):
        self.drawOuter(canvas, data)
        x0, y0 = self.cx - data.width / 64, self.cy - data.width / 64
        x1, y1 = x0 + data.width / 32, y0
        x2, y2 = x1, self.cy + data.width / 128
        x3, y3 = self.cx, self.cy + data.width / 54
        x4, y4 = x0, y2
        canvas.create_polygon(x0, y0, x1, y1, x2, y2, x3, y3, x4, y4, fill = \
        "goldenrod", width = 0)

#health powerup class that inherits from PowerUps     
class Health(PowerUps):
    def reactToPowerUp(self, data, car):
        if abs(self.cx - car.cx) <= data.width / 24 + self.outerR \
        and abs(self.cy - car.cy) <= data.width * (3 / 64) + \
        self.outerR:
            car.isInvincible = False
            car.isHealth = True
            car.isSlow = False
            data.powerUps.remove(self)
    
    def draw(self, canvas, data):
        self.drawOuter(canvas, data)
        x0, y0 = self.cx - data.width / 64, self.cy
        x1, y1 = self.cx + data.width / 64, self.cy
        x2, y2 = self.cx, self.cy - data.width / 64
        x3, y3 = self.cx, self.cy + data.width / 64
        canvas.create_line(x0, y0, x1, y1, fill = "firebrick1", width = 10)
        canvas.create_line(x2, y2, x3, y3, fill = "firebrick1", width = 10)

#time freeze powerup that inherits from PowerUps    
class SlowTime(PowerUps):
    def reactToPowerUp(self, data, car):
        if abs(self.cx - car.cx) <= data.width / 24 + self.outerR \
        and abs(self.cy - car.cy) <= data.width * (3 / 64) + \
        self.outerR:
            car.isInvincible = False
            car.isHealth = False
            car.isSlow = True
            data.powerUps.remove(self)
            
    def draw(self, canvas, data):
        self.drawOuter(canvas, data)
        x0, y0 = self.cx - data.width / 48, self.cy - data.width / 48
        x1, y1 = self.cx + data.width / 48, self.cy + data.width / 48
        x2, y2 = self.cx, self.cy - data.width / 64
        x3, y3 = self.cx, self.cy
        x4, y4 = self.cx, self.cy
        x5, y5 = self.cx + data.width / 64, self.cy
        canvas.create_oval(x0, y0, x1, y1, fill = "white", width = 0)
        canvas.create_oval(x0, y0, x1, y1, width = 5)
        canvas.create_line(x2, y2, x3, y3, fill = "gray", width = 2)
        canvas.create_line(x4, y4, x5, y5, fill = "gray", width = 2)   

#fuel increase for the racing mode that also inherits from PowerUps
class FuelIncrease(PowerUps):
    def reactToFuel(self, data, car):
        if abs(self.cx - car.cx) <= data.width / 24 + self.outerR \
        and abs(self.cy - car.cy) <= data.width * (3 / 64) + \
        self.outerR:
            car.isFuel = True
            data.fuels.remove(self)
            
    def draw(self, canvas, data):
        self.drawOuter(canvas, data)
        x0, y0 = self.cx - data.width / 72, self.cy - data.width / 72
        x1, y1 = self.cx + data.width / 72, self.cy + data.width / 72
        x2, y2 = self.cx + data.width / 108, self.cy - data.width / 108
        x3, y3 = x2 + data.width / 108, y2 - data.width / 108
        canvas.create_line(x2, y2, x3, y3, fill = "gray40", width = 5)
        canvas.create_rectangle(x0, y0, x1, y1, fill = "red", width = 0)

#main class that generates the turns on the racing mode        
class Turn(object):
    def __init__(self, data):
        self.cx = data.width / 2
        self.cy = 0
        self.speed = 20
        self.factor = 0
        
    def move(self):
        self.cy += self.speed
        
    def drawTurnSign(self, canvas, data):
        x = self.cx
        y = self.cy - data.width / 4
        r = data.width / 24
        x0, y0 = x - r / 2, y - (3 / 2) * r
        x1, y1 = x0 + r, y0
        x2, y2 = x + (3 / 2) * r, y - r / 2
        x3, y3 = x2, y2 + r
        x4, y4 = x1, y + (3 / 2) * r
        x5, y5 = x0, y4
        x6, y6 = x - (3 / 2) * r, y3
        x7, y7 = x6, y2
        canvas.create_polygon(x0, y0, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, \
        x6, y6, x7, y7, fill = "red", width = 0)
        canvas.create_text(x, y, text = "TURN", fill = "white", font = \
        "Times 20 bold")
        
#generates the right turns
class Right(Turn):
    def drawRightLanes(self, canvas, data):
        for i in range(20):
            if i % 2 == 0:
                color = "red"
            else:
                color = "white"
            x0, y0 = (self.cx - data.width / 4 - data.width / 60) + i * \
            (data.width / 20), self.cy - data.width / 2 - data.width / 120
            x1, y1 = x0 + data.width / 20, y0
            canvas.create_line(x0, y0, x1, y1, fill = color, width = \
            data.width / 60)
        for i in range(10):
            if i % 2 == 0:
                color = "red"
            else:
                color = "white"
            x0, y0 = (self.cx + data.width /4 + data.width / 60) + i * \
            (data.width / 20), self.cy + data.width / 120
            x1, y1 = x0 + data.width / 20, y0
            canvas.create_line(x0, y0, x1, y1, fill = color, width = \
            data.width / 60)
    
    def draw(self, canvas, data):
        canvas.create_rectangle(self.cx - data.width / 4 - data.width / 60, \
        self.cy - data.height, self.cx + data.width / 2, self.cy - data.width \
        / 2, fill = "cornsilk3", width = 0)
        canvas.create_line(self.cx - data.width / 4 + self.factor, self.cy - \
        data.width / 4 + self.factor, self.cx + data.width - (4 * self.factor) \
        ,self.cy - data.width / 4 - (4 * self.factor), \
        fill = "gray", width = data.width / 2)
        if data.activateTurn == False:
            self.drawRightLanes(canvas, data)
            self.drawTurnSign(canvas, data)
        
#generates the left turns
class Left(Turn):
    def drawLeftLanes(self, canvas, data):
            for i in range(20):
                if i % 2 == 0:
                    color = "red"
                else:
                    color = "white"
                x0, y0 = (self.cx + data.width / 4 + data.width / 60) - i * \
                (data.width / 20), self.cy - data.width / 2 - data.width / 120
                x1, y1 = x0 - data.width / 20, y0
                canvas.create_line(x0, y0, x1, y1, fill = color, width = \
                data.width / 60)
            for i in range(10):
                if i % 2 == 0:
                    color = "red"
                else:
                    color = "white"
                x0, y0 = (self.cx - data.width / 4 - data.width / 20) - i * \
                (data.width / 20), self.cy - data.width / 120
                x1, y1 = x0 + data.width / 20, y0
                canvas.create_line(x0, y0, x1, y1, fill = color, width = \
                data.width / 60)

    def draw(self, canvas, data):
        canvas.create_rectangle(self.cx - data.width / 2, self.cy - \
        data.height, self.cx + data.width / 4 + data.width / 60, self.cy - \
        data.width / 2, fill = "cornsilk3", width = 0)
        canvas.create_line(self.cx + data.width / 4 - self.factor, self.cy - \
        data.width / 4 + self.factor, self.cx - data.width + (4 * \
        self.factor), self.cy - data.width / 4 - (4 * self.factor), fill = \
        "gray", width = data.width / 2)
        if data.activateTurn == False:
            self.drawLeftLanes(canvas, data)
            self.drawTurnSign(canvas, data)
        
        
# CITATION: Animation Starter Code from Course Website:
#https://www.cs.cmu.edu/~112-n19/notes/notes-animations-part2.html

####################################

from tkinter import *

####################################

#creates the white/red side road
def initializeSide(data):
    for i in range(-2, 20):
        if i % 2 == 0:
            color = "red"
        else:
            color = "white"
        data.sideRoads.append(SideRoad(data, i, color))

#creates all the lanes for the road
def initializeLane(data):
    for i in range(-4, 8, 2):
        if i % 2 == 0:
            data.lanes.append(Lane(data, i))

#creates all the trees on the right and left side
def initializeRightTree(data):
    for i in range(-4, 4):
        if i % 2 == 0:
            cx = data.width / 8 - data.width / 24
        else:
            cx = data.width / 8 + data.width / 24
        data.rightTrees.append(RightTree(data, i, cx))
    
def initializeLeftTree(data):
    for i in range(-4, 4):
        if i % 2 == 0:
            cx = data.width * (7 / 8) - data.width / 24
        else:
            cx = data.width * (7 / 8) + data.width / 24
        data.leftTrees.append(LeftTree(data, i, cx))

def initializeSetting(data):
    initializeSide(data)
    initializeLane(data)
    initializeRightTree(data)
    initializeLeftTree(data)

# CITATION: Read and Write File from Course Website:
#https://www.cs.cmu.edu/~112-n19/notes/notes-strings.html#basicFileIO

def readFile(path):
    with open(path, "rt") as f:
        return f.read()

def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)

#helps set up the leaderboard by taking in info from text file        
def setLeaderBoard(data):
    leaderboard = readFile("leaderboard.txt")
    for line in leaderboard.splitlines():
        position = []
        for name in line.split(","):
            position.append(name)
        data.leaderboard.append(position)

# CITATION: Loading Images from Course Website:
#https://www.cs.cmu.edu/~112-n19/notes/notes-animations-demos.html

def loadInstructionImage(data):
    data.instructions = []
    filename = "TP-Images/Instruction.gif"
    data.instructions.append(PhotoImage(file = filename))

#initializes the variables specific to the racing/normal mode
def normalInit(data):
    data.turnDir = []
    data.turn = False
    data.activateTurn = False
    data.score = 0
    data.level = 1
    data.levelSpd = 10
    data.timerFires = 0 
    data.timeElapsed = 0
    data.fuelAngle = math.pi
    data.fuels = []
    data.progressBar = 0

#initializes the variables specific to the endless mode    
def endlessInit(data):
    data.coins = []
    data.powerUps = []
    data.powerUpActive = False
    data.powerUpBar = data.height / 4

#initializes the variables specific to creating the leaderboard
def leaderboardInit(data):
    data.leaderboard = []
    data.leader = False
    data.user = ""
    setLeaderBoard(data)

def init(data):
    data.mode = "splashScreen"
    loadInstructionImage(data)
    data.sideRoads = []
    data.lanes = []
    data.rightTrees = []
    data.leftTrees = []
    initializeSetting(data)
    data.car = Car(data, data.width / 2, data.height - data.width / 9)
    data.obstacleCars = []
    endlessInit(data)
    normalInit(data)
    leaderboardInit(data)
    data.crashed = False
    data.crashTimer = 0
    data.isPaused = False
    data.gameOver = False


#CITATION: Mode Format from Course Website:
#https://www.cs.cmu.edu/~112-n19/notes/notes-animations-demos.html

####################################
# mode dispatcher
####################################

def mousePressed(event, data):
    if (data.mode == "splashScreen"):
        splashScreenMousePressed(event, data)
    elif (data.mode == "endless"):
        endlessMousePressed(event, data)
    elif(data.mode == "normal"):
        normalMousePressed(event, data)
    elif(data.mode == "instruction"):
        instructionMousePressed(event, data)
    elif(data.mode == "leaderboard"):
        leaderboardMousePressed(event, data)

def keyPressed(event, data):
    if (data.mode == "splashScreen"):
        splashScreenKeyPressed(event, data)
    elif (data.mode == "endless"):
        endlessKeyPressed(event, data)
    elif(data.mode == "normal"):
        normalKeyPressed(event, data)
    elif(data.mode == "instruction"):
        instructionKeyPressed(event, data)
    elif(data.mode == "leaderboard"):
        leaderboardKeyPressed(event, data)

def timerFired(data):
    if (data.mode == "splashScreen"):
        splashScreenTimerFired(data)
    elif (data.mode == "endless"):
        endlessTimerFired(data)
    elif(data.mode == "normal"):
        normalTimerFired(data)
    elif(data.mode == "instruction"):
        instructionTimerFired(data)
    elif(data.mode == "leaderboard"):
        leaderboardTimerFired(data)

def redrawAll(canvas, data):
    if (data.mode == "splashScreen"):
        splashScreenRedrawAll(canvas, data)
    elif (data.mode == "endless"):
        endlessRedrawAll(canvas, data)
    elif(data.mode == "normal"):
        normalRedrawAll(canvas, data)
    elif(data.mode == "instruction"):
        instructionRedrawAll(canvas, data)
    elif(data.mode == "leaderboard"):
        leaderboardRedrawAll(canvas, data)

####################################
# splashScreen mode
####################################

#keeps track of which button you press on the home screen and adjusts the mode
def splashScreenMousePressed(event, data):
    if event.x > data.width / 2 - data.width / 8 and event.x < data.width / 2 \
    + data.width / 8 and event.y > data.height / 2 - data.height / 5 + \
    (data.height / 60) * (0 + 1) + data.height * (5 / 48) * 0 and event.y < \
    data.height / 2 - data.height / 5 + (data.height / 60) * (0 + 1) + \
    data.height * (5 / 48) * 1:
        data.mode = "instruction"
    
    elif event.x > data.width / 2 - data.width / 8 and event.x < data.width / 2 \
    + data.width / 8 and event.y > data.height / 2 - data.height / 5 + \
    (data.height / 60) * (1 + 1) + data.height * (5 / 48) * 1 and event.y < \
    data.height / 2 - data.height / 5 + (data.height / 60) * (1 + 1) + \
    data.height * (5 / 48) * 2:
        data.mode = "normal"
        
    elif event.x > data.width / 2 - data.width / 8 and event.x < data.width / 2 \
    + data.width / 8 and event.y > data.height / 2 - data.height / 5 + \
    (data.height / 60) * (2 + 1) + data.height * (5 / 48) * 2 and event.y < \
    data.height / 2 - data.height / 5 + (data.height / 60) * (2 + 1) + \
    data.height * (5 / 48) * 3:
        data.mode = "endless"
        
    elif event.x > data.width / 2 - data.width / 8 and event.x < data.width / 2 \
    + data.width / 8 and event.y > data.height / 2 - data.height / 5 + \
    (data.height / 60) * (3 + 1) + data.height * (5 / 48) * 3 and event.y < \
    data.height / 2 - data.height / 5 + (data.height / 60) * (3 + 1) + \
    data.height * (5 / 48) * 4:
        data.mode = "leaderboard"    

def splashScreenKeyPressed(event, data):
    pass

#creates the animated background of the splash screen/menu screen
def splashScreenTimerFired(data):
    moveSide(data)
    moveLane(data)
    moveTrees(data)

#creates the buttons with their appropriate label
def drawButtons(canvas, data):
    for i in range(4):
        x0, y0 = data.width / 2 - data.width / 8, data.height / 2 - \
        data.height / 5 + (data.height / 60) * (i + 1) + data.height * \
        (5 / 48) * i
        x1, y1 = data.width / 2 + data.width / 8, y0 + data.height * (5 / 48)
        canvas.create_rectangle(x0, y0, x1, y1, fill = "gray", width  = 2)
        if i == 0:
            text = "Instructions"
        elif i == 1:
            text = "Race Mode"
        elif i == 2:
            text = "Endless Mode"
        elif i == 3:
            text = "Leaderboard"
        canvas.create_text((x0 + x1) / 2, (y0 + y1) / 2, text = text, fill = \
        "white", font = "Times 23 bold")

def splashScreenRedrawAll(canvas, data):
    drawScenery(canvas, data)
    drawRoad(canvas, data)
    canvas.create_rectangle(data.width / 8, -2, data.width * (7 / 8), \
    data.height / 5, fill = "cadetblue3", width = 5)
    canvas.create_rectangle(data.width / 2 - data.width / 6, data.height / 2 - \
    data.width / 6, data.width / 2 + data.width / 6, data.height / 2 + \
    data.width / 4, fill = "cadetblue3", width = 5)
    canvas.create_text(data.width / 2, data.height / 10, text = \
    "TRAFFIC RUSH", fill = "white", font = "Times 50 bold italic")
    drawButtons(canvas, data)

####################################
# instructions
####################################

def instructionMousePressed(event, data):
    pass
    
def instructionKeyPressed(event, data):
    if event.char == "m":
        init(data)
    
def instructionTimerFired(data):
    moveSide(data)
    moveLane(data)
    moveTrees(data)

#displays the instruction screen with the image that was previously loaded    
def instructionRedrawAll(canvas, data):
    drawScenery(canvas, data)
    drawRoad(canvas, data)
    canvas.create_rectangle(data.width / 8, -2, data.width * (7 / 8), \
    data.height / 5, fill = "cadetblue3", width = 5)
    canvas.create_text(data.width / 2, data.height / 10, text = \
    "TRAFFIC RUSH", fill = "white", font = "Times 50 bold italic")
    cx = data.width / 2
    cy = data.height / 2
    canvas.create_image(cx - 300, cy - 150, anchor=NW, image = \
    data.instructions[0])
    canvas.create_rectangle(cx - 300, cy - 150, cx + 300, cy + 255, width = 5)
   
####################################
# leaderboard
####################################
    
def leaderboardMousePressed(event, data):
    pass
    
def leaderboardKeyPressed(event, data):
    if event.char == "m":
        init(data)
    
def leaderboardTimerFired(data):
    moveSide(data)
    moveLane(data)
    moveTrees(data)    
 
#reads in the data from the text file in order to display content in tkinter
def drawLeaderBoard(canvas, data):
    cx = data.width / 2
    cy = data.height / 2
    canvas.create_rectangle(data.width / 8, -2, data.width * (7 / 8), \
    data.height / 5, fill = "cadetblue3", width = 5)
    canvas.create_text(data.width / 2, data.height / 10, text = \
    "TRAFFIC RUSH", fill = "white", font = "Times 50 bold italic")
    canvas.create_rectangle(cx - 300, cy - 150, cx + 300, cy + 255, fill = \
    "cadetblue3", width = 5)
    canvas.create_line(cx, cy - 150, cx, cy + 255, width = 5)
    canvas.create_text(cx - 150, cy - 120, text = "Racing Mode (sec):", \
    fill = "black", font = "Times 25 bold underline")
    canvas.create_text(cx + 150, cy - 120, text = "Endless Mode:", \
    fill = "black", font = "Times 25 bold underline")
    for i in range(5):
        canvas.create_text(cx - 150, cy - 55 + i * 65, text = "%d) %s: %s" % \
        (i + 1, str(data.leaderboard[i][0]), str(data.leaderboard[i][1])), \
        fill = "black", font = "Times 25 bold")
    for i in range(5, 10):
        canvas.create_text(cx + 150, cy - 55 + (i - 5) * 65, text = \
        "%d) %s: %s" % (i - 4, str(data.leaderboard[i][0]), \
        str(data.leaderboard[i][1])), fill = "black", font = "Times 25 bold")
        
def leaderboardRedrawAll(canvas, data):
    drawScenery(canvas, data)
    drawRoad(canvas, data)
    drawLeaderBoard(canvas, data)

####################################
# endless mode
####################################

def endlessMousePressed(event, data):
    pass

#controls the movement of the car (left and right)
def moveCar(event, data):
    if event.keysym == "Left":
        data.car.moveLeft()
        if data.car.cx < data.width / 4 + data.width / 200 + \
        data.width / 24:
            data.car.cx = data.width / 4 + data.width / 200 + \
        data.width / 24
    elif event.keysym == "Right":
        data.car.moveRight()
        if data.car.cx > (3 / 4) * data.width - data.width / 200 - \
        data.width / 24:
            data.car.cx = (3 / 4) * data.width - data.width / 200 - \
        data.width / 24

#keeps track of all the key presses in endless mode
def endlessKeyPressed(event, data):
    if data.gameOver == False:
        if data.isPaused == False:
            if data.crashed == False:
                moveCar(event, data)
        if event.char == "p":
            data.isPaused = not data.isPaused
    if event.char == "m":
        init(data)

#the three functions below create the animating appearance of the roads/trees
def moveSide(data):
    if data.turn == True and data.turnDir[0].cy <= data.height * (3 / 4):
        edgeLen = data.height / 20
        if data.sideRoads[-1].cy >= data.height + (3 / 2) * edgeLen:
            data.sideRoads = []
            initializeSide(data)
        for sideRoad in data.sideRoads:
            sideRoad.move()
    elif data.turn == False:
        edgeLen = data.height / 20
        if data.sideRoads[-1].cy >= data.height + (3 / 2) * edgeLen:
            data.sideRoads = []
            initializeSide(data)
        for sideRoad in data.sideRoads:
            sideRoad.move()
        
def moveLane(data):
    if data.turn == True and data.turnDir[0].cy <= data.height * (3 / 4):
        laneLen = data.height / 8
        if data.lanes[-1].cy >= data.height + (5 / 2) * laneLen:
            data.lanes = []
            initializeLane(data)
        for lane in data.lanes:
            lane.move()
    elif data.turn == False:
        laneLen = data.height / 8
        if data.lanes[-1].cy >= data.height + (5 / 2) * laneLen:
            data.lanes = []
            initializeLane(data)
        for lane in data.lanes:
            lane.move()

def moveTrees(data):
    if data.turn == True and data.turnDir[0].cy <= data.height * (3 / 4):
        treeDist = data.height / 4
        if data.rightTrees[5].cy >= data.height + (3 / 2) * treeDist:
            data.rightTrees = []
            initializeRightTree(data)
        for rightTree in data.rightTrees:
            rightTree.move()
        if data.leftTrees[5].cy >= data.height + (3 / 2) * treeDist:
            data.leftTrees = []
            initializeLeftTree(data)
        for leftTree in data.leftTrees:
            leftTree.move()
    elif data.turn == False:
        treeDist = data.height / 4
        if data.rightTrees[5].cy >= data.height + (3 / 2) * treeDist:
            data.rightTrees = []
            initializeRightTree(data)
        for rightTree in data.rightTrees:
            rightTree.move()
        if data.leftTrees[5].cy >= data.height + (3 / 2) * treeDist:
            data.leftTrees = []
            initializeLeftTree(data)
        for leftTree in data.leftTrees:
            leftTree.move()

#function that spawns the obstacle cars and moves them with their speeds
def spawnCar(data):
    if data.crashed == False:
        if data.car.isSlow != True:
            if data.timerFires % 50 == 0:
                cx = random.randint(data.width // 4 + data.width // 24, \
                data.width * (3 / 4) - data.width // 24)
                cy = - data.width * (3 / 64)
                data.obstacleCars.append(ObstacleCar(data, cx, cy))
    moveObstacleCars(data)

def moveObstacleCars(data):
    for obstacleCar in data.obstacleCars:
        obstacleCar.move()
        if obstacleCar.cx < data.width / 4 + data.width / 200 + \
        data.width / 24:
            obstacleCar.cx = data.width / 4 + data.width / 200 + \
            data.width / 24
        if obstacleCar.cx > (3 / 4) * data.width - data.width / 200 - \
        data.width / 24:
            obstacleCar.cx = (3 / 4) * data.width - data.width / 200 - \
            data.width / 24
        if obstacleCar.cy >= data.height + data.width * (3 / 64):
            data.obstacleCars.remove(obstacleCar)
            if data.mode == "endless":
                data.score += 10
            else:
                data.score += 1
                data.progressBar = data.progressBar + (data.width / 3) / 50
                if data.progressBar >= data.width / 3 - 2:
                    data.progressBar = data.width / 3 - 2
                    data.leader = True
            data.leader = False
        elif obstacleCar.cy < - data.width * (3 / 64):
            data.obstacleCars.remove(obstacleCar)

#helps check if the user's car makes contact with any of the obstacle cars
def checkCollision(data):
    for obstacleCar in data.obstacleCars:
        if abs(obstacleCar.cx - data.car.cx) <= data.width / 12 and \
        abs(obstacleCar.cy - data.car.cy) <= data.width * (3 / 32):
            if data.car.isInvincible == True:
                data.obstacleCars.remove(obstacleCar)
                data.score += 20
            else:
                data.crashed = True
                #below keeps track of the HP loss and updates the HP bar
                if data.mode == "endless":
                    factor = random.randint(25, 40)
                    hpLoss = factor / 100
                    data.car.bar = data.car.bar - (data.width / 12) * hpLoss
                    if data.car.bar <= 0:
                        data.car.bar = 0
                        data.gameOver = True
                        data.leader = True
                for obstacleCar in data.obstacleCars:
                    obstacleCar.speedX = (obstacleCar.cx - data.car.cx) / 8
                    obstacleCar.speedY = -1 * obstacleCar.speedY                

#function that randomly spawns the coins with random values on the road
def spawnCoin(data):
    if data.crashed == False:
        if data.car.isSlow == True:
            time = 50
        else:
            time = 80
        if data.timerFires % time == 0:
            cx = random.randint(data.width // 4 + data.width // 24, \
            data.width * (3 / 4) - data.width // 24)
            cy = - data.width * (3 / 64)
            data.coins.append(Coin(data, cx, cy))
    for coin in data.coins:
        coin.move()
        if coin.cy >= data.height + data.width * (3 / 64):
            data.coins.remove(coin)
 
#checks if the user's car touches/'collects' the coin
def checkCoinCollision(data):
    for coin in data.coins:
        if abs(coin.cx - data.car.cx) <= data.width / 24 + coin.outerR and \
        abs(coin.cy - data.car.cy) <= data.width * (3 / 64) + coin.outerR:
            data.score += coin.randomAmount
            data.coins.remove(coin)

#function that spawns a random powerup somewhere on the road
def spawnPowerUp(data):
    if data.crashed == False:
        if data.timerFires % 225 == 0:
            cx = random.randint(data.width // 4 + data.width // 24, \
            data.width * (3 / 4) - data.width // 24)
            cy = - data.width * (3 / 64)
            powerType = random.choice([Invincibility(data, cx, cy), \
            Health(data, cx, cy), SlowTime(data, cx, cy)])
            data.powerUps.append(powerType)
    for powerUp in data.powerUps:
        powerUp.move()
        if powerUp.cy >= data.height + data.width * (3 / 64):
            data.powerUps.remove(powerUp)

#increases the HP bar if health powerup collected    
def updateHealth(data):
    factor = random.randint(25, 40)
    hpGain = factor / 100
    data.car.bar = data.car.bar + (data.width / 12) * hpGain
    if data.car.bar >= data.width / 12:
        data.car.bar = data.width / 12
    data.car.isHealth = False    

#checks if the user's car makes contact with any of the powerUps    
def checkPowerUp(data):
    for powerUp in data.powerUps:
        powerUp.reactToPowerUp(data, data.car)
    if data.car.isInvincible == True:
        data.powerUpActive = True
    elif data.car.isHealth == True:
        updateHealth(data)
    elif data.car.isSlow == True:
        data.powerUpActive = True

#function that keeps track of the powerUp timer bar
def powerUpTimer(data):
    data.powerUpBar += data.height / 300
    if data.powerUpBar >= data.height * (3 / 4):
        data.powerUpActive = False
        data.powerUpBar = data.height / 4
        data.car.isInvincible = False
        data.car.isHealth = False
        data.car.isSlow = False

def spawnObjects(data):
    spawnCoin(data)
    spawnPowerUp(data)
 
#keeps track of all the timerFired   
def endlessTimerFired(data):
    if data.gameOver == False:
        if data.isPaused == False:
            data.timerFires += 1
            spawnCar(data)
            #increments the level/difficulty
            if data.timerFires % 500 == 0:
                data.level += 1
                data.levelSpd += 2
            if data.powerUpActive == True:
                powerUpTimer(data)
            #things to do run if car is not crashed
            if data.crashed == False:
                moveSide(data)
                moveLane(data)
                moveTrees(data)
                spawnObjects(data)
                checkCollision(data)
                checkPowerUp(data)
                checkCoinCollision(data)
            #if car is crashed, crash timer is initialized before moving again
            elif data.crashed == True:
                data.crashTimer += 1
                if data.crashTimer % 25 == 0:
                    data.crashed = False
                    for obstacleCar in data.obstacleCars:
                        obstacleCar.speedY = - obstacleCar.speedY

#below are all the draw helper functions to create the scene of the game        
def drawRoad(canvas, data):
    canvas.create_rectangle(data.width / 4, 0, (3 / 4) * data.width, \
    data.height, fill = "gray", width = 0)
    for sideRoad in data.sideRoads:
        sideRoad.draw(canvas, data)
    for lane in data.lanes:
        lane.draw(canvas, data)

def drawScenery(canvas, data):
    edgeWidth = data.width / 60
    canvas.create_rectangle(0, 0, data.width / 4 - edgeWidth, data.height, \
    fill = "cornsilk3", width = 0)
    canvas.create_rectangle((3 / 4) * data.width, 0, data.width, data.height, \
    fill = "cornsilk3", width = 0)
    for rightTree in data.rightTrees:
        rightTree.draw(canvas, data)
    for leftTree in data.leftTrees:
        leftTree.draw(canvas, data)

def drawItems(canvas, data):
    for coin in data.coins:
        coin.draw(canvas)
    for powerUp in data.powerUps:
        powerUp.draw(canvas, data)
    
def drawCars(canvas, data):
    for obstacleCar in data.obstacleCars:
        obstacleCar.draw(canvas, data)

def drawPowerUpBar(canvas, data):
    x0, y0 = data.width / 8 - data.width / 120 - data.width / 32, \
    data.powerUpBar
    x1, y1 = data.width / 8 - data.width / 120 + data.width / 32, \
    data.height * (3 / 4)
    canvas.create_rectangle(x0 - 2, data.height / 4 - 2, x1 + 2, y1 + 2, \
    width = 2)
    canvas.create_rectangle(x0, y0, x1, y1, fill = "IndianRed2", width = 0)
    canvas.create_text((x1 + x0) / 2, data.height / 5, text = "POWERUP TIMER", \
    fill = "white", font = "Times 15 bold")

def drawScore(canvas, data):
    canvas.create_text(data.width * (7 / 8) + data.width / 120, data.height / \
    25, text = "SCORE:", fill = "white", font = "Times 30 bold underline")
    canvas.create_text(data.width * (7 / 8) + data.width / 120, data.height * \
    (3 / 25), text = "%d" % (data.score), fill = "white", font = \
    "Times 30 bold")
    
def drawLevel(canvas, data):
    canvas.create_text(data.width / 8 - data.width / 120, data.height / 25, \
    text = "LEVEL:", fill = "white", font = "Times 30 bold underline")
    canvas.create_text(data.width / 8 - data.width / 120, data.height * \
    (3 / 25), text = "%d" % (data.level), fill = "white", font = \
    "Times 30 bold")

#takes in the username from the Button widget and updates leaderboard from it
def getUserName(data, entry_box):
    data.user = entry_box.get()
    updateEndlessLeaderboard(data)
    reUpdateTextFile(data)
    
# CITATION: User Input Mechanic For Tkinter from Video Online:
#https://www.youtube.com/watch?v=psKTroKLYfs

def endlessGameOver(data):
    root = Tk()
    root.title("HighScore")
    root.geometry("640x450+0+0")
    heading = Label(root, text = "You Made The Leaderboard!", font = ("arial", \
    20, "bold"), fg = "black").pack()
    label1 = Label(root, text = "Enter your name: ", font = ("arial", 15, \
    "bold"), fg = "black").place(x = 10, y = 200)
    entry_box = Entry(root, width = 25, bg = "cadetblue3")
    entry_box.place(x = 280, y = 210) 
    work = Button(root, text = "Enter", width = 30, height = 5, bg = "gray", \
    command = lambda: getUserName(data, entry_box))
    work.place(x = 250, y = 300)

#adjusts each position of the leaderboard if score is high enough    
def updateEndlessLeaderboard(data):
    if data.score > int(data.leaderboard[5][1]):
        for i in range(9, 5, -1):
            data.leaderboard[i][0] = data.leaderboard[i - 1][0]
            data.leaderboard[i][1] = data.leaderboard[i - 1][1]
        data.leaderboard[5][0] = data.user
        data.leaderboard[5][1] = data.score
    elif data.score > int(data.leaderboard[6][1]):
        for i in range(9, 6, -1):
            data.leaderboard[i][0] = data.leaderboard[i - 1][0]
            data.leaderboard[i][1] = data.leaderboard[i - 1][1]
        data.leaderboard[6][0] = data.user
        data.leaderboard[6][1] = data.score
    elif data.score > int(data.leaderboard[7][1]):
        for i in range(9, 7, -1):
            data.leaderboard[i][0] = data.leaderboard[i - 1][0]
            data.leaderboard[i][1] = data.leaderboard[i - 1][1]
        data.leaderboard[7][0] = data.user
        data.leaderboard[7][1] = data.score
    elif data.score > int(data.leaderboard[8][1]):
        data.leaderboard[9][0] = data.leaderboard[8][0]
        data.leaderboard[9][1] = data.leaderboard[8][1]
        data.leaderboard[8][0] = data.user
        data.leaderboard[8][1] = data.score
    elif data.score > int(data.leaderboard[9][1]):
        data.leaderboard[9][0] = data.user
        data.leaderboard[9][1] = data.score

#rewrites the new text file with the updated leaderboard info
def reUpdateTextFile(data):
    content = ""
    for i in range(9):
        content += "%s,%s\n" % (data.leaderboard[i][0], data.leaderboard[i][1])
    content += "%s,%s" % (data.leaderboard[9][0], data.leaderboard[9][1])
    writeFile("leaderboard.txt", content)
    
def drawGameOver(canvas, data):
        canvas.create_rectangle(data.width / 2 - 275, data.height / 2 - 100, \
        data.width / 2 + 275, data.height / 2 + 100, fill = "tomato2", \
        width = 2)
        canvas.create_text(data.width / 2, data.height / 2 - data.height / 16, \
        text = "GAME OVER", fill = "black", font = "Times 30 bold")
        canvas.create_text(data.width / 2, data.height / 2 + data.height / 16, \
        text = "YOUR FINAL SCORE: %d" % (data.score), fill = "black", \
        font = "Times 30 bold")
        if data.score > int(data.leaderboard[9][1]) and data.leader == True:
            endlessGameOver(data)
            data.leader = False

#draws everything needed for the endless mode    
def endlessRedrawAll(canvas, data):
    drawScenery(canvas, data)
    drawRoad(canvas, data)
    drawScore(canvas, data)
    drawLevel(canvas, data)
    drawItems(canvas, data)
    drawCars(canvas, data)
    data.car.draw(canvas, data)
    if data.powerUpActive == True:
        drawPowerUpBar(canvas, data)
    if data.isPaused == True:
        canvas.create_rectangle(data.width / 2 - 150, data.height / 2 - 50, \
        data.width / 2 + 150, data.height / 2 + 50, fill = "cadetblue3", \
        width = 2)
        canvas.create_text(data.width / 2, data.height / 2, text = "PAUSED", \
        fill = "black", font = "Times 50 bold")
    if data.gameOver == True:
        drawGameOver(canvas, data)
        canvas.create_text(data.width / 2, data.height / 2 + data.height / 16, \
        text = "YOUR FINAL SCORE: %d" % (data.score), fill = "black", \
        font = "Times 30 bold")

####################################
# normal/racing mode
####################################
    
def normalMousePressed(event, data):
    pass

#checks if user wants to 'turn' the car at a right/left turn with Space Bar    
def turnCar(event, data):
    if data.turnDir[0].cy <= data.width * (3 / 4) and event.keysym == "space":
        data.activateTurn = True
        data.car.speedY = 5

#keeps track of all the key presses for the normal/racing mode    
def normalKeyPressed(event, data):
    if data.gameOver == False:
        if data.isPaused == False:
            if data.crashed == False:
                moveCar(event, data)
                if data.turn == True:
                    turnCar(event, data)
        if event.char == "p":
            data.isPaused = not data.isPaused
    if event.char == "m":
        init(data)

#spawns the fuel boosts on the road
def spawnFuel(data):
    if data.crashed == False:
        if data.timerFires % 100 == 0:
            cx = random.randint(data.width // 4 + data.width // 24, \
            data.width * (3 / 4) - data.width // 24)
            cy = - data.width * (3 / 64)
            powerType = FuelIncrease(data, cx, cy)
            data.fuels.append(powerType)
    for fuel in data.fuels:
        fuel.move()
        if fuel.cy >= data.height + data.width * (3 / 64):
            data.fuels.remove(fuel)

#checks if the user's car makes contact with the fuel    
def fuelCollision(data):
    for fuel in data.fuels:
        fuel.reactToFuel(data, data.car)
    if data.car.isFuel == True:
        data.fuelAngle += math.pi / 4
        if data.fuelAngle >= math.pi:
            data.fuelAngle = math.pi
        data.car.isFuel = False

#updates the time elapsed and the number of cars passed 
def checkScore(data):
    if data.score >= 50:
        data.car.speedY = -20
    if data.timerFires % 50 == 0 and data.score < 50:
        data.timeElapsed += 1
    if data.turn == False and data.score < 50:
        spawnCar(data)

#reduces the fuel amount over time 
def checkFuel(data):
    data.fuelAngle -= math.pi / 720
    if data.fuelAngle <= 0 and data.score < 50:
        data.gameOver = True

def checkTurn(data):
        if data.turn == False and data.timerFires % 300 == 0:
            spawnTurn(data)
        elif data.turn == True:
            data.obstacleCars = []
            for dir in data.turnDir:
                dir.move()
                if data.activateTurn == False and dir.cy >= data.height * \
                (3 / 4):
                    dir.speed = 0
                    data.car.speedY = -20

#randomly spawns a turn at any particular moment
def spawnTurn(data):
    if data.score < 50:
        turnType = random.choice([Right(data), Left(data)])
        data.turnDir.append(turnType)
        data.turn = True
    
#moves the car up during the 
def moveTheCar(data):
    data.car.move()
    if data.car.cy <= data.height * (3 / 4) - data.width / 2 + \
    data.width / 24 and data.score < 50:
        data.gameOver = True
    if data.car.cy >= data.height - data.width / 9:
        data.car.cy = data.height - data.width / 9
        data.car.speedY = 0

#helps with the 'turning' effect    
def rotateTurn(data):
    if data.activateTurn == True:
        data.turnDir[0].factor += 25
        if data.turnDir[0].factor >= data.width / 4:
            data.turnDir[0].factor = data.width / 4
            data.turn = False
            data.activateTurn = False
            data.turnDir.pop()

#keeps track of all the timer fired for the racing/normal mode    
def normalTimerFired(data):
    if data.gameOver == False:
        if data.isPaused == False:
            data.timerFires += 1
            data.fuelAngle -= math.pi / 2880
            checkFuel(data)
            checkScore(data)
            moveTheCar(data)
            rotateTurn(data)
            if data.crashed == False:
                moveSide(data)
                moveLane(data)
                moveTrees(data)
                checkTurn(data)
                if data.turn == False:
                    spawnFuel(data)
                    checkCollision(data)
                    fuelCollision(data)
            elif data.crashed == True:
                data.crashTimer += 1
                if data.crashTimer % 25 == 0:
                    data.crashed = False
                    for obstacleCar in data.obstacleCars:
                        obstacleCar.speedY = - obstacleCar.speedY

#below draws most of the objects needed to create the scene of the racing mode
def drawTimers(canvas, data):
    canvas.create_text(data.width * (7 / 8) + data.width / 120, data.height / \
    25, text = "TIME:", fill = "white", font = "Times 30 bold underline")
    canvas.create_text(data.width * (7 / 8) + data.width / 120, data.height * \
    (3 / 25), text = "%d" % (data.timeElapsed), fill = "white", font = \
    "Times 30 bold")
    
def drawFuel(canvas, data):
    radius = (data.width - data.width * (3 / 4) - (data.width  / 60)) / 2
    cx, cy = data.width - radius, data.height
    canvas.create_oval(cx - radius, cy - radius, cx + radius, cy + radius, \
    fill = "white", width = 5)
    canvas.create_text(cx - radius + 20, cy - 20, text = "F", font = \
    "Times 25 bold")
    canvas.create_text(cx + radius - 20, cy - 20, text = "E", fill = "red", \
    font = "Times 25 bold")
    canvas.create_line(cx, cy, cx + (radius - 15) * math.cos(data.fuelAngle), \
    cy - (radius - 15) * math.sin(data.fuelAngle), width = 3)    
    
def drawProgressBar(canvas, data):
    x0, y0 = data.width / 2 - data.width / 6, data.height / 12 - data.height \
    / 24
    x1, y1 = data.width / 2 + data.width / 6, data.height / 12 + data.height \
    / 24
    canvas.create_rectangle(x0, y0, x1, y1, width = 2)
    x2, y2 = x0 + 1, y0 + 1
    x3, y3 = x2 + data.progressBar, y1 - 1
    canvas.create_rectangle(x2, y2, x3, y3, fill = "green3", width = 0)

#takes in user input with button widget to update leaderboard (same as endless)
def getNormalUserName(data, entry_box):
    data.user = entry_box.get()
    updateNormalLeaderboard(data)
    reUpdateTextFile(data)
    
# CITATION: User Input Mechanic For Tkinter from Video Online:
#https://www.youtube.com/watch?v=psKTroKLYfs

def normalGameOver(data):
    root = Tk()
    root.title("HighScore")
    root.geometry("640x450+0+0")
    heading = Label(root, text = "You Made The Leaderboard!", font = ("arial", \
    20, "bold"), fg = "black").pack()
    label1 = Label(root, text = "Enter your name: ", font = ("arial", 15, \
    "bold"), fg = "black").place(x = 10, y = 200)
    entry_box = Entry(root, width = 25, bg = "cadetblue3")
    entry_box.place(x = 280, y = 210) 
    work = Button(root, text = "Enter", width = 30, height = 5, bg = "gray", \
    command = lambda: getNormalUserName(data, entry_box))
    work.place(x = 250, y = 300)
    
def updateNormalLeaderboard(data):
    if data.timeElapsed < int(data.leaderboard[0][1]):
        for i in range(4, 0, -1):
            data.leaderboard[i][0] = data.leaderboard[i - 1][0]
            data.leaderboard[i][1] = data.leaderboard[i - 1][1]
        data.leaderboard[0][0] = data.user
        data.leaderboard[0][1] = data.timeElapsed
    elif data.timeElapsed < int(data.leaderboard[1][1]):
        for i in range(4, 1, -1):
            data.leaderboard[i][0] = data.leaderboard[i - 1][0]
            data.leaderboard[i][1] = data.leaderboard[i - 1][1]
        data.leaderboard[1][0] = data.user
        data.leaderboard[1][1] = data.timeElapsed
    elif data.timeElapsed < int(data.leaderboard[2][1]):
        for i in range(4, 2, -1):
            data.leaderboard[i][0] = data.leaderboard[i - 1][0]
            data.leaderboard[i][1] = data.leaderboard[i - 1][1]
        data.leaderboard[2][0] = data.user
        data.leaderboard[2][1] = data.timeElapsed
    elif data.timeElapsed < int(data.leaderboard[3][1]):
        data.leaderboard[4][0] = data.leaderboard[8][0]
        data.leaderboard[4][1] = data.leaderboard[8][1]
        data.leaderboard[3][0] = data.user
        data.leaderboard[3][1] = data.timeElapsed
    elif data.timeElapsed < int(data.leaderboard[4][1]):
        data.leaderboard[4][0] = data.user
        data.leaderboard[4][1] = data.timeElapsed

#creates the message if you finished the course for the racing mode
def normalWin(canvas, data):
    canvas.create_rectangle(data.width / 2 - 300, data.height / 2 - 100, \
    data.width / 2 + 300, data.height / 2 + 100, fill = "yellow2", \
    width = 2)
    canvas.create_text(data.width / 2, data.height / 2 - data.height / 16, \
    text = "CONGRATS, YOU FINISHED!", fill = "black", font = "Times 30 bold")
    canvas.create_text(data.width / 2, data.height / 2 + data.height / 16, \
    text = "YOUR TIME: %d SECONDS" % (data.timeElapsed), fill = "black", \
    font = "Times 30 bold")
    if data.timeElapsed < int(data.leaderboard[4][1]) and data.leader == True:
        normalGameOver(data)
        data.leader = False

def drawNormalGameOver(canvas, data):
    canvas.create_rectangle(data.width / 2 - 275, data.height / 2 - 100, \
    data.width / 2 + 275, data.height / 2 + 100, fill = "tomato2", \
    width = 2)
    canvas.create_text(data.width / 2, data.height / 2 - data.height / 16, \
    text = "GAME OVER", fill = "black", font = "Times 30 bold")
    canvas.create_text(data.width / 2, data.height / 2 + data.height / 16, \
    text = "YOUR DISTANCE: %d%%" % (2 * data.score), fill = \
    "black", font = "Times 30 bold")

#draws everything that's needed for the racing mode
def normalRedrawAll(canvas, data):
    drawScenery(canvas, data)
    drawFuel(canvas, data)
    drawRoad(canvas, data)
    for fuel in data.fuels:
        fuel.draw(canvas, data)
    if data.score < 50:
        drawCars(canvas, data)
    if data.turn == True:
        for turn in data.turnDir:
            turn.draw(canvas, data)
    drawTimers(canvas, data)
    data.car.draw(canvas, data)
    drawProgressBar(canvas, data)
    if data.isPaused == True:
        canvas.create_rectangle(data.width / 2 - 150, data.height / 2 - 50, \
        data.width / 2 + 150, data.height / 2 + 50, fill = "cadetblue3", \
        width = 2)
        canvas.create_text(data.width / 2, data.height / 2, text = "PAUSED", \
        fill = "black", font = "Times 50 bold")
    if data.gameOver == True:
        drawNormalGameOver(canvas, data)
    if data.score >= 50:
        normalWin(canvas, data)

####################################
#Run Function
####################################

# CITATION: Run Function from Course Website:
#https://www.cs.cmu.edu/~112-n19/notes/notes-animations-part2.html

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 10 # milliseconds
    root = Tk()
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(800, 600)