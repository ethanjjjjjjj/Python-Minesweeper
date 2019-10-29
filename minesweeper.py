#Ethan Williams
#Minesweeper
#20/11/16
import gc
from tkinter import *
import time
import random #imports the library to make randome coordinates for the bombs
from PIL import ImageTk, Image

s=""
global userx
global usery
touching=[]
def resetgrids():
    global grid
    global grid2
    global blanks
    global firstgo
    firstgo=0
    grid=[#defines the hidden grid where the bomb positions are kept
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]]
    grid2=[#defines the grid which is shown to the user each turn
        ["■","■","■","■","■","■","■","■","■","■"],
        ["■","■","■","■","■","■","■","■","■","■"],
        ["■","■","■","■","■","■","■","■","■","■"],
        ["■","■","■","■","■","■","■","■","■","■"],
        ["■","■","■","■","■","■","■","■","■","■"],
        ["■","■","■","■","■","■","■","■","■","■"],
        ["■","■","■","■","■","■","■","■","■","■"],
        ["■","■","■","■","■","■","■","■","■","■"],
        ["■","■","■","■","■","■","■","■","■","■"],
        ["■","■","■","■","■","■","■","■","■","■"]]
    bombs=0#sets the initial value of bombs
    while bombs<20:#loop keeps adding bombs at random coordinates until there are 20 bombs
        x=random.randrange(1,10)#generates the random coordinate for the bomb
        y=random.randrange(1,10)
        if grid[x][y] == "x":
            pass
        else:
            grid[x][y]="x"
            bombs=bombs+1#adds 1 to the number of bombs in the grid
    for a in range(0,10):#calculates values to go in the boxes based on how many bombs are next to them
        for b in range(0,10):
            gridvalue=0 #sets the initial value of a box to 0
            if a==0 and b==0:#top left corner       Specific cases for checking surrounding boxes
                if grid[1][0]=="x":
                    gridvalue=gridvalue+1
                if grid[1][1]=="x":
                    gridvalue=gridvalue+1
                if grid[0][1]=="x":
                    gridvalue=gridvalue+1
            elif a==0 and b==9:#top right corner
                if grid[a][b-1]=="x":
                    gridvalue=gridvalue+1
                if grid[a+1][b-1]=="x":
                    gridvalue=gridvalue+1
                if grid[a+1][b]=="x":
                    gridvalue=gridvalue+1
            elif a==9 and b==0:#bottom left
                if grid[a-1][b]=="x":
                    gridvalue=gridvalue+1
                if grid[a-1][b+1]=="x":
                    gridvalue=gridvalue+1
                if grid[a][b+1]=="x":
                    gridvalue=gridvalue+1
            elif a==9 and b==9:#bottom right
                if grid[a-1][b]=="x":
                    gridvalue=gridvalue+1
                if grid[a-1][b-1]=="x":
                    gridvalue=gridvalue+1
                if grid[a][b-1]=="x":
                    gridvalue=gridvalue+1
            elif a>0 and a<9 and b==0:#left column
                if grid[a+1][b]=="x":
                    gridvalue=gridvalue+1
                if grid[a+1][b+1]=="x":
                    gridvalue=gridvalue+1
                if grid[a][b+1]=="x":
                    gridvalue=gridvalue+1
                if grid[a-1][b]=="x":
                    gridvalue=gridvalue+1
                if grid[a-1][b+1]=="x":
                    gridvalue=gridvalue+1
            elif a>0 and a < 9 and b==9:#right column
                if grid[a-1][b]=="x":
                    gridvalue=gridvalue+1
                if grid[a-1][b-1]=="x":
                    gridvalue=gridvalue+1
                if grid[a][b-1]=="x":
                    gridvalue=gridvalue+1
                if grid[a+1][b-1]=="x":
                    gridvalue=gridvalue+1
                if grid[a+1][b]=="x":
                    gridvalue=gridvalue+1
            elif 0<b and b<9 and a==0: #top row
                if grid[0][b-1]=="x":
                    gridvalue=gridvalue+1
                if grid[1][b-1]=="x":
                    gridvalue=gridvalue+1
                if grid[1][b]=="x":
                    gridvalue=gridvalue+1
                if grid[1][b+1]=="x":
                    gridvalue=gridvalue+1
                if grid[0][b+1]:
                    gridvalue=gridvalue+1
            elif 0<b and b<9 and a==9: #bottom row
                if grid[a][b-1]=="x":
                    gridvalue=gridvalue+1
                if grid[a-1][b-1]=="x":
                    gridvalue=gridvalue+1
                if grid[a-1][b]=="x":
                    gridvalue=gridvalue+1
                if grid[a-1][b+1]=="x":
                    gridvalue=gridvalue+1
                if grid[a][b+1]:
                    gridvalue=gridvalue+1
            elif a>0 and a<9 and b>0 and b<9:#main section
                if grid[a-1][b-1]=="x":
                    gridvalue=gridvalue+1
                if grid[a-1][b]=="x":
                    gridvalue=gridvalue+1
                if grid[a-1][b+1]=="x":
                    gridvalue=gridvalue+1
                if grid[a][b-1]=="x":
                    gridvalue=gridvalue+1
                if grid[a][b+1]=="x":
                    gridvalue=gridvalue+1
                if grid[a+1][b-1]=="x":
                    gridvalue=gridvalue+1
                if grid[a+1][b]=="x":
                    gridvalue=gridvalue+1
                if grid[a+1][b+1]=="x":
                    gridvalue=gridvalue+1
            if grid[a][b]=="x":#skips the box if it has a bomb in it
                pass
            else:
                grid[a][b]=gridvalue #sets the value of the box to 0 if there are no bombs near it
    blanks=[]#sets the list containing all of the blank boxes to 0
    for e in range(0,10):#puts all the blank values into a list
        for f in range(0,10):
            if grid[e][f]==0:
                blanks.append([e,f])

