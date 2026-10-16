from tkinter import *
import copy
from operator import itemgetter

borad = [
    ['', '', ''],
    ['', '', ''],
    ['', '', ''],
]


def show():  
    print(borad[0])
    print(borad[1])
    print(borad[2])


window = Tk()
window.title("Tic Tac Toe")

FirstPlayer = 'x'
SecondPlayer = "o"
turn = "x"


def clicked(row, col):
    global FirstPlayer
    global SecondPlayer
    global turn
    if FirstPlayer == "x" and check_winner() == False:
        game_btns[row][col]['text'] = FirstPlayer
        borad[row][col] = "x"
        turn = "o"
        FirstPlayer = "o"
    elif SecondPlayer == "o" and check_winner() == False:
        game_btns[row][col]['text'] = SecondPlayer
        borad[row][col] = "o"
        turn = "x"
        FirstPlayer = "x"

    show()
    show()

    if check_winner() == True:
        label.config(text=(FirstPlayer + " loser!"))

    elif check_winner() == 'tie':
        label.config(text=("Tie, No Winner!"))

    #   if Player1 == 'O' and check_winner() == False:#دور ال AI
    #   game_btns[row][col]['text'] = FirstPlayer
    #   FirstPlayer = "X"


def start_new_game():
    for row in range(3):
        for col in range(3):
            game_btns[row][col].config(text="", bg="#F0F0F0")


def check_winner():
    # check all 3 horizontal conditions
    for row in range(3):
        if game_btns[row][0]['text'] == game_btns[row][1]['text'] == game_btns[row][2]['text'] != "":
            game_btns[row][0].config(bg="cyan")
            game_btns[row][1].config(bg="cyan")
            game_btns[row][2].config(bg="cyan")
            return True

    # check all 3 vertical conditions
    for col in range(3):
        if game_btns[0][col]['text'] == game_btns[1][col]['text'] == game_btns[2][col]['text'] != "":
            game_btns[0][col].config(bg="cyan")
            game_btns[1][col].config(bg="cyan")
            game_btns[2][col].config(bg="cyan")
            return True

    # check diagonals conditions
    if game_btns[0][0]['text'] == game_btns[1][1]['text'] == game_btns[2][2]['text'] != "":
        game_btns[0][0].config(bg="cyan")
        game_btns[1][1].config(bg="cyan")
        game_btns[2][2].config(bg="cyan")
        return True
    elif game_btns[0][2]['text'] == game_btns[1][1]['text'] == game_btns[2][0]['text'] != "":
        game_btns[0][2].config(bg="cyan")
        game_btns[1][1].config(bg="cyan")
        game_btns[2][0].config(bg="cyan")
        return True

    # if there are no empty spaces left
    if check_empty_spaces() == False:
        for row in range(3):
            for col in range(3):
                game_btns[row][col].config(bg='red')

        return 'tie'

    else:
        return False


def check_empty_spaces():
    spaces = 9

    for row in range(3):
        for col in range(3):
            if game_btns[row][col]['text'] != "":
                spaces -= 1

    if spaces == 0:  
        return False
    else:
        return True


def ai_mm_init(self):
    player = "o"
    a = -1000
    b = 1000

    borad_copy = copy.deepcopy(self.borad)

    best_outcome = -100

    best_move = None

    for i in range(9):
        if borad_copy[i] == " ":
            borad_copy[i] = player
            val = self.minimax(self.get_enemy(player), borad_copy, a, b)
            borad_copy[i] = " "
            if player == "o":
                if val > best_outcome:
                    best_outcome = val
                    best_move = i
            else:
                if val < best_outcome:
                    best_outcome = val
                    best_move = i

    self.make_move(best_move)


restart_btn = Button(text="restart", font=('consolas', 20),
                        command=start_new_game)  
restart_btn.pack(side="top")  

label = Label(text=(FirstPlayer + " turn"), font=('consolas', 30))
label.pack(side="top")

game_btns = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
btns_frame = Frame(window)  
btns_frame.pack()

for row in range(3):  
    for col in range(3):
        game_btns[row][col] = Button(btns_frame, text="", font=('consolas', 20), width=3, height=3,
                                        command=lambda row=row, col=col: clicked(row,
                                                        col))  
        game_btns[row][col].grid(row=row, column=col)  

window.mainloop()  