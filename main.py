#tags: empty=0 mine=90 1=1 2=2 3=3 4=4 5=5 6=6 7=7 8=8 flag=10
#hidden tags: empty=-1 flaged mine=900
#dificulty ez=48 med=72 hard=80

import random
import pygame
pygame.init()

screen = pygame.display.set_mode([400, 460])
pygame.display.set_caption("Minesweeper")
programIcon = pygame.image.load("media/icon.png")
pygame.display.set_icon(programIcon)
width=20
height=20
margin=2
running = True
white=(0xffffff)
lgray=(0xbfbfbf)
red=(255,0,0)
black=(0,0,0)
topBarHeight=60
grid = [[0 for x in range(20)] for y in range(20)]
count=0
time=pygame.time.Clock()
start=0
myFont = pygame.font.Font("media/DSEG7Modern-Bold.ttf", 20)
timer=myFont.render("00:00", 1, red)
mines=myFont.render("00000", 1, red)
tile=pygame.image.load("media/tile.png")
bgtile=pygame.image.load("media/bgtile.png")
flag=pygame.image.load("media/flag.png")
num1=pygame.image.load("media/num1.png")
num2=pygame.image.load("media/num2.png")
num3=pygame.image.load("media/num3.png")
num4=pygame.image.load("media/num4.png")
num5=pygame.image.load("media/num5.png")
num6=pygame.image.load("media/num6.png")
num7=pygame.image.load("media/num7.png")
num8=pygame.image.load("media/num8.png")
mine=pygame.image.load("media/mine.png")
mineFail=pygame.image.load("media/minefail.png")
notMine=pygame.image.load("media/notmine.png")
button=pygame.image.load("media/button.png")
buttonPressed=pygame.image.load("media/buttonpressed.png")
buttonSurprised=pygame.image.load("media/surprise.png")
mineCount=0
easy=48
medium=72
hard=80
falgCount=0

def checkNumber(y,x):
    minesAroundCount=0
    if x!=0 and y!=0 and grid[y-1][x-1]>=90: minesAroundCount+=1
    if x!=19 and y!=0 and grid[y-1][x+1]>=90: minesAroundCount+=1
    if y!=0 and grid[y-1][x]>=90: minesAroundCount+=1
    if x!=0 and y!=19 and grid[y+1][x-1]>=90: minesAroundCount+=1
    if x!=19 and y!=19 and grid[y+1][x+1]>=90: minesAroundCount+=1
    if y!=19 and grid[y+1][x]>=90: minesAroundCount+=1
    if x!=19 and grid[y][x+1]>=90: minesAroundCount+=1
    if x!=0 and grid[y][x-1]>=90: minesAroundCount+=1
    return minesAroundCount

def flood(b, a):
    if grid[b][a]==0:
        if checkNumber(b,a)>0:
            grid[b][a]=checkNumber(b,a)
        else:
            grid[b][a]=-1
            if a<19 and b<19:
                flood(b+1, a+1)
            if a>0 and b<19:
                flood(b+1, a-1)
            if b<19:
                flood(b+1, a)
            if a<19 and b>0:
                flood(b-1, a+1)
            if a>0 and b>0:
                flood(b-1, a-1)
            if b>0:
                flood(b-1, a)
            if a>0:
                flood(b,a-1)
            if a<19:
                flood(b,a+1)
    else:
        return

#def generate(y,x):
#    for minePos in range (200):
#        minePosColumn=random.randint(0,19)
#        minePosRow=random.randint(0,19)
#        if (minePosColumn, minePosRow)!=(x-1, y-1) and (minePosColumn, minePosRow)!=(x, y-1) and (minePosColumn, minePosRow)!=(x+1, y-1) and (minePosColumn, minePosRow)!=(x-1, y) and (minePosColumn, minePosRow)!=(x, y) and (minePosColumn, minePosRow)!=(x+1, y) and (minePosColumn, minePosRow)!=(x-1, y+1) and (minePosColumn, minePosRow)!=(x, y+1) and (minePosColumn, minePosRow)!=(x+1, y+1) and grid[minePosRow][minePosColumn]!=90:       
#            grid[minePosRow][minePosColumn]=90
#            mineCount=mineCount+1
#       if mineCount==48:
#            break