resetgrids()
def printList():#prints out the 2d grid
    for i in range(0,10):
        out=""
        for c in range(0,10):
            out=out+str(grid2[i][c])+" "#adds the value of each line of the grid to a variable
        print(s.join(out))#prints each line of the grid without any quotation marks or square brackets
#printList() #prints the blank grid initially for the user at the start of the game
endgame=False

#loop that keeps the game going until the player hits a bomb
    #userx=int(input("input an x value"))
    #usery=int(input("input a y value"))
    #print("\n"*22)#prints 22 new lines to clear the shell for the next printed grid
    ##usery=(9-usery)+1#converts the user's x and y inputs into indexes for the grid list
    #userx=userx-1
def changegrid(usery,userx):
    
    global touching
    global blanks
    global firstgo
    if firstgo==0:
        while grid[usery][userx]!=0:
            resetgrids()
        firstgo=firstgo+1
    grid2[usery][userx]=grid[usery][userx]
    
    if grid[usery][userx]==0: #checks if the user chose a box that is blank(has no bombs next to it)

        touching=[] #defines a new list to store the coordinates of all the adjacent blank boxes next to the one the user selects
        blanky=usery
        blankx=userx
        touching.append([blanky,blankx])#puts the user chosen box into the list

        for i1 in range(0,len(blanks)): #loops for the number of items in the list of blank boxes
            for i2 in range(0,len(touching)):
                    y2=touching[i2][0]
                    x2=touching[i2][1]
                    possible=[]
                    try:#trying to see if the box above the currently selected coordinates exists
                        trying=grid[y2-1][x2]#tries by setting a variable equal to the box
                        possible.append([y2-1,x2]) # if it does exist then it is added to the list of possible adjacent boxes
                    except:#if the box doesnt exist this code is passed and does nothing
                        pass
                    try:
                        trying=grid[y2][x2-1]#checks if the box to the left exists
                        possible.append([y2,x2-1])
                    except:
                        pass
                    try:
                        trying=grid[y2][x2+1]#checks if the box to the right exists
                        possible.append([y2,x2+1])
                    except:
                        pass
                    try:
                        trying=grid[y2+1][x2]#checks if the box beneath exists
                        possible.append([y2+1,x2])
                    except:
                        pass
                    try:
                        trying=grid[y2-1][x2-1]#checks if the box beneath exists
                        possible.append([y2-1,x2-1])
                    except:
                        pass
                    try:
                        trying=grid[y2-1][x2+1]#checks if the box beneath exists
                        possible.append([y2-1,x2+1])
                    except:
                        pass
                    try:
                        trying=grid[y2+1][x2-1]#checks if the box beneath exists
                        possible.append([y2+1,x2-1])
                    except:
                        pass
                    try:
                        trying=grid[y2+1][x2+1]#checks if the box beneath exists
                        possible.append([y2+1,x2+1])
                    except:
                        pass
                    
                    for i3 in range(0,len(possible)):#goes through the list of possible adjacents
                        if (possible[i3] in blanks): #checks if any of them are on the list of blank boxes
                            if possible[i3] in  touching: #if it is already in the list of touching blanks it does nothing
                                pass
                            else:
                                touching.append(possible[i3])#if the coordinates are not already in the list then they are added to the list of blank boxes touching the one the user picked
    if touching==[]: #if there is nothing in the touching variable the code does nothing. This stops the program crashing if it can't find values in it
        pass
    else:
        for i4 in range(0,len(touching)):#sets the grid value equal to blank if the box is on the touching blanks list b means blank box
            ny=touching[i4][0]
            nx=touching[i4][1]
            grid2[ny][nx]="0"
            if grid2[ny][nx]=="0":
                try:
                    if nx==0 and ny==0 :
                        try:
                            grid2[ny][nx+1]=grid[ny][nx+1]
                        except:
                            pass
                        try:
                            grid2[ny+1][nx+1]=grid[ny+1][nx+1]
                        except:
                            pass
                        try:
                            grid2[ny+1][nx]=grid[ny+1][nx]
                        except:
                            pass
                    elif nx==9 and ny==0:
                        try:
                            grid2[ny][nx-1]=grid[ny][nx-1]
                        except:
                            pass
                        try:
                            grid2[ny+1][nx-1]=grid[ny+1][nx-1]
                        except:
                            pass
                        try:
                            grid2[ny+1][nx]=grid[ny+1][nx]
                        except:
                            pass
                    elif nx==0 and ny >0:
                        try:
                            grid2[ny-1][nx]=grid[ny-1][nx]
                        except:
                            pass
                        try:
                            grid2[ny-1][nx+1]=grid[ny-1][nx+1]
                        except:
                            pass
                        try:
                            grid2[ny][nx+1]=grid[ny][nx+1]
                        except:
                            pass
                        try:
                            grid2[ny+1][nx+1]=grid[ny+1][nx+1]
                        except:
                            pass
                        try:
                            grid2[ny+1][nx]=grid[ny+1][nx]
                        except:
                            pass
                    elif ny==0 and nx>0:
                        try:
                            grid2[ny][nx-1]=grid[ny][nx-1]
                        except:
                            pass
                        try:
                            grid2[ny][nx+1]=grid[ny][nx+1]
                        except:
                            pass
                        try:
                            grid2[ny+1][nx-1]=grid[ny+1][nx-1]
                        except:
                            pass
                        try:
                            grid2[ny+1][nx]=grid[ny+1][nx]
                        except:
                            pass
                        try:
                            grid2[ny+1][nx+1]=grid[ny+1][nx+1]
                        except:
                            pass
                    
                    else:
                        try:
                            grid2[ny-1][nx-1]=grid[ny-1][nx-1]
                        except:
                            pass
                        try:
                            grid2[ny-1][nx]=grid[ny-1][nx]
                        except:
                            pass
                        try:
                            grid2[ny-1][nx+1]=grid[ny-1][nx+1]
                        except:
                            pass
                        try:
                            grid2[ny][nx-1]=grid[ny][nx-1]
                        except:
                            pass
                        try:
                            grid2[ny][nx+1]=grid[ny][nx+1]
                        except:
                            pass
                        try:
                            grid2[ny+1][nx-1]=grid[ny+1][nx-1]
                        except:
                            pass
                        try:
                            grid2[ny+1][nx]=grid[ny+1][nx]
                        except:
                            pass
                        try:
                            grid2[ny+1][nx+1]=grid[ny+1][nx+1]
                        except:
                            pass
                except:
                    pass
                
        touching=[]
    #printList()   #prints the grid for the user (with any blanks or numbers currently being shown to the user) 
    if grid[usery][userx]=="x": #if the user chose a box with a mine on it then it prints a message and ends the loop
        print("you hit a mine")
        refreshbuttons()
        for endy in range(0,10):
            for endx in range(0,10):
                grid2[endy][endx]=grid[endy][endx]
        endgame=True
