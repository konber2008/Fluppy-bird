import tkinter as tk
import random

def jump(event):
    global canvas, player, player_y, stop_action
    if stop_action:
        return
    canvas.move(player, 0, -60)
    player_y -= 60
    if player_y < 0:
        stop_action = True

def create_obj(i):
    global canvas, objects, synt, root, x, sizeHole
    ind_hole = random.randint(150, root.winfo_screenheight()-250)
    wall1 = canvas.create_rectangle(i, 0, i+x, ind_hole, fill = "brown")
    wall2 = canvas.create_rectangle(i, ind_hole+sizeHole, i+x, root.winfo_screenheight(), fill = "brown")
    objects.append((wall1, wall2, ind_hole))
    synt.append(i)

def start():
    global canvas, synt, objects, cp, x ,y, player_y, player_x, sizeHole, player, stop_action, root, score
    if stop_action:
        print(score)
        return
    
    #Walls action
    N = len(synt)
    created = False
    for i in range(N):
        canvas.move(objects[i][0], -10, 0)
        canvas.move(objects[i][1], -10, 0)
        synt[i] -= 10
        if synt[i] <= player_x and synt[i]+x >= player_x:
            if player_y < objects[i][2]-7 or player_y + 30 > objects[i][2] + sizeHole + 7:
                print(score)
                stop_action =True
                return
        if synt[i]+x == player_x-10:
            score +=1
        if synt[i]+x+y <= 0:
            canvas.delete(objects[i][0])
            canvas.delete(objects[i][1])
            del objects[i]
            del synt[i]
            create_obj(cp)
            created = True
    if created:
        canvas.move(objects[-1][0], -10, 0)
        canvas.move(objects[-1][1], -10, 0)
        synt[-1] -= 10
    
    #Player action
    canvas.move(player, 0, 30)
    player_y += 30
    if player_y + 30 > root.winfo_screenheight():
        print(score)
        stop_action = True
        return
    canvas.after(100, start)

def start_round(event):
    global x, y, objects, synt, player_y, player_x, score, stop_action, player
    if not stop_action:
        return

    canvas.delete("all")
    objects = []
    synt = []
    player_y = 300
    stop_action = False
    for i in range(900, 900+root.winfo_screenwidth()+x+y, x+y):
        create_obj(i)
    
    player = canvas.create_oval(player_x, player_y, player_x+30, player_y+30, fill="blue")
    start()

root = tk.Tk()
canvas = tk.Canvas(root, bg="#e0e0e0")
canvas.pack(fill="both", expand=True)

x = 100
y = 200
sizeHole = 200
objects = []
synt = []
player_y = 300
player_x = 200
score = 0
stop_action = True
player = None

cp = root.winfo_screenwidth() + x+y - root.winfo_screenwidth()%(x+y)

root.bind("<Return>", start_round)
root.bind("<Up>", jump)

root.mainloop()
