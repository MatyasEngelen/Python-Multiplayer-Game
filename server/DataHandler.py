import sqlite3

def MessageSort(Message):
    match Message:
        case "EnterQueue":
            print("enter ok")
        case _:
            print("Err message sort, invalid data")

def JoinQueue():
    #where to store database
    con = sqlite3.connect('C:\coding\gamefr\Python-Multiplayer-Game\Database\queue.db')
    