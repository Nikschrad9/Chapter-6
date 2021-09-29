from tkinter import *
from tkinter import ttk

def exitApp():
    # exitApp function
    # takes no parameters
    # returns no values
    # ends the program
    
    root.destroy()
    
# set up the window and name it 'Rock Paper Scissor Lizard Spock'
root = Tk()
root.title('Rock Paper Scissor Lizard Spock')
root.minsize(1000, 600)

gameDisplay = Canvas(root, height=400, width=1000, bd=5)
gameDisplay.place(x=0, y=50)

# create the images
rockPic = PhotoImage(file='rock.png')
paperPic = PhotoImage(file='paper.png')
scissorsPic = PhotoImage(file='scissors.png')
lizardPic = PhotoImage(file='lizard.png')
spockPic = PhotoImage(file='spock.png')

# create the buttons, put the images on them, and place them
rockButton = Button(root, image=rockPic, bd=5)
rockButton.place(x=0, y=410)

paperButton = Button(root, image=paperPic)
paperButton.place(x=200, y=410)

scissorsButton = Button(root, image=scissorsPic)
scissorsButton.place(x=400, y=410)

lizardButton = Button(root, image=lizardPic)
lizardButton.place(x=600, y=410)

spockButton = Button(root, image=spockPic)
spockButton.place(x=800, y=410)

# start the programs main loop
root.mainloop()