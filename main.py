#tags: empty=0 mine=9 1=1 2=2 3=3 4=4 5=5 6=6 7=7 8=8 flag=100
#hidden tags empty=99 mine=90
#dificulty ez=90

import random
import pygame
pygame.init()

screen = pygame.display.set_mode([400, 460])
pygame.display.set_caption("Minesweeper")
programIcon = pygame.image.load('media/icon.png')
pygame.display.set_icon(programIcon)
width=20
height=20
margin=2
running = True
white=(255,255,255)
lgray=(0xbfbfbf)
green=(0,255,0)
red=(255,0,0)
topBarHeight=60
grid = [[0 for x in range(20)] for y in range(20)]
count=0
time=pygame.time.Clock()
start=0
myFont = pygame.font.Font("media/DSEG7Modern-Bold.ttf", 20)
timer=myFont.render("00:00", 1, red)
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
mineCount=0

def checkNumber(y,x):
    minesAroundCount=0
    if columnPos!=0 and rowPos!=0 and grid[rowPos-1][columnPos-1]==90: minesAroundCount+=1
    if columnPos!=19 and rowPos!=0 and grid[rowPos-1][columnPos+1]==90 : minesAroundCount+=1
    if rowPos!=0 and grid[rowPos-1][columnPos]==90: minesAroundCount+=1
    if columnPos!=0 and rowPos!=19 and grid[rowPos+1][columnPos-1]==90: minesAroundCount+=1
    if columnPos!=19 and rowPos!=19 and grid[rowPos+1][columnPos+1]==90: minesAroundCount+=1
    if rowPos!=19 and grid[rowPos+1][columnPos]==90 : minesAroundCount+=1
    if columnPos!=19 and grid[rowPos][columnPos+1]==90: minesAroundCount+=1
    if columnPos!=0 and grid[rowPos][columnPos-1]==90: minesAroundCount+=1
    print(minesAroundCount)
    return minesAroundCount

while running:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                mousePos=pygame.mouse.get_pos()
                columnPos=mousePos[0]//(20)
                rowPos=(mousePos[1]//(20))-3
                if grid[rowPos][columnPos]==0:
                    numMines=checkNumber(rowPos, columnPos)
                    if numMines>0:
                        grid[rowPos][columnPos]=numMines
                    else:
                        grid[rowPos][columnPos]=99
                if count ==0:
                    start=pygame.time.get_ticks()
                    count+=1
            elif event.button==3:
                mousePos=pygame.mouse.get_pos()
                columnPos=mousePos[0]//(20)
                rowPos=(mousePos[1]//(20))-3
                if grid[rowPos][columnPos]==0:
                    grid[rowPos][columnPos]=100
                if count ==0:
                    start=pygame.time.get_ticks()                
                    count+=1

    if count==1:
        for minePos in range (200):
            minePosColumn=random.randint(0,19)
            minePosRow=random.randint(0,19)
            if (minePosColumn, minePosRow)!=(columnPos-1, rowPos-1) and (minePosColumn, minePosRow)!=(columnPos, rowPos-1) and (minePosColumn, minePosRow)!=(columnPos+1, rowPos-1) and (minePosColumn, minePosRow)!=(columnPos-1, rowPos) and (minePosColumn, minePosRow)!=(columnPos, rowPos) and (minePosColumn, minePosRow)!=(columnPos+1, rowPos) and (minePosColumn, minePosRow)!=(columnPos-1, rowPos+1) and (minePosColumn, minePosRow)!=(columnPos, rowPos+1) and (minePosColumn, minePosRow)!=(columnPos+1, rowPos+1) and grid[minePosRow][minePosColumn]!=90:       
                grid[minePosRow][minePosColumn]=90
                mineCount=mineCount+1
                print(minePosRow, minePosColumn)
            if mineCount==80:
                break
        count+=1
    
    screen.fill(lgray)
    firstRowCounter=0
    for row in range(20):
        for column in range(20):
            color = lgray
            screen.blit(tile,[20*column,(20*row)+60])
            if grid[row][column] == 99:
                screen.blit(bgtile,[20*(column),(20*(row))+60])
            elif grid[row][column]==100:
                screen.blit(flag,[20*(column),(20*(row))+60])
            elif grid[row][column]==90:
                screen.blit(mine,[20*(column),(20*(row))+60])
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
            #pygame.draw.rect(screen, color, [(margin + width) * column + margin, (margin + height) * row + margin+60, width, height])
    minutes=((pygame.time.get_ticks() - start)//60000)
    seconds=((pygame.time.get_ticks() - start)//1000)-minutes*60
    if count>0: 
        timer=myFont.render(str(minutes).zfill(2)+":"+str(seconds).zfill(2), 1, red)
    if count>0: 
        time=(pygame.time.get_ticks() - start)

    screen.blit(timer, [166,25])
    pygame.display.flip()


pygame.quit()
