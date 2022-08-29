from audioop import add
import sqlite3

def MessageSort(Message):
    match Message:
        case "EnterQueue":
            print("enter ok")
        case _:
            print("Err message sort, invalid data")

def JoinQueue(addr):
    #where to store database
    con = sqlite3.connect('C:\coding\gamefr\Python-Multiplayer-Game\Database\queue.db')
    c = con.cursor()
                   
    c.execute('''
          INSERT INTO UserQueue (UserAddr)
                VALUES
                ({})
          '''.format(addr))