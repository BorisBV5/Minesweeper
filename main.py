#tags: empty=0 mine=90 1=1 2=2 3=3 4=4 5=5 6=6 7=7 8=8 flag=10
#hidden tags: empty=-1 flaged mine=900 mine clicked=999 mines reveal=909
#dificulty ez=48 med=72 hard=80

#Spagetti code I wrote in high school(might fix later)(probably won't)

import random
import pygame
import json

pygame.init()

screen = pygame.display.set_mode([400, 460])
pygame.display.set_caption("Minesweeper")
programIcon = pygame.image.load("media/icon.png")
pygame.display.set_icon(programIcon)
running = True
white=(0xffffff)
lgray=(0xbfbfbf)
red=(255,0,0)
black=(0,0,0)
grid = [[0 for x in range(20)] for y in range(20)]
count=0
time=pygame.time.Clock()
start=0
end=0
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
buttonDefeat=pygame.image.load("media/fail.png")
buttonWin=pygame.image.load("media/win.png")
topBg=pygame.image.load("media/topbg.png")
bg=pygame.image.load("media/bg.png")
mineCount=0
easy=48
medium=72
hard=80
flagCount=0
buttonIsPressed=False
buttonIsSurprised=False
tileIsPressed=False
defeat=False
win=False
dificultySelection=True
buttonEasyIsPressed=False
buttonMediumIsPressed=False
buttonHardIsPressed=False
selectedDificulty=1
notClicked=0
save = {
    'easy': 0,
    'medium': 0,
    'hard': 0
}
try:
    with open('save.txt') as records:
        save = json.load(records)
except:
    print("fnf")

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

def checkFlags(y,x):
    flagsAroundCount=0
    if x!=0 and y!=0: 
        if grid[y-1][x-1]==10 or grid[y-1][x-1]==900: flagsAroundCount+=1
    if x!=19 and y!=0:
        if grid[y-1][x+1]==10 or grid[y-1][x+1]==900: flagsAroundCount+=1
    if y!=0:
        if grid[y-1][x]==10 or grid[y-1][x]==900: flagsAroundCount+=1
    if x!=0 and y!=19:
        if grid[y+1][x-1]==10 or grid[y+1][x-1]==900: flagsAroundCount+=1
    if x!=19 and y!=19:
        if grid[y+1][x+1]==10 or grid[y+1][x+1]==900: flagsAroundCount+=1
    if y!=19:
        if grid[y+1][x]==10 or grid[y+1][x]==900: flagsAroundCount+=1
    if x!=19:
        if grid[y][x+1]==10 or grid[y][x+1]==900: flagsAroundCount+=1
    if x!=0:
        if grid[y][x-1]==10 or grid[y][x-1]==900: flagsAroundCount+=1
    return flagsAroundCount

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

