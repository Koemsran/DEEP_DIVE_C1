import tkinter as tk
from PIL import Image, ImageTk

# Create the Tkinter window
window = tk.Tk()
window.title('Juggle-Game')
window.attributes('-fullscreen', True)

SCREEN_WIDTH = 3000
SCREEN_HEIGHT = 900

GRAVITY_FORCE = 9
JUMP_FORCE = 100
SPEED = 7

TIME_LOOP = 10

# ------------- Variables ---------------------
keyPressed = []

frame = tk.Frame(window, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
frame.pack()

canvas = tk.Canvas(frame, width=SCREEN_WIDTH, height=SCREEN_HEIGHT,  scrollregion= (0,0,4000,5000))
canvas.pack()

#scrollbar
scrollbar_bottom = tk.Scrollbar(window, orient='horizontal', command=canvas.xview)
canvas.configure(xscrollcommand=scrollbar_bottom.set)
scrollbar_bottom.place(relx=0, rely=1, relwidth=1, anchor='sw')

#create image
border_bottom_image = Image.open('images/border_bottom.jpg')
img_bottom= ImageTk.PhotoImage(border_bottom_image)

bom_image = Image.open('images/bom.png')
bom_resize = bom_image.resize((70,70))
img_bom =ImageTk.PhotoImage(bom_resize)

bom2_image = Image.open('images/bom2.png')
img_bom2 =ImageTk.PhotoImage(bom2_image)

bg1_image = Image.open('images/bg1.png')
img_bg1 =ImageTk.PhotoImage(bg1_image)

#Create image bubble water
bubble_image = Image.open('images/bubbles/bubble.png')
bubble = ImageTk.PhotoImage(bubble_image)

bubble1_image = Image.open('images/bubbles/bubble1.png')
bubble1 = ImageTk.PhotoImage(bubble1_image)

bubble2_image = Image.open('images/bubbles/bubble2.png')
bubble2 = ImageTk.PhotoImage(bubble2_image)

bubble3_image = Image.open('images/bubbles/bubble3.png')
bubble3 = ImageTk.PhotoImage(bubble3_image)

bubble4_image = Image.open('images/bubbles/bubble4.png')
bubble4 = ImageTk.PhotoImage(bubble4_image)

bubble5_image = Image.open('images/bubbles/bubble5.png')
bubble5 = ImageTk.PhotoImage(bubble5_image) 

bubble6_image = Image.open('images/bubbles/bubble6.png')
bubble6 = ImageTk.PhotoImage(bubble6_image) 

bubble7_image = Image.open('images/bubbles/bubble7.png')
bubble7 = ImageTk.PhotoImage(bubble7_image) 

bubble8_image = Image.open('images/bubbles/bubble8.png')
bubble8 = ImageTk.PhotoImage(bubble8_image) 

bubble9_image = Image.open('images/bubbles/bubble9.png')
bubble9 = ImageTk.PhotoImage(bubble9_image) 

bubble10_image = Image.open('images/bubbles/bubble10.png')
bubble10 = ImageTk.PhotoImage(bubble10_image) 

bubble11_image = Image.open('images/bubbles/bubble6.png')
bubble11 = ImageTk.PhotoImage(bubble11_image) 

bubble12_image = Image.open('images/bubbles/bubble7.png')
bubble12 = ImageTk.PhotoImage(bubble12_image) 

bubble13_image = Image.open('images/bubbles/bubble8.png')
bubble13 = ImageTk.PhotoImage(bubble13_image) 

bubble14_image = Image.open('images/bubbles/bubble9.png')
bubble14 = ImageTk.PhotoImage(bubble14_image) 
bubble_image = Image.open('images/bubbles/bubble.png')
bubble = ImageTk.PhotoImage(bubble_image)

bubble15_image = Image.open('images/bubbles/bubble1.png')
bubble15 = ImageTk.PhotoImage(bubble15_image)

bubble16_image = Image.open('images/bubbles/bubble2.png')
bubble16 = ImageTk.PhotoImage(bubble16_image)

bubble17_image = Image.open('images/bubbles/bubble3.png')
bubble17 = ImageTk.PhotoImage(bubble17_image)

bubble18_image = Image.open('images/bubbles/bubble4.png')
bubble18 = ImageTk.PhotoImage(bubble18_image)

bubble19_image = Image.open('images/bubbles/bubble5.png')
bubble19 = ImageTk.PhotoImage(bubble19_image) 

bubble20_image = Image.open('images/bubbles/bubble6.png')
bubble20 = ImageTk.PhotoImage(bubble20_image) 

bubble21_image = Image.open('images/bubbles/bubble7.png')
bubble21 = ImageTk.PhotoImage(bubble21_image) 

bubble22_image = Image.open('images/bubbles/bubble8.png')
bubble22 = ImageTk.PhotoImage(bubble22_image) 

bubble23_image = Image.open('images/bubbles/bubble9.png')
bubble23 = ImageTk.PhotoImage(bubble23_image) 

bubble24_image = Image.open('images/bubbles/bubble10.png')
bubble24 = ImageTk.PhotoImage(bubble24_image) 

bubble25_image = Image.open('images/bubbles/bubble6.png')
bubble25 = ImageTk.PhotoImage(bubble25_image) 

bubble26_image = Image.open('images/bubbles/bubble7.png')
bubble26 = ImageTk.PhotoImage(bubble26_image) 

bubble27_image = Image.open('images/bubbles/bubble8.png')
bubble27 = ImageTk.PhotoImage(bubble27_image) 

bubble28_image = Image.open('images/bubbles/bubble9.png')
bubble28 = ImageTk.PhotoImage(bubble28_image) 


#group fish image
fish1_image = Image.open('images/fishes/fish1.gif')
fish1_resize = fish1_image.resize((100,100))
img_fish1 =ImageTk.PhotoImage(fish1_resize)

fish2_image = Image.open('images/fishes/fish2.gif')
fish2_resize = fish2_image.resize((100,100))
img_fish2 =ImageTk.PhotoImage(fish2_resize)

fish3_image = Image.open('images/fishes/fish3.gif')
fish3_resize = fish3_image.resize((100,100))
img_fish3 =ImageTk.PhotoImage(fish3_resize)

fish4_image = Image.open('images/fishes/fish4.gif')
fish4_resize = fish4_image.resize((100,100))
img_fish4 =ImageTk.PhotoImage(fish4_resize)

fish5_image = Image.open('images/fishes/fish5.gif')
fish5_resize = fish5_image.resize((100,100))
img_fish5 =ImageTk.PhotoImage(fish5_resize)

fish6_image = Image.open('images/fishes/fish6.gif')
fish6_resize = fish6_image.resize((100,100))
img_fish6 =ImageTk.PhotoImage(fish6_resize)

fish7_image = Image.open('images/fishes/fish7.gif')
fish7_resize = fish7_image.resize((100,100))
img_fish7 =ImageTk.PhotoImage(fish7_resize)

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

# grass4_image = Image.open('grass4.png')
# grass4_resize = grass4_image.resize((100,100))
# img_grass4 =ImageTk.PhotoImage(grass4_resize)

# grass4_image = Image.open('grass4.png')
# grass4_resize = grass4_image.resize((100,100))
# img_grass4 =ImageTk.PhotoImage(grass4_resize)

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

stone2_image = Image.open('images/stones/stone1.png')
stone2_resize = stone2_image.resize((80,70))
img_stone2 =ImageTk.PhotoImage(stone2_resize)

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
canvas.create_image(0, 750, image = img_bottom, tags="PLATFORM")
canvas.create_image(400, 750, image = img_bottom, tags="PLATFORM")
canvas.create_image(800, 750, image = img_bottom, tags="PLATFORM")
canvas.create_image(1045, 750, image = img_bottom, tags="PLATFORM")
canvas.create_image(1545, 750, image = img_bottom, tags="PLATFORM")
canvas.create_image(2045, 750, image = img_bottom, tags="PLATFORM")
canvas.create_image(1545, 750, image = img_bottom, tags="PLATFORM")
canvas.create_image(2045, 750, image = img_bottom, tags="PLATFORM")
canvas.create_image(2545, 750, image = img_bottom, tags="PLATFORM")
canvas.create_image(3045, 750, image = img_bottom, tags="PLATFORM")
canvas.create_image(3545, 750, image = img_bottom, tags="PLATFORM")
canvas.create_image(4045, 750, image = img_bottom, tags="PLATFORM")


# Create a falling object (bubble water)
object_id = canvas.create_image(100, 700, image = bubble, tags='BUBBLE')
object1_id = canvas.create_image(600, 700, image = bubble1, tags='BUBBLE')
object2_id = canvas.create_image(350, 900, image = bubble2, tags='BUBBLE')
object3_id = canvas.create_image(900, 700, image = bubble3, tags='BUBBLE')
object4_id = canvas.create_image(1200, 750, image = bubble4, tags='BUBBLE')
object5_id = canvas.create_image(1500, 800, image = bubble5, tags='BUBBLE') 
object6_id = canvas.create_image(2000, 700, image = bubble6, tags='BUBBLE')
object7_id = canvas.create_image(1800, 700, image = bubble7, tags='BUBBLE')
object8_id = canvas.create_image(1080, 900, image = bubble8, tags='BUBBLE')
object9_id = canvas.create_image(900, 700, image = bubble9, tags='BUBBLE')
object10_id = canvas.create_image(3000, 750, image = bubble10, tags='BUBBLE')
object11_id = canvas.create_image(3400, 700, image = bubble11, tags='BUBBLE')
object12_id = canvas.create_image(3500, 750, image = bubble12, tags='BUBBLE')
object13_id = canvas.create_image(2700, 800, image = bubble13, tags='BUBBLE') 
object14_id = canvas.create_image(1300, 700, image = bubble14, tags='BUBBLE')
object15_id = canvas.create_image(600, 700, image = bubble15, tags='BUBBLE')
object16_id = canvas.create_image(350, 900, image = bubble16, tags='BUBBLE')
object17_id = canvas.create_image(900, 700, image = bubble17, tags='BUBBLE')
object18_id = canvas.create_image(1200, 750, image = bubble18, tags='BUBBLE')
object19_id = canvas.create_image(1500, 800, image = bubble19, tags='BUBBLE') 
object20_id = canvas.create_image(2000, 400, image = bubble20, tags='BUBBLE')
object21_id = canvas.create_image(1800, 700, image = bubble21, tags='BUBBLE')
object22_id = canvas.create_image(1080, 900, image = bubble22, tags='BUBBLE')
object23_id = canvas.create_image(900, 700, image = bubble23, tags='BUBBLE')
object24_id = canvas.create_image(3000, 750, image = bubble24, tags='BUBBLE')
object25_id = canvas.create_image(3400, 700, image = bubble25, tags='BUBBLE')
object26_id = canvas.create_image(3500, 750, image = bubble26, tags='BUBBLE')
object27_id = canvas.create_image(2700, 800, image = bubble27, tags='BUBBLE') 
object28_id = canvas.create_image(1300, 700, image = bubble28, tags='BUBBLE')

object1 = canvas.create_image(100, 1000, image = bubble, tags='BUBBLE1')
object2 = canvas.create_image(600, 1000, image = bubble1, tags='BUBBLE1')
object3 = canvas.create_image(350, 900, image = bubble2, tags='BUBBLE1')
object4 = canvas.create_image(900, 1000, image = bubble3, tags='BUBBLE1')
object5 = canvas.create_image(1200, 1000, image = bubble4, tags='BUBBLE1')
object6 = canvas.create_image(350, 900, image = bubble5, tags='BUBBLE1') 


# Create a falling object (boms)
bom_id = canvas.create_image(190, 200, image = img_bom)
bom2_id = canvas.create_image(500, 685, image = img_bom2)

# Create a falling object (fishes)
fish1_id = canvas.create_image(190, 200, image = img_fish1)
fish2_id = canvas.create_image(300, 200, image = img_fish2)
fish3_id = canvas.create_image(300, 400, image = img_fish3)
fish4_id = canvas.create_image(800, 680, image = img_fish4)
fish5_id = canvas.create_image(700, 300, image = img_fish5)
fish6_id = canvas.create_image(600, 500, image = img_fish6)
fish7_id = canvas.create_image(50, 300, image = img_fish7)

# # Create a falling object (grasses)
grass1_id = canvas.create_image(1200, 565, image = img_grass1)
grass2_id = canvas.create_image(2385,565, image = img_grass2)
grass3_id = canvas.create_image(3400, 590, image = img_grass3)
# grass4_id = canvas.create_image(100, 670, image = img_grass4)
# grass4_id = canvas.create_image(100, 670, image = img_grass4)
grass6_id = canvas.create_image(400, 650, image = img_grass6)
grass6_id = canvas.create_image(1500, 700, image = img_grass7)

# # Create a falling object (stones)
stone1_id = canvas.create_image(1000, 685, image = img_stone1)
stone1_id = canvas.create_image(2000, 685, image = img_stone2)



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


# Function to update the object's position
def update_position_down():
    bubble_coods = canvas.coords('BUBBLE')


    if bubble_coods[1]< 0 and bubble_coods[1]>-100:
        canvas.move('BUBBLE', 0, 3)
        
        window.after(50, update_position_down)
    elif bubble_coods[1]<-100:
        move_up()
    else:
        update_position_up()

def update_position_up():
    bubble_coods = canvas.coords('BUBBLE')
    
    
    if bubble_coods[1]>= -100 :
        
        canvas.move('BUBBLE', 0, -2)


        window.after(30, update_position_up)
    else:
        move_up()

def move_up():
    canvas.delete('BUBBLE')

    bubble_coods = canvas.coords('BUBBLE1')
    # bubble_coods = canvas.coords(object2)
    # bubble_coods = canvas.coords(object3)
    # bubble_coods = canvas.coords(object4)
    # bubble_coods = canvas.coords(object5)
    # bubble_coods = canvas.coords(object6)
    
    if bubble_coods[1]>= -100 :
        canvas.move(object1, 0, -4)
        canvas.move(object2, 0, -3)
        canvas.move(object3, 0, -3.5)
        canvas.move(object4, 0, -1.5)
        canvas.move(object5, 0, -2)
        canvas.move(object6, 0, -4)
        window.after(30, move_up)
    else:
        canvas.delete('BUBBLE1')
        update_position_up()


window.after(30, update_position_up)


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
    border_coord = canvas.coords(' PLATFORM')
    if coord[1] + player_id.height() <= 920:
        canvas.move(player, 0, 9)
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
    print(event.keysym)
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

window.bind("<Key>", start_move)
window.bind("<KeyRelease>", stop_move)

window.mainloop()