#gui stuff:
root=Tk()
frame=Frame(root)

HEIGHT = 30
WIDTH = 30
path = "C:\\Users\\Tript\\Desktop\\What!\\bomb.jpg"
thumbnail = Image.open(path)
thumbnail.thumbnail((HEIGHT, WIDTH), Image.ANTIALIAS)
bomb = ImageTk.PhotoImage(thumbnail)

def gencanvas():
    global canvas
    canvas=Canvas(frame,width=500,height=500)
    canvas.pack()
label1=Label(text="Minesweeper")
label1.pack(side=TOP)
frame.pack()
def determinepos(x,y):
    #print(x,y)
    changegrid(x,y)
    refreshbuttons()
buttonnumber=0
buttonx=-1
buttony=-1
gencanvas()
def refreshbuttons():
    canvas.delete(ALL)
    gc.collect()
    global buttonx
    global buttony
    buttonx=-1
    buttony=-1
    buttonnumber=0
    for d in range(50,1000,100):
        buttonx=buttonx+1
        buttony=-1
        for b in range(50,1000,100):
            buttony=buttony+1
            e=d/2
            c=b/2
            buttonnumber=buttonnumber+1
            if grid2[buttonx][buttony]==1:
                button1=Button(command=lambda buttonx2=buttonx,buttony2=buttony: determinepos(buttonx2,buttony2),text=grid2[buttonx][buttony],font=("Courier", 44),fg="blue")
            elif grid2[buttonx][buttony]==2:
                button1=Button(command=lambda buttonx2=buttonx,buttony2=buttony: determinepos(buttonx2,buttony2),text=grid2[buttonx][buttony],font=("Courier", 44),fg="green")
            elif grid2[buttonx][buttony]==3:
                button1=Button(command=lambda buttonx2=buttonx,buttony2=buttony: determinepos(buttonx2,buttony2),text=grid2[buttonx][buttony],font=("Courier", 44),fg="red")
            elif grid2[buttonx][buttony]==4:
                button1=Button(command=lambda buttonx2=buttonx,buttony2=buttony: determinepos(buttonx2,buttony2),text=grid2[buttonx][buttony],font=("Courier", 44),fg="#00008B")
            elif grid2[buttonx][buttony]==5:
                button1=Button(command=lambda buttonx2=buttonx,buttony2=buttony: determinepos(buttonx2,buttony2),text=grid2[buttonx][buttony],font=("Courier", 44),fg="#8B0000")
            elif grid2[buttonx][buttony]==6:
                button1=Button(command=lambda buttonx2=buttonx,buttony2=buttony: determinepos(buttonx2,buttony2),text=grid2[buttonx][buttony],font=("Courier", 44),fg="#40E0D0")
            elif grid2[buttonx][buttony]==7:
                button1=Button(command=lambda buttonx2=buttonx,buttony2=buttony: determinepos(buttonx2,buttony2),text=grid2[buttonx][buttony],font=("Courier", 44),fg="black")
            elif grid2[buttonx][buttony]==8:
                button1=Button(command=lambda buttonx2=buttonx,buttony2=buttony: determinepos(buttonx2,buttony2),text=grid2[buttonx][buttony],font=("Courier", 44),fg="#D3D3D3")
            elif grid2[buttonx][buttony]=='x':
                button1=Button(root, text="", image=bomb)
            else:
                button1=Button(command=lambda buttonx2=buttonx,buttony2=buttony: determinepos(buttonx2,buttony2),text=grid2[buttonx][buttony],font=("Courier", 44),fg="black")
            window1=canvas.create_window(c,e,height=50,width=50,window=button1)
    root.update()
def resetgrids2():
    global firstgo
    resetgrids()
    refreshbuttons()
resetbutton=Button(frame,text="reset",command=resetgrids2)
resetbutton.pack(side=BOTTOM)
refreshbuttons()
root.mainloop()
