#-----------import for run window-------------
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import winsound
from random import randrange
from random import randint, choice
import pygame
import threading 
from pygame import mixer
import time


# ----------Create the Tkinter window-------------
window = tk.Tk()
window.title('Deepdive-Game')
window.attributes('-fullscreen', True)

SCREEN_WIDTH = 3000
SCREEN_HEIGHT = 900
GRAVITY_FORCE = 9
JUMP_FORCE = 300
SPEED = 6
TIMED_LOOP = 10



# ------------- Variables ---------------------

frame = tk.Frame(window, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
frame.pack()

canvas = tk.Canvas(frame, width=SCREEN_WIDTH, height=SCREEN_HEIGHT,  scrollregion= (0,0,4000,5000))
canvas.pack()

#---------scrollbar-----------

scrollbar_bottom = tk.Scrollbar(window, orient='horizontal', command=canvas.xview)
canvas.configure(xscrollcommand=scrollbar_bottom.set)
scrollbar_bottom.place(relx=0, rely=1, relwidth=1, anchor='sw')

#-----------create image-----------

bom_image = Image.open('images/bom.png')
bom_resize = bom_image.resize((70,70))
img_bom =ImageTk.PhotoImage(bom_resize)

bom2_image = Image.open('images/bom2.png')
img_bom2 =ImageTk.PhotoImage(bom2_image)

bg1_image = Image.open('images/bg1.png')
img_bg1 =ImageTk.PhotoImage(bg1_image)

#..............group dimond image..............

dimond1_image = Image.open('images/dimond/dimond.gif')
dimond1_resize = dimond1_image.resize((50,60))
img_dimond1 =ImageTk.PhotoImage(dimond1_resize)

dimond2_image = Image.open('images/dimond/dimond2.gif')
dimond2_resize = dimond2_image.resize((30,40))
img_dimond2 =ImageTk.PhotoImage(dimond2_resize)

#..........box.........

box1_image = Image.open('images/box/box.png')
box1_resize = box1_image.resize((60,60))
img_box1 =ImageTk.PhotoImage(box1_resize)

#...........enemies..............

shark1_image = Image.open('images/enemies/enemy1.gif')
shark1_resize = shark1_image.resize((250,100))
img_shark1 =ImageTk.PhotoImage(shark1_resize)

shark2_image = Image.open('images/enemies/enemy2 1.png')
shark2_resize = shark2_image.resize((250,100))
img_shark2 =ImageTk.PhotoImage(shark2_resize)

shark3_image = Image.open('images/enemies/animate1.png')
shark3_resize = shark3_image.resize((250,100))
img_shark3 =ImageTk.PhotoImage(shark3_resize)

#.........fishes small............

fish1_image = Image.open('images/fishes/fish.png')
fish1_resize = fish1_image.resize((250,120))
img_fish1 =ImageTk.PhotoImage(fish1_resize)

fish2_image = Image.open('images/fishes/fish1.gif')
fish2_resize = fish2_image.resize((100,50))
img_fish2 =ImageTk.PhotoImage(fish2_resize)

fish4_image = Image.open('images/fishes/fish3.gif')
fish4_resize = fish4_image.resize((150,100))
img_fish4 =ImageTk.PhotoImage(fish4_resize)

fish5_image = Image.open('images/fishes/fish4.gif')
fish5_resize = fish5_image.resize((150,80))
img_fish5 =ImageTk.PhotoImage(fish5_resize)

fish6_image = Image.open('images/fishes/fish5.gif')
fish6_resize = fish6_image.resize((130,80))
img_fish6 =ImageTk.PhotoImage(fish6_resize)

fish7_image = Image.open('images/fishes/fish6.gif')
fish7_resize = fish7_image.resize((150,80))
img_fish7 =ImageTk.PhotoImage(fish7_resize)

fish8_image = Image.open('images/fishes/fish7.gif')
fish8_resize = fish8_image.resize((200,150))
img_fish8 =ImageTk.PhotoImage(fish8_resize)

fish9_image = Image.open('images/fishes/fish8.png')
fish9_resize = fish9_image.resize((200,150))
img_fish9 =ImageTk.PhotoImage(fish9_resize)

#-----------grass image--------------

grass1_image = Image.open('images/grasses/grass1.gif')
grass1_resize = grass1_image.resize((100,300))
img_grass1 =ImageTk.PhotoImage(grass1_resize)

grass2_image = Image.open('images/grasses/grass1.gif')
grass2_resize = grass2_image.resize((100,300))
img_grass2 =ImageTk.PhotoImage(grass2_resize)

grass3_image = Image.open('images/grasses/grass1.gif')
grass3_resize = grass3_image.resize((100,250))
img_grass3 =ImageTk.PhotoImage(grass3_resize)

grass4_image = Image.open('images/grasses/grass4.png')
grass4_resize = grass4_image.resize((100,100))
img_grass4 =ImageTk.PhotoImage(grass4_resize)

grass6_image = Image.open('images/grasses/grass6.gif')
grass6_resize = grass6_image.resize((200,150))
img_grass6 =ImageTk.PhotoImage(grass6_resize)

grass7_image = Image.open('images/grasses/grass7.png')
grass7_resize = grass7_image.resize((200,150))
img_grass7 =ImageTk.PhotoImage(grass7_resize)

#-------------stones image----------------

stone1_image = Image.open('images/stones/stone1.png')
stone1_resize = stone1_image.resize((80,70))
img_stone1 =ImageTk.PhotoImage(stone1_resize)

stone2_image = Image.open('images/stones/stone2.png')
stone2_resize = stone2_image.resize((80,70))
img_stone2 =ImageTk.PhotoImage(stone2_resize)

stone3_image = Image.open('images/stones/stone3.png')
stone3_resize = stone3_image.resize((80,70))
img_stone3 =ImageTk.PhotoImage(stone3_resize)

#----------bom--------------

bom3_image = Image.open('images/bom3.png')
bom3_resize = bom3_image.resize((50,300))
img_bom3 =ImageTk.PhotoImage(bom3_resize)

#---------image flag-------------

flag_image = Image.open('images/flag.png')
flag_resize = flag_image.resize((80,90))
img_flag =ImageTk.PhotoImage(flag_resize)

#------------------create canvas image bg------------------

canvas.create_image(600,300, image =img_bg1)
canvas.create_image(1800,300, image =img_bg1)
canvas.create_image(3000,300, image =img_bg1)
canvas.create_image(4000,300, image =img_bg1)
flag_id = canvas.create_image(3900, 670, image = img_flag, tags= 'FLAG')

#------------canvas image border bottom--------------

image_list = []
for i in range(11):
    border_bottom_image = Image.open('images/border_bottom.jpg')
    img_bottom= ImageTk.PhotoImage(border_bottom_image)
    image_list.append(img_bottom)

# -----------Iterate over the list of PhotoImage objects and create a create_image() item for each image.-----------

x=0
y=750
for img in image_list:
    canvas.create_image(x, y, image=img, tag="PLATFORM")
    x+=400

# --------------------------Create a falling object (boms)--------------------------

bom_id = canvas.create_image(190, 200, image = img_bom, tags= 'BOM')
bom2_id = canvas.create_image(500, 685, image = img_bom2, tags = 'BOM')
bom3_id = canvas.create_image(1500, 150, image = img_bom3, tags = 'BOM')
bom3_id = canvas.create_image(2900, 130, image = img_bom3, tags = 'BOM')


#----------Anime on bubble water------------

bubble_img = Image.open('images/bubbles/bubble1.png')
bubble_id=ImageTk.PhotoImage(bubble_img)
image_bubble_list = []
for i in range(100):
    bubble_img = Image.open('images/bubbles/bubble1.png')
    bubble1 =ImageTk.PhotoImage(bubble_img)
    image_bubble_list.append(bubble1)
    
# -----Iterate over the list of PhotoImage objects and create a create_image() item for each image.----

x=0
y=0
for image in image_bubble_list:
    canvas.create_image(x, y, image=image, tag="BUBBLE")
    x+=500
    y+=100
    
# -----Function to update the object's position-----

def update_position_down():
    bubble_coods = canvas.coords('BUBBLE')

    if bubble_coods[1]< 500:
        canvas.move('BUBBLE', 0, 3)
        
        window.after(50, update_position_down)
    else:
        update_position_up()

def update_position_up():
    bubble_coods = canvas.coords('BUBBLE')
    if bubble_coods[1]> -300 :
        canvas.move('BUBBLE', 0, -2)
        window.after(30, update_position_up)
    else:
        update_position_down()

window.after(30, update_position_up)

# Iterate over the list of PhotoImage objects and create a create_image() item for each image.

canvas.create_image(2000, 400, image=img_shark1, tag="ENEMY")
canvas.create_image(500, 200, image=img_shark1, tag="ENEMY")

# Function to update the object's position

def update_position_right():
    fish_coods = canvas.coords('ENEMY')
    if fish_coods[0]< 4000:
        canvas.itemconfigure('ENEMY', image = img_shark2 )
        canvas.move('ENEMY', 3, 0)
        window.after(20, update_position_right)
    else:
        update_position_left()

def update_position_left():
    fish_coods = canvas.coords('ENEMY')
    if fish_coods[0]> -150 :
        canvas.itemconfigure('ENEMY', image = img_shark1 )
        canvas.move('ENEMY', -3, 0)
        window.after(20, update_position_left)
    else:
        update_position_right()

window.after(20, update_position_right)

#--------------------------Create a falling object (stones)--------------------------

stone3_id = canvas.create_image(1000, 685, image = img_stone3, tags= 'STONE')
stone2_id = canvas.create_image(2000, 685, image = img_stone2, tags= 'STONE')
stone3_id = canvas.create_image(2900, 685, image = img_stone3, tags= 'STONE')
stone1_id = canvas.create_image(200, 685, image = img_stone1, tags= 'STONE')

#--------------------------Create a falling object (dimond1)--------------------------

dimond1_id = canvas.create_image(700, 690, image = img_dimond1, tags= 'DIAMOND')
dimond1_id = canvas.create_image(3000, 690, image = img_dimond1, tags= 'DIAMOND')
dimond1_id = canvas.create_image(1700, 297, image = img_dimond1, tags= 'DIAMOND')
dimond1_id = canvas.create_image(3000, 245, image = img_dimond1, tags= 'DIAMOND')

# # Create a falling object (fishes)

# fish2_id = canvas.create_image(100, 200, image = img_fish2, tags='FISHL')
fish4_id = canvas.create_image(250, 500, image = img_fish4, tags='FISH')
fish4_id = canvas.create_image(1200, 100, image = img_fish4, tags='FISH')
fish5_id = canvas.create_image(900, 690, image = img_fish5, tags='FISH')
fish6_id = canvas.create_image(1200, 400, image = img_fish6, tags='FISH')
fish6_id = canvas.create_image(700, 200, image = img_fish6, tags='FISH')
fish7_id = canvas.create_image(800, 300, image = img_fish7, tags='FISH')
fish9_id = canvas.create_image(300, 300, image = img_fish9, tags='FISH')

# Function to update the object's position
def update_position_rights():
    fish_coods = canvas.coords('FISH')
    if fish_coods[0]< 4000:
        canvas.move('FISH', 4, 0)
        window.after(20, update_position_rights)
    else:
        update_position_lefts()

def update_position_lefts():
    fish_coods = canvas.coords('FISH')
    if fish_coods[0]> -150 :
        canvas.move('FISH', -5, 0)
        window.after(20, update_position_lefts)
    else:
        update_position_rights()

window.after(20, update_position_rights)

# --------------------------Create a falling object (box)--------------------------

box1_id = canvas.create_image(595, 690, image = img_box1,tags='BOX')
box1_id = canvas.create_image(650, 690, image = img_box1,tags='BOX')
box1_id = canvas.create_image(650, 635, image = img_box1,tags='BOX')

box1_id = canvas.create_image(1250, 690, image = img_box1,tags='BOX')
box1_id = canvas.create_image(1300, 690, image = img_box1,tags='BOX')
box1_id = canvas.create_image(1300, 635, image = img_box1,tags='BOX')
box1_id = canvas.create_image(1350, 690, image = img_box1,tags='BOX')
box1_id = canvas.create_image(1350, 635, image = img_box1,tags='BOX')
box1_id = canvas.create_image(1350, 580, image = img_box1,tags='BOX')

box1_id = canvas.create_image(2000, 690, image = img_box1,tags='BOX')
box1_id = canvas.create_image(2080, 630, image = img_box1,tags='BOX')
box1_id = canvas.create_image(2140, 630, image = img_box1,tags='BOX')
box1_id = canvas.create_image(2200, 630, image = img_box1,tags='BOX')
box1_id = canvas.create_image(2260, 630, image = img_box1,tags='BOX')

box1_id = canvas.create_image(2800, 690, image = img_box1,tags='BOX')
box1_id = canvas.create_image(3333, 690, image = img_box1,tags='BOX')
box1_id = canvas.create_image(3460, 690, image = img_box1,tags='BOX')

box1_id = canvas.create_image(3000, 300, image = img_box1,tags='BOX')
box1_id = canvas.create_image(3070, 300, image = img_box1,tags='BOX')
box1_id = canvas.create_image(1700, 350, image = img_box1,tags='BOX')
box1_id = canvas.create_image(1700, 400, image = img_box1,tags='BOX')
box1_id = canvas.create_image(1700, 450, image = img_box1,tags='BOX')
box1_id = canvas.create_image(1700, 500, image = img_box1,tags='BOX')
box1_id = canvas.create_image(1700, 550, image = img_box1,tags='BOX')
box1_id = canvas.create_image(1700, 600, image = img_box1,tags='BOX')
box1_id = canvas.create_image(1700, 650, image = img_box1,tags='BOX')
box1_id = canvas.create_image(1700, 690, image = img_box1,tags='BOX')
box1_id = canvas.create_image(1700, 200, image = img_box1,tags='BOX')

# ..................dimond​​ score.............
canvas.create_text(800, 50, text=": 0", font=("bold", 20), fill="white", tags = 'SCORE')
dimond2_id = canvas.create_image(760, 48, image = img_dimond2)

## .................Level...............

score_id = canvas.create_text(600, 50, text="Level : 1 ", font=("bold", 20), fill="white")


# ------------------Function to update the object's position ------------------

xspeed=3
yspeed=3
def moveBom():
    global xspeed
    global yspeed
    canvas.move(bom_id, xspeed, yspeed)
    leftPos = canvas.coords(bom_id)
    topPos = canvas.coords(bom_id)
    rightPos = canvas.coords(bom_id)
    bottomPos = canvas.coords(bom_id)

    if rightPos[0] > SCREEN_WIDTH or leftPos[0] < 0:
        xspeed = -xspeed

    if bottomPos[1] > SCREEN_HEIGHT-200 or topPos[1] < 0  :
        yspeed = -yspeed
    canvas.after(10, moveBom)
canvas.after(10, moveBom)

#...................Sound............................

pygame.mixer.init()
sound = pygame.mixer.Sound('images/sounds/song1.mp3')
def play_sound():
    while True:
        sound.play()
        pygame.time.wait(int(sound.get_length() * 1000))
sound_thread = threading.Thread(target=play_sound)
sound_thread.start()

#------------------create player------------------

X_VELOCITY = 9
Y_VELOCITY = 9

player1_img=Image.open('images/players/player1.png')
player1_id = ImageTk.PhotoImage(player1_img)
player1 = canvas.create_image(150, 653, image=player1_id , tags='PLAYER')

player2_img =Image.open('images/players/player2.png')
resize_player2=player2_img.resize((250, 200))
player2_id = ImageTk.PhotoImage(resize_player2)

player3_img =Image.open('images/players/player_right1.png')
resize_player3 = player3_img.resize((150,120))
player3_id = ImageTk.PhotoImage(resize_player3)

player4_img =Image.open('images/players/player_down.png')
resize_player4 = player4_img.resize((250, 200))
player4_id = ImageTk.PhotoImage(resize_player4)


# #Gravity
# #-------------Function----------------

# #Check if the player can move by projecting the movement with dx and dy
# #If checkground is True, check if the player is on the ground by projecting the movement with the last coordinate
# #Instead of getting the platform list with canvas. Find_withtag("PLATFORM"), we could have used a global list
# #Return True if the player can move (i.e is not near any wall), False otherwise

# def check_movement(dx=0, dy=0, checkGround=False):
#     coord = canvas.coords(player1)
#     platforms = canvas.find_withtag("PLAYER")

#     if coord[0] + dx < 0 or coord[0] + player1_id.width() > SCREEN_WIDTH:
#         return False
    
#     if checkGround:
#         overlap = canvas.find_overlapping(coord[0], coord[1], coord[0], coord[1]+ player1_id.height())
#     else:
#         overlap = canvas.find_overlapping(coord[0] +dx, coord[1]+dy, coord[0]+player1_id.width(), coord[1]+player1_id.height())
#     # print(overlap)
#     for platform in platforms:
#         if platform in overlap:
#             return False
#     return True

# #Jump by moving the player up by player
# #Only if the player can move up
# #The force paremeter is always decreasing by 1 until it reach 0
# #The force should be higher than the gravity force to be able

# def jump(force):
#     if force > 0:
#         if not check_movement(0, -force):
#             canvas.move(player1, 0, -force)
#             window.after(TIMED_LOOP, jump, force-1)

# #The start_move function is called when a key is pressed
# #It adds the key to the keypressed lish if it's not already in it
# #If the keypressed lish was empty, it calls move function

# def start_move(event):
#     if event.keysym not in keyPressed:
#         keyPressed.append(event.keysym)
#         if len(keyPressed) == 1:
#             move()

# #The move function is called every TIME_LOOP milliseconds
# #It checks if the player can move in the direction of the keyPressed lish
# #It also check if the player is on the ground before jumping

# def move():
#     if not keyPressed ==[]:
#         x = 0
#         if "Left" in keyPressed:
#             x -= SPEED
#             canvas.itemconfig(player1, image=player4_id)
#         elif "Right" in keyPressed:
#             x += SPEED
#             canvas.itemconfig(player1, image=player3_id)
#         elif "space" in keyPressed and not check_movement(0, GRAVITY_FORCE, True):
#             jump(JUMP_FORCE)
#         if not check_movement(x):
#             canvas.move(player1, x, 0)
#         window.after(TIMED_LOOP, move)

# #The gravity function is called every TIME_LOOP milliseconds
# #It checks if the player can move down by GRAVITY_FORCE 
# #It is always looping, even if the player can't move down
# def gravity():
#     if check_movement(0, GRAVITY_FORCE, True):
#         canvas.move(player1, 0, GRAVITY_FORCE)
#     window.after(TIMED_LOOP, gravity)

# gravity()

# #The stop _move function is called when a key is released
# #It removes the key from the keyPress lish
# def stop_move(event):
#     global keyPressed
#     if event.keysym in keyPressed:
#         keyPressed.remove(event.keysym)


# ------------------touch ------------------

def move_player1():
    coords= canvas.coords(player1)
    players1=canvas.find_withtag('DIAMOND')
    overlap1= canvas.find_overlapping(coords[0], coords[1], coords[0]+player1_id.width(), coords[1]+player1_id.height())
    for py1 in players1:
        if py1 in overlap1:
            return py1
    return 0

def move_player2():
    coords= canvas.coords(player1)
    players2=canvas.find_withtag('FLAG')
    overlap2= canvas.find_overlapping(coords[0], coords[1], coords[0]+player1_id.width(), coords[1]+player1_id.height())
    for py2 in players2:
        if py2 in overlap2:
            return py2
    return 0

def game_lose():
    index =canvas.coords(player1)
    boms=canvas.find_withtag('BOM')
    over=canvas.find_overlapping(index[0], index[1], index[0]+img_bom.width(), index[1]+img_bom.height())
    for bom in boms:
        if bom in over:
            return True
    return False

def game_lose1():
    index =canvas.coords(player1)
    boms=canvas.find_withtag('ENEMY')
    over=canvas.find_overlapping(index[0], index[1], index[0]+img_bom.width(), index[1]+img_bom.height())
    for bom in boms:
        if bom in over:
            return True
    return False

#  ------------------Window lose imge ------------------

game =Image.open('images/bg1.png')
lose = ImageTk.PhotoImage(game)

game_over =Image.open('images/game_over.png')
over = ImageTk.PhotoImage(game_over)

died =Image.open('images/died.png')
resize =died.resize((120,100))
player_died = ImageTk.PhotoImage(resize)

# ------------------Win image ------------------

game_win =Image.open('images/winner.png')
win = ImageTk.PhotoImage(game_win)

# ------------------Window lose ------------------

def lose_window():
    canvas.delete('all')
    canvas.create_image(400,300, image= lose, tags= 'LOSE')
    canvas.create_image(900,300, image= lose, tags= 'LOSE')
    canvas.create_image(670,400, image= over, tags= 'LOSE')
    canvas.itemconfigure(player1, image =player_died)
    canvas.create_image(110, 100, image=btn_back_game, tags="back")

# ------------------put sound ------------------

    mixer.init()
    mixer.music.load('images/sounds/lose.mp3')
    mixer.music.play()
    time.sleep(2)
    mixer.music.stop()

def win_window():
    canvas.delete('all')
    canvas.create_image(400,300, image= lose, tags= 'WIN')
    canvas.create_image(900,300, image= lose, tags= 'WIN')
    canvas.create_image(670,400, image= game_win, tags= 'WIN')
    canvas.itemconfigure(player1, image =player_died)
    canvas.create_image(110, 100, image=btn_back_game, tags="back")

# ------------------put sound ------------------

    mixer.init()
    mixer.music.load('images/sounds/winner.mp3')
    mixer.music.play()
    time.sleep(1.5)
    mixer.music.stop()

#  ------------------Create a falling object (grasses) ------------------

grass1_id = canvas.create_image(1200, 565, image = img_grass1)
grass2_id = canvas.create_image(2385,565, image = img_grass2)
grass3_id = canvas.create_image(3400, 590, image = img_grass3)
grass6_id = canvas.create_image(400, 650, image = img_grass6)
grass6_id = canvas.create_image(1800, 650, image = img_grass6)
grass6_id = canvas.create_image(3200, 650, image = img_grass6)
grass7_id = canvas.create_image(1500, 700, image = img_grass7)
grass7_id = canvas.create_image(2600, 700, image = img_grass7)
grass7_id = canvas.create_image(3600, 700, image = img_grass7)

def is_border_left():
        return canvas.coords(player1)[0] < 30

def is_border_right():
        return canvas.coords(player1)[0] > 4000

def is_border_top():
        return canvas.coords(player1)[1] < 30

def is_border_bottom():
        return canvas.coords(player1)[1] > 653
score = 0
def move_shape(event):
    global score
    if event.keysym == "Left" and not is_border_left():
        canvas.move(player1, -10, 0)
        canvas.itemconfigure(player1, image = player2_id)
    elif event.keysym == "Right" and not is_border_right():
        canvas.move(player1, 10, 0)
        canvas.itemconfigure(player1, image = player1_id)
    elif event.keysym == "Up" and not is_border_top():
        canvas.move(player1, 0, -10)
        canvas.itemconfigure(player1, image= player3_id)
    elif event.keysym == "Down" and not is_border_bottom():
        canvas.move(player1, 0, 10)
        canvas.itemconfigure(player1, image=player4_id)
    shape1 = move_player1()
    shape2 = move_player2()
    if  game_lose():
        lose_window()
    if game_lose1():
        lose_window()

    if shape1>0:
        canvas.delete(shape1)
        mixer.init()
        mixer.music.load('images/sounds/got.mp3')
        mixer.music.play()
        time.sleep(0.7)
        mixer.music.stop()

    # sum score

        score+=1
        canvas.itemconfigure('SCORE', text=(":" +str(score)))
    if shape2>0:
        canvas.delete(shape2)
        win_window()

#------------------Gravity------------------

# ------------------No auto scroll ------------------

def scroll_right(event):
    canvas.xview('scroll', 1, 'units')

def scroll_left(event):
    canvas.xview('scroll', -1, 'units')

window.bind("<Key>", move_shape)


# ------------------Varaible ------------------

game_start = tk.PhotoImage(file="images/menus/bg_start.png")
# game_bg = tk.PhotoImage(file="images/menus/bg.png")
# game_level = tk.PhotoImage(file="images/menus/bg_level.png")

btn_menus_game = tk.PhotoImage(file="images/menus/menus 1.png")
btn_start_game = tk.PhotoImage(file="images/menus/start_menu.png")
btn_continue_game = tk.PhotoImage(file="images/menus/continue_menu.png")
btn_exit_game = tk.PhotoImage(file="images/menus/exit_menu.png")
btn_back_game = tk.PhotoImage(file="images/menus/back_menu.png")

##----back------
canvas.create_image(110, 100, image=btn_back_game, tags="back")
# level1 = tk.PhotoImage(file="images/menus/level1.png")
# level2 = tk.PhotoImage(file="images/menus/level2.png")
# level3 = tk.PhotoImage(file="images/menus/level3.png")

# #------------------Show start game ------------------
def gameShow(event):
    canvas.delete("all")
    canvas.create_image(680, 372, image=game_start)
    canvas.create_image(660,100, image=btn_menus_game, tags="menusgame")
    canvas.create_image(660,280, image=btn_start_game, tags="startgame")
    canvas.create_image(660,420, image=btn_continue_game, tags="continue")
    canvas.create_image(655,550,image=btn_exit_game, tags="exit")

## ------------------show level game ------------------

# def levelGame(event):
#     canvas.delete(all)
#     canvas.create_image(680,372, image=game_level)
#     canvas.create_image(250,372, image=level1, tags = 'level1')
#     canvas.create_image(670,372, image=level2)
#     canvas.create_image(1100,372, image=level3)
#     canvas.create_image(110, 100, image=btn_back_game, tags="back")

## ------------------level1 of game ------------------

# def showLevel1(event):
#     canvas.create_image(50,60, image = img_bg1)  


# #------------------show for how to play ------------------

# def gameHelp(event):
#     canvas.delete("all")
#     canvas.create_image(680, 372, image=game_bg)
#     canvas.create_image(110, 200, image=btn_back_game, tags="back")

# #------------------close game ------------------

# def gameExit(event):
#     window.destroy()

##------------------display winner ------------------

# canvas.create_image(680, 372, image=game_start)
# canvas.create_image(660,100, image=btn_menus_game, tags="menusgame")
# canvas.create_image(660,280, image=btn_start_game, tags="startgame")
# canvas.create_image(660,420, image=btn_continue_game, tags="continue")
# canvas.create_image(655,550,image=btn_exit_game, tags="exit")
# # winsound.PlaySound("images/sounds/start.mp3",winsound.SND_FILENAME | winsound.SND_ASYNC)


## ------------------Bind the button clicks to the corresponding functions------------------

# canvas.tag_bind("startgame", "<Button-1>",levelGame )
# canvas.tag_bind("continue", "<Button-1>",levelGame )
# canvas.tag_bind("exit", "<Button-1>", gameExit)
canvas.tag_bind("back", "<Button-1>", lose_window)
canvas.tag_bind("back", "<Button-1>", win_window)
# canvas.tag_bind("level1", "<Button-1>", showLevel1)




# canvas.pack(expand=True, fill='both')

window.mainloop()