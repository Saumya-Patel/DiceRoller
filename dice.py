from tkinter import*

die ={
0 : '🎲',
1 : '⚀',
2 : '⚁',
3 : '⚂',
4 : '⚃',
5 : '⚄',
6 : '⚅'
}

App = Tk()
App.title('DiceRoller')
#App.geometry('500x500')
App['background'] = 'black'


dice = Label(App,text=die[0], font=('Times',200), foreground="black")
dice.grid(row=0, column=0, padx=50, pady=50)

def roll():
    from random import randint
    i = randint(1,6)
    msg =Label(App, text=die[i], font=('Times',200))
    msg.grid(row=0, column=0, padx=50, pady=50)

B = Button(App, text="ROLL", command=roll, relief='raised', background='grey', foreground='white', font=('Times', 20),borderwidth=5,width='10')
B.grid(row=2, column=0,  padx=50, pady=20)

App.mainloop()