from tkinter import *
from tkinter import ttk
import random

def exitApp():
    # exitApp function
    # takes no parameters
    # returns no values
    # ends the program
    
    root.destroy()
    
def randomChoice():
    
    randNum = random.randint(0, 4)
    
    if randNum == 0:
        
    
def rock():
    
    gameDisplay.delete(ALL)
    
    gameDisplay.create_image(800, 100, image=rockPic, anchor=W)
    
def paper():
    
    gameDisplay.delete(ALL)
    
    gameDisplay.create_image(800, 100, image=paperPic, anchor=W)
    
def scissors():
    
    gameDisplay.delete(ALL)
    
    gameDisplay.create_image(800, 100, image=scissorsPic, anchor=W)
    
def lizard():
    
    gameDisplay.delete(ALL)
    
    gameDisplay.create_image(800, 100, image=lizardPic, anchor=W)
    
def spock():
    
    gameDisplay.delete(ALL)
    
    gameDisplay.create_image(800, 100, image=spockPic, anchor=W)
    
# set up the window and name it 'Rock Paper Scissor Lizard Spock'
root = Tk()
root.title('Rock Paper Scissor Lizard Spock')
root.minsize(1000, 600)

# create a canvas to hold the choices of the AI and the player
gameDisplay = Canvas(root, bg='#497ce3', height=350, width=1000)
gameDisplay.place(x=-2, y=20)

# create the images
rockPic = PhotoImage(file='rock.png')
paperPic = PhotoImage(file='paper.png')
scissorsPic = PhotoImage(file='scissors.png')
lizardPic = PhotoImage(file='lizard.png')
spockPic = PhotoImage(file='spock.png')

# create the buttons, put the images on them, and place them
# ---------------------------------------------------------------------------
rockButton = Button(root, image=rockPic, command=rock, bd=3)
rockButton.place(x=0, y=410)

paperButton = Button(root, image=paperPic, command=paper, bd=3)
paperButton.place(x=200, y=410)

scissorsButton = Button(root, image=scissorsPic, command=scissors, bd=3)
scissorsButton.place(x=400, y=410)

lizardButton = Button(root, image=lizardPic, command=lizard, bd=3)
lizardButton.place(x=600, y=410)

spockButton = Button(root, image=spockPic, command=spock, bd=3)
spockButton.place(x=800, y=410)
# ---------------------------------------------------------------------------

# gameDisplay.create_image(10, 100, image=spockPic, anchor=W)

# start the programs main loop
root.mainloop()