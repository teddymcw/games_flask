from flask import Flask, render_template, flash
from flask.ext.sqlalchemy import SQLAlchemy 
from forms import InputForm

#for config
import os

#instantiations needed
app = Flask(__name__)
db = SQLAlchemy(app)

#make shift config section
#    below is for CSFR prevention by wtforms
app.config['SECRET_KEY'] = 'hard to guess string'
#find this file
basedir = os.path.abspath(os.path.dirname(__file__))
#db section
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
#not sure what line below does
#app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True


#application code
#board = range(10) #should we replace with string values? ya
board = [str(num) for num in range(10)]

def print_board():   
    #print(board[:3]) adapting from cli version
    #print(board[3:6]) 
    #print(board[6:9])
    #return "top: {0}\nmid: {1}\nbot: {2}".format(board[:3], board[3:6], board[6:9]) 
    return board[:3], board[3:6], board[6:9]

def play():
    for turn in range(len(board) // 2): #we need 9 turns
        print_board()
        guess1 = int(raw_input("Player 1 enter your 'X' using corresponding integer\t"))    
        if not str(board[guess1]).isdigit(): #extra validation check
            print("that spot is already taken tho!\n you lose your turn")
        else:
            board.pop(guess1)
            board.insert(guess1, 'X')
        print_board()
        guess2 = int(raw_input("Player 2 enter you 'O' using corresponding integer\t"))
        if not str(board[guess2]).isdigit(): #extra validation check
            print("that spot is already taken tho!\n you lose your turn")
        else:
            board.pop(guess2)
            board.insert(guess2, 'O')
    return board

def win():
    pass

#play()

#routing code
@app.route("/")
def hello():
    return "board.html"

@app.route("/play", methods=["GET", "POST"])
def show_board():
    new_board = print_board()
    form=InputForm()
    if form.validate_on_submit():
        flash("you are validated")
    else:
        flash("ehhh...ehh!, form didn't go")
    return render_template("board.html", form=form, board_1=new_board[0], board_2=new_board[1], board_3=new_board[2])


if __name__ == "__main__":
    app.run(debug=True)