while running:

    mousePos=pygame.mouse.get_pos()
    columnPos=mousePos[0]//(20)
    rowPos=(mousePos[1]//(20))-3
    screen.blit(topBg, [0,0])
    notClicked=0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open('save.txt','w') as records:
                json.dump(save, records)
            running = False
        elif event.type==pygame.MOUSEBUTTONDOWN:
            if dificultySelection:
                if mousePos[1]>90 and mousePos[1]<130 and mousePos[0]>180 and mousePos[0]<220:
                    buttonEasyIsPressed=True
                if mousePos[1]>190 and mousePos[1]<230 and mousePos[0]>180 and mousePos[0]<220:
                    buttonMediumIsPressed=True
                if mousePos[1]>290 and mousePos[1]<330 and mousePos[0]>180 and mousePos[0]<220:
                    buttonHardIsPressed=True
            else:
                if mousePos[1]>10 and mousePos[1]<50 and mousePos[0]>180 and mousePos[0]<220:
                    buttonIsPressed=True
                if defeat or win:
                    break
                if mousePos[1]<60:
                    break
                if event.button==1:
                    if grid[rowPos][columnPos]==0 or grid[rowPos][columnPos]==90:    
                        tileIsPressed=True
                        buttonIsSurprised=True
                    elif grid[rowPos][columnPos]>0 and grid[rowPos][columnPos]<9:
                        tileIsPressed=True
                        buttonIsSurprised=True
                elif event.button==3:
                    if grid[rowPos][columnPos]==10:
                        grid[rowPos][columnPos]=0
                        flagCount-=1
                    elif grid[rowPos][columnPos]==0:
                        grid[rowPos][columnPos]=10
                        flagCount+=1
                    elif grid[rowPos][columnPos]==90:
                        grid[rowPos][columnPos]=900
                        flagCount+=1
                    elif grid[rowPos][columnPos]==900:
                        grid[rowPos][columnPos]=90
                        flagCount-=1
                    if count ==0:
                        start=pygame.time.get_ticks()                
                        count+=1


        elif event.type==pygame.MOUSEBUTTONUP:
            if dificultySelection:
                buttonEasyIsPressed=False
                buttonMediumIsPressed=False
                buttonHardIsPressed=False
                if mousePos[1]>90 and mousePos[1]<130 and mousePos[0]>180 and mousePos[0]<220:
                    selectedDificulty=1
                    dificultySelection=False
                if mousePos[1]>190 and mousePos[1]<230 and mousePos[0]>180 and mousePos[0]<220:
                    selectedDificulty=2
                    dificultySelection=False
                if mousePos[1]>290 and mousePos[1]<330 and mousePos[0]>180 and mousePos[0]<220:
                    selectedDificulty=3
                    dificultySelection=False
            else:
                if event.button==1:
                    tileIsPressed=False
                    buttonIsPressed=False
                    buttonIsSurprised=False
                    if mousePos[1]>10 and mousePos[1]<50 and mousePos[0]>180 and mousePos[0]<220:
                        grid = [[0 for x in range(20)] for y in range(20)]
                        count=0
                        start=0
                        timer=myFont.render("00:00", 1, red)
                        mineCount=0
                        flagCount=0
                        buttonIsPressed=False
                        defeat=False
                        win=False
                        notClicked=0
                        dificultySelection=True
                    if defeat or win:
                        break
                    if mousePos[1]<60:
                        break
                    if grid[rowPos][columnPos]==0:
                        if count==2:
                            flood(rowPos, columnPos)
                    elif grid[rowPos][columnPos]==90:
                        grid[rowPos][columnPos]=999
                        defeat=True
                        end=pygame.time.get_ticks()
                        for i in range(len(grid)):
                            for j in range(len(grid[i])):
                                if grid[i][j]==90:
                                    grid[i][j]=909
                    elif grid[rowPos][columnPos]>0 and grid[rowPos][columnPos]<9:
                        if checkFlags(rowPos, columnPos) >= grid[rowPos][columnPos]:
                            if columnPos!=0 and rowPos!=0 and grid[rowPos-1][columnPos-1]==0: flood(rowPos-1,columnPos-1)
                            elif columnPos!=0 and rowPos!=0 and grid[rowPos-1][columnPos-1]==90:
                                grid[rowPos-1][columnPos-1]=999
                                defeat=True
                                end=pygame.time.get_ticks()
                            if columnPos!=19 and rowPos!=0 and grid[rowPos-1][columnPos+1]==0: flood(rowPos-1, columnPos+1)
                            elif columnPos!=19 and rowPos!=0 and grid[rowPos-1][columnPos+1]==90:
                                grid[rowPos-1][columnPos+1]=999
                                defeat=True
                                end=pygame.time.get_ticks()
                            if rowPos!=0 and grid[rowPos-1][columnPos]==0: flood(rowPos-1, columnPos)
                            elif rowPos!=0 and grid[rowPos-1][columnPos]==90:
                                grid[rowPos-1][columnPos]=999
                                defeat=True
                                end=pygame.time.get_ticks()
                            if columnPos!=0 and rowPos!=19 and grid[rowPos+1][columnPos-1]==0: flood(rowPos+1, columnPos-1)
                            elif columnPos!=0 and rowPos!=19 and grid[rowPos+1][columnPos-1]==90:
                                grid[rowPos+1][columnPos-1]=999
                                defeat=True
                                end=pygame.time.get_ticks()
                            if columnPos!=19 and rowPos!=19 and grid[rowPos+1][columnPos+1]==0: flood(rowPos+1, columnPos+1)
                            elif columnPos!=19 and rowPos!=19 and grid[rowPos+1][columnPos+1]==90:
                                grid[rowPos+1][columnPos+1]=999
                                defeat=True
                                end=pygame.time.get_ticks()
                            if rowPos!=19 and grid[rowPos+1][columnPos]==0: flood(rowPos+1, columnPos)
                            elif rowPos!=19 and grid[rowPos+1][columnPos]==90:
                                grid[rowPos+1][columnPos]=999
                                defeat=True
                                end=pygame.time.get_ticks()
                            if columnPos!=19 and grid[rowPos][columnPos+1]==0: flood(rowPos, columnPos+1)
                            elif columnPos!=19 and grid[rowPos][columnPos+1]==90:
                                grid[rowPos][columnPos+1]=999
                                defeat=True
                                end=pygame.time.get_ticks()
                            if columnPos!=0 and grid[rowPos][columnPos-1]==0: flood(rowPos, columnPos-1)
                            elif columnPos!=0 and grid[rowPos][columnPos-1]==90:
                                grid[rowPos][columnPos-1]=999
                                defeat=True
                                end=pygame.time.get_ticks()
                    if count ==0:
                        start=pygame.time.get_ticks()
                        count+=1

    if count==1:
        for minePos in range (200):
            minePosColumn=random.randint(0,19)
            minePosRow=random.randint(0,19)
            if (minePosColumn, minePosRow)!=(columnPos-1, rowPos-1) and (minePosColumn, minePosRow)!=(columnPos, rowPos-1)\
                and (minePosColumn, minePosRow)!=(columnPos+1, rowPos-1) and (minePosColumn, minePosRow)!=(columnPos-1, rowPos)\
                and (minePosColumn, minePosRow)!=(columnPos, rowPos) and (minePosColumn, minePosRow)!=(columnPos+1, rowPos)\
                and (minePosColumn, minePosRow)!=(columnPos-1, rowPos+1) and (minePosColumn, minePosRow)!=(columnPos, rowPos+1)\
                and (minePosColumn, minePosRow)!=(columnPos+1, rowPos+1) and grid[minePosRow][minePosColumn]!=90:       
                grid[minePosRow][minePosColumn]=90
                mineCount=mineCount+1
            if selectedDificulty==1:    
                if mineCount==48:
                    break
            elif selectedDificulty==2:    
                if mineCount==72:
                    break
            elif selectedDificulty==3:    
                if mineCount==80:
                    break
        flood(rowPos, columnPos)
        count+=1

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]==0:
                notClicked+=1

    if count==2:
        if mineCount-flagCount==0 or notClicked==0:
            if notClicked!=0:
                pass
            else:
                for i in range(len(grid)):
                    for j in range(len(grid[i])):  #fix this something isn't right here
                        if grid[i][j]==90:
                            grid[i][j]=900
                            end=pygame.time.get_ticks()
                count+=1
                if count==3:
                    end=pygame.time.get_ticks()
                    count+=1
                flagCount=mineCount
                win=True

    if defeat:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==10:
                    grid[i][j]=101

    if dificultySelection==False:    #this is garbage(make it not garbage)
        for row in range(20):
            for column in range(20):
                color = lgray
                screen.blit(tile,[20*column,(20*row)+60])        
                if grid[row][column] == -1:
                    screen.blit(bgtile,[20*(column),(20*(row))+60])
                elif grid[row][column]==10:
                    screen.blit(flag,[20*(column),(20*(row))+60])
                elif grid[row][column]==90:
                    screen.blit(tile,[20*(column),(20*(row))+60])
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
                elif grid[row][column]==999:
                    screen.blit(mineFail,[20*(column),(20*(row))+60])
                elif grid[row][column]==909:
                    screen.blit(mine,[20*(column),(20*(row))+60])
                elif grid[row][column]==101:
                    screen.blit(notMine,[20*(column),(20*(row))+60])
                if tileIsPressed and grid[rowPos][columnPos] not in (1, 2, 3, 4, 5, 6, 7, 8, 10, 900) and mousePos[1]>60:
                    screen.blit(bgtile,[20*(columnPos),(20*(rowPos))+60])
                elif tileIsPressed and grid[rowPos][columnPos] in (1, 2, 3, 4, 5, 6, 7, 8) and mousePos[1]>60:
                    if columnPos!=0 and rowPos!=0 and grid[rowPos-1][columnPos-1]in (0, 90): screen.blit(bgtile,[20*(columnPos-1),(20*(rowPos-1))+60])
                    if columnPos!=19 and rowPos!=0 and grid[rowPos-1][columnPos+1]in (0, 90): screen.blit(bgtile,[20*(columnPos+1),(20*(rowPos-1))+60])
                    if rowPos!=0 and grid[rowPos-1][columnPos]in (0, 90): screen.blit(bgtile,[20*(columnPos),(20*(rowPos-1))+60])
                    if columnPos!=0 and rowPos!=19 and grid[rowPos+1][columnPos-1]in (0, 90): screen.blit(bgtile,[20*(columnPos-1),(20*(rowPos+1))+60])
                    if columnPos!=19 and rowPos!=19 and grid[rowPos+1][columnPos+1]in (0, 90): screen.blit(bgtile,[20*(columnPos+1),(20*(rowPos+1))+60])
                    if rowPos!=19 and grid[rowPos+1][columnPos]in (0, 90): screen.blit(bgtile,[20*(columnPos),(20*(rowPos+1))+60])
                    if columnPos!=19 and grid[rowPos][columnPos+1]in (0, 90): screen.blit(bgtile,[20*(columnPos+1),(20*(rowPos))+60])
                    if columnPos!=0 and grid[rowPos][columnPos-1] in (0, 90): screen.blit(bgtile,[20*(columnPos-1),(20*(rowPos))+60])
        
        if defeat:
            minutes=((end - start)//60000)
            seconds=((end - start)//1000)-minutes*60
        elif win:
            minutes=((end - start)//60000)
            seconds=((end - start)//1000)-minutes*60
            if selectedDificulty==1:
                if (end-start)<save['easy'] and save['easy']!=0:
                    save['easy']=end - start
                elif save['easy']==0:
                    save['easy']=end - start
            elif selectedDificulty==2:
                if (end-start)<save['mdium']:
                    save['medium']=end - start
                elif save['medium']==0:
                    save['medium']=end - start
            elif selectedDificulty==3:
                if (end-start)<save['hard']:
                    save['hard']=end - start
                elif save['hard']==0:
                    save['hard']=end - start
        else:
            minutes=((pygame.time.get_ticks() - start)//60000)
            seconds=((pygame.time.get_ticks() - start)//1000)-minutes*60
        if count>0: 
            timer=myFont.render(str(minutes).zfill(2)+":"+str(seconds).zfill(2), 1, red)
            time=(pygame.time.get_ticks() - start)

        if buttonIsPressed:
            screen.blit(buttonPressed, [180, 10])
        elif buttonIsSurprised:
            screen.blit(buttonSurprised, [180, 10])
        elif defeat:
            screen.blit(buttonDefeat, [180, 10])
        elif win:
            screen.blit(buttonWin, [180, 10])
        else: 
            screen.blit(button, [180, 10])
        mines=myFont.render(str(mineCount-flagCount).zfill(4), 1, red)
        pygame.draw.rect(screen, black, [27 , 17, 68, 27])
        screen.blit(mines, [29, 20])
        pygame.draw.rect(screen, black, [305 , 17, 71, 27])
        screen.blit(timer, [306,20])
    
    else:
        screen.blit(bg, [0,0])
        if buttonEasyIsPressed:
            screen.blit(buttonPressed, [180, 90])
        else:
            screen.blit(button, [180, 90])
        if buttonMediumIsPressed:
            screen.blit(buttonPressed, [180, 190])
        else:
            screen.blit(buttonWin, [180, 190])
        if buttonHardIsPressed:
            screen.blit(buttonPressed, [180, 290])
        else:
            screen.blit(buttonDefeat, [180, 290])
        bestEasy=myFont.render(str((save['easy']//60000)).zfill(2)+":"+str((save['easy']//1000)-(save['easy']//60000)*60).zfill(2), 1, red)
        bestMedium=myFont.render(str((save['medium']//60000)).zfill(2)+":"+str((save['medium']//1000)-(save['medium']//60000)*60).zfill(2), 1, red)
        bestHard=myFont.render(str((save['hard']//60000)).zfill(2)+":"+str((save['hard']//1000)-(save['hard']//60000)*60).zfill(2), 1, red)
        pygame.draw.rect(screen, black, [165 , 140, 71, 27])
        screen.blit(bestEasy, [167,143])
        pygame.draw.rect(screen, black, [165 , 240, 71, 27])
        screen.blit(bestMedium, [167,243])
        pygame.draw.rect(screen, black, [165 , 340, 71, 27])
        screen.blit(bestHard, [167,343])

    
    pygame.display.flip()


pygame.quit()
