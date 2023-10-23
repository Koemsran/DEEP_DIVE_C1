import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import winsound
from random import randrange
from random import randint, choice

# Create the Tkinter window
window = tk.Tk()
window.title('Deepdive-Game')
window.attributes('-fullscreen', True)

SCREEN_WIDTH = 3000
SCREEN_HEIGHT = 900

GRAVITY_FORCE = 9
JUMP_FORCE = 300
SPEED = 6

TIME_LOOP = 20

# ------------- Variables ---------------------
keyPressed = []

frame = tk.Frame(window, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
frame.pack()

canvas = tk.Canvas(frame, width=SCREEN_WIDTH, height=SCREEN_HEIGHT,  scrollregion= (0,0,4000,5000))
canvas.pack()

#.....score......
score = 0

#scrollbar
scrollbar_bottom = tk.Scrollbar(window, orient='horizontal', command=canvas.xview)
canvas.configure(xscrollcommand=scrollbar_bottom.set)
scrollbar_bottom.place(relx=0, rely=1, relwidth=1, anchor='sw')

#create image

bom_image = Image.open('images/bom.png')
bom_resize = bom_image.resize((70,70))
img_bom =ImageTk.PhotoImage(bom_resize)

bom2_image = Image.open('images/bom2.png')
img_bom2 =ImageTk.PhotoImage(bom2_image)

bg1_image = Image.open('images/bg1.png')
img_bg1 =ImageTk.PhotoImage(bg1_image)

#Create image bubble water

image_bubble_list = []
for i in range(50):
    bubble1_image = Image.open('images/bubbles/bubble1.png')
    bubble1 = ImageTk.PhotoImage(bubble1_image)
    image_bubble_list.append(bubble1)
    
# Iterate over the list of PhotoImage objects and create a create_image() item for each image.
x=0
y=0
for image in image_bubble_list:
    canvas.create_image(x, y, image=image, tag="BUBBLE")
    x+=100
    y+=100
    
# Function to update the object's position
def update_position_down():
    bubble_coods = canvas.coords('BUBBLE')

    if bubble_coods[1]< 700:
        canvas.move('BUBBLE', 0, 3)
        
        window.after(50, update_position_down)
    else:
        update_position_up()

def update_position_up():
    bubble_coods = canvas.coords('BUBBLE')
    if bubble_coods[1]> -200 :
        canvas.move('BUBBLE', 0, -2)
        window.after(30, update_position_up)
    else:
        update_position_down()

window.after(30, update_position_up)




#group fish image

# image_fish_list = []
# for i in range(1,8):
#     fish_image = Image.open('images/fishes/fish'+str(i)+'.gif')
#     fish_resize = fish_image.resize((100,100))
#     img_fish =ImageTk.PhotoImage(fish_resize)
#     image_fish_list.append(img_fish)
    
# # Iterate over the list of PhotoImage objects and create a create_image() item for each image.
# x=10
# y=10
# for fish in image_fish_list:
#     canvas.create_image(x, y, image=fish, tag="FISH")
#     print(x)
#     x+=300
#     y+=200


#group dimond image

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




#grass image

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

#stones image
stone1_image = Image.open('images/stones/stone1.png')
stone1_resize = stone1_image.resize((80,70))
img_stone1 =ImageTk.PhotoImage(stone1_resize)

stone2_image = Image.open('images/stones/stone2.png')
stone2_resize = stone2_image.resize((80,70))
img_stone2 =ImageTk.PhotoImage(stone2_resize)

stone3_image = Image.open('images/stones/stone3.png')
stone3_resize = stone3_image.resize((80,70))
img_stone3 =ImageTk.PhotoImage(stone3_resize)

#image flag
flag_image = Image.open('images/flag.png')
flag_resize = flag_image.resize((80,90))
img_flag =ImageTk.PhotoImage(flag_resize)

#create canvas image bg
canvas.create_image(600,300, image =img_bg1)
canvas.create_image(1800,300, image =img_bg1)
canvas.create_image(3000,300, image =img_bg1)
canvas.create_image(4000,300, image =img_bg1)
flag_id = canvas.create_image(3900, 670, image = img_flag)


#canvas image border bottom
image_list = []
for i in range(11):
    border_bottom_image = Image.open('images/border_bottom.jpg')
    img_bottom= ImageTk.PhotoImage(border_bottom_image)
    image_list.append(img_bottom)

# Iterate over the list of PhotoImage objects and create a create_image() item for each image.
x=0
y=750
for img in image_list:
    canvas.create_image(x, y, image=img, tag="PLATFORM")
    x+=400
    

# Create a falling object (boms)
bom_id = canvas.create_image(190, 200, image = img_bom)
bom2_id = canvas.create_image(500, 685, image = img_bom2)


# # Create a falling object (grasses)
grass1_id = canvas.create_image(1200, 565, image = img_grass1)
grass2_id = canvas.create_image(2385,565, image = img_grass2)
grass3_id = canvas.create_image(3400, 590, image = img_grass3)
grass6_id = canvas.create_image(400, 650, image = img_grass6)
grass6_id = canvas.create_image(1800, 650, image = img_grass6)
grass6_id = canvas.create_image(3200, 650, image = img_grass6)
grass7_id = canvas.create_image(1500, 700, image = img_grass7)
grass7_id = canvas.create_image(2600, 700, image = img_grass7)
grass7_id = canvas.create_image(3600, 700, image = img_grass7)

# # Create a falling object (stones)
stone3_id = canvas.create_image(1000, 685, image = img_stone3)
stone2_id = canvas.create_image(2000, 685, image = img_stone2)
stone3_id = canvas.create_image(2900, 685, image = img_stone3)
stone1_id = canvas.create_image(200, 685, image = img_stone1)

# # Create a falling object (dimond1)

dimond1_id = canvas.create_image(700, 690, image = img_dimond1)
dimond1_id = canvas.create_image(3000, 690, image = img_dimond1)
dimond1_id = canvas.create_image(1900, 690, image = img_dimond1)

# #.....Create a falling object (box)....

box1_id = canvas.create_image(595, 690, image = img_box1)
box1_id = canvas.create_image(650, 690, image = img_box1)
box1_id = canvas.create_image(650, 635, image = img_box1)

box1_id = canvas.create_image(1250, 690, image = img_box1)
box1_id = canvas.create_image(1300, 690, image = img_box1)
box1_id = canvas.create_image(1300, 635, image = img_box1)
box1_id = canvas.create_image(1350, 690, image = img_box1)
box1_id = canvas.create_image(1350, 635, image = img_box1)
box1_id = canvas.create_image(1350, 580, image = img_box1)

box1_id = canvas.create_image(2000, 690, image = img_box1)
box1_id = canvas.create_image(2080, 630, image = img_box1)
box1_id = canvas.create_image(2140, 630, image = img_box1)
box1_id = canvas.create_image(2200, 630, image = img_box1)
box1_id = canvas.create_image(2260, 630, image = img_box1)

box1_id = canvas.create_image(2800, 690, image = img_box1)
box1_id = canvas.create_image(3333, 690, image = img_box1)
box1_id = canvas.create_image(3460, 690, image = img_box1)


# ..................dimond​​ score.............

score_id = canvas.create_text(340, 50, text=" : 0 ", font=("bold", 20), fill="white")
dimond2_id = canvas.create_image(300, 50, image = img_dimond2)

## .................Level...............

score_id = canvas.create_text(150, 50, text="Level : 1 ", font=("bold", 20), fill="white")


# Function to update the object's position
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




#create player
X_VELOCITY = 9
Y_VELOCITY = 9


player_img = Image.open('images/players/player_down.png')
player_id = ImageTk.PhotoImage(player_img)

player_img2 =Image.open('images/players/player_left.png')
player_id2 = ImageTk.PhotoImage(player_img2)

player_img3 =Image.open('images/players/player1.png')
player_id3 = ImageTk.PhotoImage(player_img3)

player_img4 =Image.open('images/players/player2.png')
player_id4 = ImageTk.PhotoImage(player_img4)

#it similar pading
player = canvas.create_image(150, 150, image=player_id )
#function to update the object's position
def update_position():
    coord = canvas.coords(player)
    border_coord = canvas.coords('PLATFORM')
    if coord[1]  <= border_coord[1]-90:
        canvas.move(player, 0, 9)
    else:
        canvas.delete(player)
        new_player = canvas.create_image(150, 660, image=player_id3 )

        
    window.after(50, update_position)

#Start the simulation  
update_position()

    

# #Gravity
# #-------------Function----------------

# #Check if the player can move by projecting the movement with dx and dy
# #If checkground is True, check if the player is on the ground by projecting the movement with the last coordinate
# #Instead of getting the platform list with canvas. Find_withtag("PLATFORM"), we could have used a global list
# #Return True if the player can move (i.e is not near any wall), False otherwise
def check_movement(dx=0, dy=0, checkGround=False):
    coord = canvas.coords(player)
    platforms = canvas.find_withtag("PLATFORM")

    if coord[0] + dx < 0 or coord[0] + player_id.width() > SCREEN_WIDTH:
        return False
    
    if checkGround:
        overlap = canvas.find_overlapping(coord[0], coord[1], coord[0], coord[1]+ player_id.height())
    else:
        overlap = canvas.find_overlapping(coord[0] +dx, coord[1]+dy, coord[0]+player_id.width(), coord[1]+player_id.height())
    # print(overlap)
    for platform in platforms:
        if platform in overlap:
            return False
    return True

# #Jump by moving the player up by player
# #Only if the player can move up
# #The force paremeter is always decreasing by 1 until it reach 0
# #The force should be higher than the gravity force to be able

def jump(force):
    if force > 0:
        if not check_movement(0, -force):
            canvas.move(player, 0, -force)
            window.after(TIME_LOOP, jump, force-1)

# #The start_move function is called when a key is pressed
# #It adds the key to the keypressed lish if it's not already in it
# #If the keypressed lish was empty, it calls move function
def start_move(event):
    if event.keysym not in keyPressed:
        keyPressed.append(event.keysym)
        if len(keyPressed) == 1:
            move()

# #The move function is called every TIME_LOOP milliseconds
# #It checks if the player can move in the direction of the keyPressed lish
# #It also check if the player is on the ground before jumping


def move():
    if not keyPressed ==[]:
        x = 0
        if "Left" in keyPressed:
            x -= SPEED
            canvas.itemconfig(player, image=player_id4)
        elif "Right" in keyPressed:
            x += SPEED
            canvas.itemconfig(player, image=player_id3)
        elif "space" in keyPressed and not check_movement(0, GRAVITY_FORCE, True):
            jump(JUMP_FORCE)
        if not check_movement(x):
            canvas.move(player, x, 0)
        window.after(TIME_LOOP, move)

# #The gravity function is called every TIME_LOOP milliseconds
# #It checks if the player can move down by GRAVITY_FORCE 
# #It is always looping, even if the player can't move down
def gravity():
    if check_movement(0, GRAVITY_FORCE, True):
        canvas.move(player, 0, GRAVITY_FORCE)
    window.after(TIME_LOOP, gravity)

gravity()

# #The stop _move function is called when a key is released
# #It removes the key from the keyPress lish
def stop_move(event):
    global keyPressed
    if event.keysym in keyPressed:
        keyPressed.remove(event.keysym)



# #Moveable player when touch border(down)
# def is_moveable():
#     coord = canvas.coords(player)
#     players = canvas.find_withtag("PLATFORM")
#     print(players)
#     overlap = canvas.find_overlapping(coord[0], coord[1], coord[0] + player_id .width(), coord[1] + player_id .height())
#     print(overlap)
#     for play in players:
#         if play in overlap:
#             return 1
#     return 0

# shape = is_moveable()
# print(shape)


# def move(x_velocity,y_velocity):
#     canvas.move(player, x_velocity, y_velocity)


# def check_direction(event):
#     if event.keysym == "Left":
#         canvas.itemconfig(player, image=player_id4)
#         move(-X_VELOCITY,0)
#     elif event.keysym == "Right":
#         canvas.itemconfig(player, image=player_id3)
#         move(X_VELOCITY,0)
#     elif event.keysym == "Up":
#         canvas.itemconfig(player, image=player_id3)
#         move(0,-Y_VELOCITY)
#     elif event.keysym == "Down":
#         canvas.itemconfig(player, image=player_id)
#         move(0,Y_VELOCITY)

# window.bind("<Key>", check_direction)

#No auto scroll
def scroll_right(event):
    canvas.xview('scroll', 1, 'units')

def scroll_left(event):
    canvas.xview('scroll', -1, 'units')


window.bind("<Right>", scroll_right)
window.bind("<Left>", scroll_left)
window.bind("<Key>", start_move)
window.bind("<KeyRelease>", stop_move)





window.mainloop()