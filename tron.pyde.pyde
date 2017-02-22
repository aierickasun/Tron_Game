"""
Tron
"""
#holds all x and ys taken up.
holdallx = []
holdally = []
class Trons:
    global holdallx
    global holdally
    def __init__(self, positionx, positiony):
        self.positionx = positionx; self.positiony = positiony
        holdallx.append(int(positionx))
        holdally.append(int(positiony))
        return None
    def move(self, direction):
        if direction=='UP':
            self.positiony-=1
            holdallx.append(int(self.positionx))
            holdally.append(int(self.positiony))
            self.positiony-=1
            holdallx.append(int(self.positionx))
            holdally.append(int(self.positiony))
        elif direction == 'DOWN':
            self.positiony+=1
            holdallx.append(int(self.positionx))
            holdally.append(int(self.positiony)) 
            self.positiony+=1
            holdallx.append(int(self.positionx))
            holdally.append(int(self.positiony))           
        elif direction == 'LEFT':
            self.positionx-=1
            holdallx.append(int(self.positionx))
            holdally.append(int(self.positiony))   
            self.positionx-=1
            holdallx.append(int(self.positionx))
            holdally.append(int(self.positiony))         
        elif direction == 'RIGHT':
            self.positionx+=1
            holdallx.append(int(self.positionx))
            holdally.append(int(self.positiony))   
            self.positionx+=1
            holdallx.append(int(self.positionx))
            holdally.append(int(self.positiony))         
        if self.__hitsomething__() == True:
            print "Uh-OH"
            gameover()
    def __hitsomething__(self):
        retwut = False
        for i in range(len(holdallx)-1):
           # print "{} == self{}. {}==self{}".format(holdallx[i], int(self.positionx),holdally[i], int(self.positiony))
            if holdallx[i]==int(self.positionx) and holdally[i]==int(self.positiony):
                retwut = True
            elif self.positionx > 495 or self.positionx < 5 or self.positiony > 495 or self.positiony < 5:
                retwut = True
        return retwut;
    def display(self, *color):
        damn = list(*color)
        stroke(damn[0], damn[1], damn[2])
        fill(damn[0], damn[1], damn[2])
        ellipse(self.positionx, self.positiony, 5,5)
        
def gameover():
    print "gameover!!!"
    background(255,255,255)
    fill(0)
    textAlign(CENTER)
    text("GAMEOVER!!!", 250,250)
    
def newgame():
    global player
    global bot
    del holdallx[:]
    del holdally[:]
    player = Trons(int(random(5, 490)),int(random(5, 490)))
    bot = Trons(int(random(5,490)),int(random(5, 490)))

def setup():
    size(500, 500)
    stroke(255,3,6)
    fill(0)
    rect(0,0,499,499)
    frameRate(60)
    newgame()
    fill(255,255, 6)
    textAlign(CENTER)
    text("Use wasd to move, press r to restart", 250, 250)
    textAlign(CENTER)
    
    
def draw():
    player.display([0,255,176])
    bot.display([255,132,0])
    
def restart():
    size(500, 500)
    stroke(255,3,6)
    fill(0)
    rect(0,0,499,499)
    newgame()
    fill(255,255, 6)
    textAlign(CENTER)
    text("Use wasd to move, press r to restart", 250, 250)
    textAlign(CENTER)

def keyPressed():
    global player
    if keyCode == 87:#W
        player.move("UP")
        bot.move("UP")
    elif keyCode == 83:#S
        player.move("DOWN")
        bot.move("DOWN")
    elif keyCode == 65:#A
        player.move("LEFT")
        bot.move("RIGHT")
    elif keyCode == 68:#D
        player.move("RIGHT")
        bot.move("LEFT")
    if keyCode == 82:
        restart()

    
    