while running:

    mousePos=pygame.mouse.get_pos()
    columnPos=mousePos[0]//(20)
    rowPos=(mousePos[1]//(20))-3
    buttonIsPressed=False
    buttonIsSurprised=False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type==pygame.MOUSEBUTTONDOWN:
            if mousePos[1]<60:
                break
            if event.button==1:
                if grid[rowPos][columnPos]==0:
                    if count==2:
                        flood(rowPos, columnPos)
                    if pygame.mouse.get_pressed()[0]:
                        buttonIsSurprised=True
                if count ==0:
                    start=pygame.time.get_ticks()
                    count+=1
            elif event.button==3:
                if grid[rowPos][columnPos]==10:
                    grid[rowPos][columnPos]=0
                    falgCount-=1
                elif grid[rowPos][columnPos]==0:
                    grid[rowPos][columnPos]=10
                    falgCount+=1
                elif grid[rowPos][columnPos]==90:
                    grid[rowPos][columnPos]=900
                    falgCount+=1
                elif grid[rowPos][columnPos]==900:
                    grid[rowPos][columnPos]=90
                    falgCount-=1
                if count ==0:
                    start=pygame.time.get_ticks()                
                    count+=1

    if mousePos[1]>10 and mousePos[1]<50 and mousePos[0]>180 and mousePos[0]<220:
        if pygame.mouse.get_pressed()[0]:
            buttonIsPressed=True

    if count==1:
        for minePos in range (200):
            minePosColumn=random.randint(0,19)
            minePosRow=random.randint(0,19)
            if (minePosColumn, minePosRow)!=(columnPos-1, rowPos-1) and (minePosColumn, minePosRow)!=(columnPos, rowPos-1) and (minePosColumn, minePosRow)!=(columnPos+1, rowPos-1) and (minePosColumn, minePosRow)!=(columnPos-1, rowPos) and (minePosColumn, minePosRow)!=(columnPos, rowPos) and (minePosColumn, minePosRow)!=(columnPos+1, rowPos) and (minePosColumn, minePosRow)!=(columnPos-1, rowPos+1) and (minePosColumn, minePosRow)!=(columnPos, rowPos+1) and (minePosColumn, minePosRow)!=(columnPos+1, rowPos+1) and grid[minePosRow][minePosColumn]!=90:       
                grid[minePosRow][minePosColumn]=90
                mineCount=mineCount+1
            if mineCount==easy:
                break
        flood(rowPos, columnPos)
        count+=1
    
    screen.fill(lgray)
    firstRowCounter=0
    for row in range(20):
        for column in range(20):
            color = lgray
            screen.blit(tile,[20*column,(20*row)+60])
            if grid[row][column] == -1:
                screen.blit(bgtile,[20*(column),(20*(row))+60])
            elif grid[row][column]==10:
                screen.blit(flag,[20*(column),(20*(row))+60])
            elif grid[row][column]==90:
                screen.blit(mine,[20*(column),(20*(row))+60])
            elif grid[row][column]==900:
                screen.blit(flag,[20*(column),(20*(row))+60])
            elif grid[row][column]==1:
                screen.blit(num1,[20*(column),(20*(row))+60])
            elif grid[row][column]==2:
                screen.blit(num2,[20*(column),(20*(row))+60])
            elif grid[row][column]==3:
                screen.blit(num3,[20*(column),(20*(row))+60])
            elif grid[row][column]==4:
                screen.blit(num4,[20*(column),(20*(row))+60])
            elif grid[row][column]==5:
                screen.blit(num5,[20*(column),(20*(row))+60])
            elif grid[row][column]==6:
                screen.blit(num6,[20*(column),(20*(row))+60])
            elif grid[row][column]==7:
                screen.blit(num7,[20*(column),(20*(row))+60])
            elif grid[row][column]==8:
                screen.blit(num8,[20*(column),(20*(row))+60])
    minutes=((pygame.time.get_ticks() - start)//60000)
    seconds=((pygame.time.get_ticks() - start)//1000)-minutes*60
    if count>0: 
        timer=myFont.render(str(minutes).zfill(2)+":"+str(seconds).zfill(2), 1, red)
    if count>0: 
        time=(pygame.time.get_ticks() - start)

    if buttonIsPressed:
        screen.blit(buttonPressed, [180, 10])
    elif buttonIsSurprised:
        screen.blit(buttonSurprised, [180, 10])
    else: 
        screen.blit(button, [180, 10])
    mines=myFont.render(str(mineCount-falgCount).zfill(4), 1, red)
    pygame.draw.rect(screen, black, [27 , 17, 68, 27])
    screen.blit(mines, [29, 20])
    pygame.draw.rect(screen, black, [305 , 17, 71, 27])
    screen.blit(timer, [306,20])
    pygame.display.flip()


pygame.quit()
