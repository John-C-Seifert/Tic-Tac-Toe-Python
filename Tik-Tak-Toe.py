from tkinter import*
import random

def reset():
    label_1.config(text=' ')
    label_2.config(text=' ')
    label_3.config(text=' ')
    label_4.config(text=' ')
    label_5.config(text=' ')
    label_6.config(text=' ')
    label_7.config(text=' ')
    label_8.config(text=' ')
    label_9.config(text=' ')


def win():
    def new_game():
        new_Window.destroy()
        global x_or_o
        global player_1_score
        global player_2_score
        global player
        global turn_number
        turn_number = 0
        if player == 'Player 1':
            player_1_score +=1
            player_1.config(text='Player 1: ' + str(player_1_score))
        else:
            player_2_score +=1
            player_2.config(text='Player 2: ' + str(player_2_score))
        x_or_o = random.choices(['X', 'O'])
        player = random.choice(['Player 1', 'Player 2'])

        current_Turn.config(text='Turn:     ' + player)
        reset()


        window.update_idletasks()

    new_Window = Tk()
    new_Window.config(bg='black')

    winner_Label = Label(new_Window, text='Winner!!!\n' + str(player),font=('Arial', 96), fg='#39FF14', bg='black')
    winner_Label.pack()


    new_game = Button(new_Window, text='New Game', bg='black',fg='#39FF14', command=new_game, font=('Arial', 26))
    new_game.pack()

    new_Window.mainloop()
    window.update_idletasks()

def checkWin():
    if label_1.cget('text') == label_2.cget('text') == label_3.cget('text') == 'X':
        return True
    elif label_4.cget('text') == label_5.cget('text') == label_6.cget('text') == 'X':
        return True
    elif label_7.cget('text') == label_8.cget('text') == label_9.cget('text') == 'X':
        return True
    elif label_1.cget('text') == label_4.cget('text') == label_7.cget('text') == 'X':
        return True
    elif label_2.cget('text') == label_5.cget('text') == label_8.cget('text') == 'X':
        return True
    elif label_3.cget('text') == label_6.cget('text') == label_9.cget('text') == 'X':
        return True
    elif label_1.cget('text') == label_5.cget('text') == label_9.cget('text') == 'X':
        return True
    elif label_3.cget('text') == label_5.cget('text') == label_7.cget('text') == 'X':
        return True
    elif label_1.cget('text') == label_2.cget('text') == label_3.cget('text') == 'O':
        return True
    elif label_4.cget('text') == label_5.cget('text') == label_6.cget('text') == 'O':
        return True
    elif label_7.cget('text') == label_8.cget('text') == label_9.cget('text') == 'O':
        return True
    elif label_1.cget('text') == label_4.cget('text') == label_7.cget('text') == 'O':
        return True
    elif label_2.cget('text') == label_5.cget('text') == label_8.cget('text') == 'O':
        return True
    elif label_3.cget('text') == label_6.cget('text') == label_9.cget('text') == 'O':
        return True
    elif label_1.cget('text') == label_5.cget('text') == label_9.cget('text') == 'O':
        return True
    elif label_3.cget('text') == label_5.cget('text') == label_7.cget('text') == 'O':
        return True


def turn(event):
    widget = event.widget
    global turn_number
    global x_or_o
    global player
    widget.config(text=x_or_o)
    turn_number +=1
    window.update_idletasks()
    if(widget.cget('text') == 'X'):
        x_or_o = 'O'
    else:
        x_or_o = 'X'
    if checkWin():
        win()
        return
    if player == 'Player 1':
        player = 'Player 2'
    else:
        player = 'Player 1'
    if turn_number == 9:
        turn_number = 0
        reset()
        player = random.choice(['Player 1', 'Player 2'])
        current_Turn.config(text='Turn : ' + player)
        return
    current_Turn.config(text='Turn:     ' + player)



player_1_score = 0
player_2_score = 0
x_or_o = random.choice(['X','O'])
player = random.choice(['Player 1', 'Player 2'])
turn_number = 0

window = Tk()
window.configure(bg='black')


player_1 = Label(window, text='Player 1: '+ str(player_1_score),font=('Arial', 25, 'bold'), fg='#39FF14', bg='black')
player_1.grid(row=0, column=0)

player_2 = Label(window, text='Player 2: ' + str(player_2_score),font=('Arial', 25, 'bold'),fg='#39FF14', bg='black')
player_2.grid(row=0, column=1)

canvas = Canvas(window, width=500, height=500, bg='black')
canvas.grid(row=1, columnspan=2)

current_Turn = Label(window, text='Turn:     ' + player, fg='#39FF14', bg='black', font=('Arial', 18), pady=10)
current_Turn.grid(columnspan=2, row=2)

label_1 = Label(window, text=' ', font=('Arial', 90),fg='#39FF14', bg='black')
canvas.create_window(100,100, window=label_1, anchor=CENTER)

label_2 = Label(window, text=' ', font=('Arial', 90),fg='#39FF14', bg='black')
canvas.create_window(100,250, window=label_2, anchor=CENTER)

label_3 = Label(window, text=' ', font=('Arial', 90),fg='#39FF14', bg='black')
canvas.create_window(100,400, window=label_3, anchor=CENTER)

label_4 = Label(window, text=' ', font=('Arial', 90),fg='#39FF14', bg='black')
canvas.create_window(250,100, window=label_4, anchor=CENTER)

label_5 = Label(window, text=' ', font=('Arial', 90),fg='#39FF14', bg='black')
canvas.create_window(250,250, window=label_5, anchor=CENTER)

label_6 = Label(window, text=' ', font=('Arial', 90),fg='#39FF14', bg='black')
canvas.create_window(250,400, window=label_6, anchor=CENTER)

label_7 = Label(window, text=' ', font=('Arial', 90),fg='#39FF14', bg='black')
canvas.create_window(400,100, window=label_7, anchor=CENTER)

label_8 = Label(window, text=' ', font=('Arial', 90),fg='#39FF14', bg='black')
canvas.create_window(400,250, window=label_8, anchor=CENTER)

label_9 = Label(window, text=' ', font=('Arial', 90),fg='#39FF14', bg='black')
canvas.create_window(400,400, window=label_9, anchor=CENTER)


canvas.create_line(25, 175, 475, 175, width='8', fill='#39FF14')
canvas.create_line(25, 325, 475, 325, width='8', fill='#39FF14')

canvas.create_line(175, 25, 175, 475, width='8', fill='#39FF14')
canvas.create_line(325, 25, 325, 475, width='8', fill='#39FF14')

label_1.bind('<Button-1>', turn)
label_2.bind('<Button-1>', turn)
label_3.bind('<Button-1>', turn)
label_4.bind('<Button-1>', turn)
label_5.bind('<Button-1>', turn)
label_6.bind('<Button-1>', turn)
label_7.bind('<Button-1>', turn)
label_8.bind('<Button-1>', turn)
label_9.bind('<Button-1>', turn)


window.mainloop()