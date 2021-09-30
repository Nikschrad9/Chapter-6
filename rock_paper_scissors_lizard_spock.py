from tkinter import *
from tkinter import ttk
import random

def exitApp():
    # exitApp function
    # takes no parameters
    # returns no values
    # ends the program
    
    root.destroy()
    
def randomChoice(playerChoice):
    
    # holds the choices that the random number will choose from
    choices = ['rock','paper','scissors','lizard','spock']
    choicePics = [rockPic, paperPic, scissorsPic, lizardPic, spockPic]
    
    # generate a random number to select the AI's choice
    randNum = random.randint(0, 4)
    
    # store the choice in the choice variable
    choice = choices[randNum]
    
    gameDisplay.create_image(10, 100, image=choicePics[randNum], anchor=W)
    
    if choice == playerChoice:
        
        winnerText.set("It's a tie.")
        
    elif choice == 'rock':
        
        if playerChoice == 'scissors' or playerChoice == 'lizard':
            winnerText.set('You lose!')
        else:
            winnerText.set('You win!')
        
    elif choice == 'paper':
        
        if playerChoice == 'rock' or playerChoice == 'spock':
            winnerText.set('You lose!')
        else:
            winnerText.set('You win!')
        
    elif choice == 'scissors':
        
        if playerChoice == 'paper' or playerChoice == 'lizard':
            winnerText.set('You lose!')
        else:
            winnerText.set('You win!')
        
    elif choice == 'lizard':
        
        if playerChoice == 'paper' or playerChoice == 'spock':
            winnerText.set('You lose!')
        else:
            winnerText.set('You win!')
        
    else:
        
        if playerChoice == 'scissors' or playerChoice == 'rock':
            winnerText.set('You lose!')
        else:
            winnerText.set('You win!')
    
    
def rock():
    
    # clear the canvas
    gameDisplay.delete(ALL)
    
    gameDisplay.create_image(800, 100, image=rockPic, anchor=W)
    
    randomChoice('rock')
    
def paper():
    
    # clear the canvas
    gameDisplay.delete(ALL)
    
    gameDisplay.create_image(800, 100, image=paperPic, anchor=W)
    
    randomChoice('paper')
    
def scissors():
    
    # clear the canvas
    gameDisplay.delete(ALL)
    
    gameDisplay.create_image(800, 100, image=scissorsPic, anchor=W)
    
    randomChoice('scissors')
    
def lizard():
    
    # clear the canvas
    gameDisplay.delete(ALL)
    
    gameDisplay.create_image(800, 100, image=lizardPic, anchor=W)
    
    randomChoice('lizard')
    
def spock():
    
    # clear the canvas
    gameDisplay.delete(ALL)
    
    gameDisplay.create_image(800, 100, image=spockPic, anchor=W)
    
    randomChoice('spock')
    
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

# create a new font style
fontStyle = font.Font(family="Helvetica", size=15)

# label text variable
winnerText = StringVar()

# create a label to show to the winner, place it in the grid, and center it
winnerLabel = Label(root, textvariable=winnerText, height=5, width=50, bg='#497ce3', fg='white', font=fontStyle)
winnerLabel.grid(column=0, row=0)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# start the programs main loop
root.mainloop()