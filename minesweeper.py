#Ethan Williams
#Minesweeper
#20/11/16
import gc
from tkinter import *
import time
import itertools as it
import random #imports the library to make randome coordinates for the bombs
from PIL import ImageTk, Image

s=""
touching=[]
global userx
global usery

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
            grid[x][y] = "x"
            bombs = bombs + 1  # adds 1 to the number of bombs in the grid
    for a in range(
        0, 10
    ):  # calculates values to go in the boxes based on how many bombs are next to them
        for b in range(0, 10):
            if grid[a][b] != "x":
                check_tuple = it.product([a - 1, a, a + 1], [b - 1, b, b + 1])
                check_list = [list(x) for x in check_tuple]
                check_list.remove([a, b])
                for elem in reversed(check_list):
                    if elem[0] < 0 or elem[0] > 9 or elem[1] < 0 or elem[1] > 9:
                        check_list.remove(elem)
                grid[a][b] = len([x for x in check_list if grid[x[0]][x[1]] == "x"])
                # sets the value of the box to 0 if there are no bombs near it
    blanks = []  # sets the list containing all of the blank boxes to 0
    for e in range(0, 10):  # puts all the blank values into a list
        for f in range(0, 10):
            if grid[e][f] == 0:
                blanks.append([e, f])


def printList():#prints out the 2d grid
    for i in range(0,10):
        out=""
        for c in range(0,10):
            out=out+str(grid2[i][c])+" "#adds the value of each line of the grid to a variable
        print(s.join(out))#prints each line of the grid without any quotation marks or square brackets
#printList() #prints the blank grid initially for the user at the start of the game

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


def gencanvas():
    global canvas
    canvas = Canvas(frame, width=500, height=500)
    canvas.pack()


def determinepos(x, y):
    changegrid(x, y)
    refreshbuttons()


def refreshbuttons():
    canvas.delete("all")
    gc.collect()
    global buttonx
    global buttony
    buttonx = -1
    buttony = -1
    buttonnumber = 0
    for d in range(50, 1000, 100):
        buttonx += 1
        buttony = -1
        for b in range(50, 1000, 100):
            buttony += 1
            e = d / 2
            c = b / 2
            buttonnumber += 1

            if grid2[buttonx][buttony] == 'x':
                button1 = Button(canvas, text="", image=bomb)
                canvas.create_window(c, e, height=50, width=50, window=button1)
                continue  # Create bomb and continue

            color = "black"
            if grid2[buttonx][buttony] == 1:
                color = "blue"
            elif grid2[buttonx][buttony] == 2:
                color = "green"
            elif grid2[buttonx][buttony] == 3:
                color ="red"
            elif grid2[buttonx][buttony] == 4:
                color ="#00008B"
            elif grid2[buttonx][buttony] == 5:
                color ="#8B0000"
            elif grid2[buttonx][buttony] == 6:
                color ="#40E0D0"
            elif grid2[buttonx][buttony] == 7:
                color ="black"
            elif grid2[buttonx][buttony] == 8:
                color ="#D3D3D3"

            button1 = Button(canvas,
                             command=lambda buttonx2=buttonx, buttony2=buttony: determinepos(buttonx2, buttony2),
                             text=grid2[buttonx][buttony], font=("Courier", 44), fg=color)
            canvas.create_window(c, e, height=50, width=50, window=button1)
    root.update()


def resetgrids2():
    global firstgo
    resetgrids()
    refreshbuttons()


resetgrids()
endgame = False

# gui stuff:
root = Tk()
frame = Frame(root)

HEIGHT = 30
WIDTH = 30
path = "bomb.jpg"
thumbnail = Image.open(path)
thumbnail.thumbnail((HEIGHT, WIDTH), Image.ANTIALIAS)
bomb = ImageTk.PhotoImage(thumbnail)

label1 = Label(text="Minesweeper")
label1.pack(side=TOP)
frame.pack()

buttonnumber = 0
buttonx = -1
buttony = -1
gencanvas()
resetbutton = Button(frame, text="reset", command=resetgrids2)
resetbutton.pack(side=BOTTOM)
refreshbuttons()
root.mainloop()
