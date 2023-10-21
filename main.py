import tkinter as tk
from PIL import Image, ImageTk

# Create the Tkinter window
window = tk.Tk()
window.title('Juggle-Game')
window.attributes('-fullscreen', True)

SCREEN_WIDTH = 3000
SCREEN_HEIGHT = 900

frame = tk.Frame(window, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
frame.pack()

canvas = tk.Canvas(frame, width=SCREEN_WIDTH, height=SCREEN_HEIGHT,  scrollregion= (0,0,4000,5000))
canvas.pack()

#scrollbar
scrollbar_bottom = tk.Scrollbar(window, orient='horizontal', command=canvas.xview)
canvas.configure(xscrollcommand=scrollbar_bottom.set)
scrollbar_bottom.place(relx=0, rely=1, relwidth=1, anchor='sw')

#create image
border_bottom_image = Image.open('border_bottom.jpg')
img_bottom= ImageTk.PhotoImage(border_bottom_image)

bom_image = Image.open('bom.png')
bom_resize = bom_image.resize((50,50))
img_bom =ImageTk.PhotoImage(bom_resize)

bg1_image = Image.open('bg1.png')
img_bg1 =ImageTk.PhotoImage(bg1_image)

#group fish image
# fish1_image = Image.open('fish1.gif')
# fish1_resize = fish1_image.resize((100,100))
# img_fish1 =ImageTk.PhotoImage(fish1_resize)

# fish2_image = Image.open('fish2.gif')
# fish2_resize = fish2_image.resize((100,100))
# img_fish2 =ImageTk.PhotoImage(fish2_resize)

# fish3_image = Image.open('fish3.gif')
# fish3_resize = fish3_image.resize((100,100))
# img_fish3 =ImageTk.PhotoImage(fish3_resize)

# fish4_image = Image.open('fish4.gif')
# fish4_resize = fish4_image.resize((100,100))
# img_fish4 =ImageTk.PhotoImage(fish4_resize)

# fish5_image = Image.open('fish5.gif')
# fish5_resize = fish5_image.resize((100,100))
# img_fish5 =ImageTk.PhotoImage(fish5_resize)

# fish6_image = Image.open('fish6.gif')
# fish6_resize = fish6_image.resize((100,100))
# img_fish6 =ImageTk.PhotoImage(fish6_resize)

# fish7_image = Image.open('fish7.gif')
# fish7_resize = fish7_image.resize((100,100))
# img_fish7 =ImageTk.PhotoImage(fish7_resize)

#grass image

grass1_image = Image.open('grass1.gif')
grass1_resize = grass1_image.resize((100,100))
img_grass1 =ImageTk.PhotoImage(grass1_resize)

# grass2_image = Image.open('grass2.gif')
# grass2_resize = grass2_image.resize((100,100))
# img_grass2 =ImageTk.PhotoImage(grass2_resize)

# grass3_image = Image.open('grass3.gif')
# grass3_resize = grass3_image.resize((100,100))
# img_grass3 =ImageTk.PhotoImage(grass3_resize)

# grass4_image = Image.open('grass4.png')
# grass4_resize = grass4_image.resize((100,100))
# img_grass4 =ImageTk.PhotoImage(grass4_resize)


#create canvas
canvas.create_image(600,300, image =img_bg1)
canvas.create_image(1800,300, image =img_bg1)
canvas.create_image(3000,300, image =img_bg1)
canvas.create_image(4000,300, image =img_bg1)
#canvas image
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


# Create a falling object (bom)
bom_id = canvas.create_image(190, 200, image = img_bom)
# Create a falling object (fish)
# fish1_id = canvas.create_image(190, 200, image = img_fish1)
# fish2_id = canvas.create_image(300, 200, image = img_fish2)
# fish3_id = canvas.create_image(300, 400, image = img_fish3)
# fish4_id = canvas.create_image(500, 700, image = img_fish4)
# fish5_id = canvas.create_image(700, 300, image = img_fish5)
# fish6_id = canvas.create_image(600, 500, image = img_fish6)
# fish7_id = canvas.create_image(50, 300, image = img_fish7)

# # Create a falling object (grass)
# grass1_id = canvas.create_image(700, 670, image = img_grass1)
# grass2_id = canvas.create_image(300, 670, image = img_grass2)
# grass3_id = canvas.create_image(900, 670, image = img_grass3)
# grass4_id = canvas.create_image(100, 670, image = img_grass4)


#design background



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

    if rightPos[0] > SCREEN_WIDTH-180 or leftPos[0] < 0:
        xspeed = -xspeed

    if bottomPos[1] > SCREEN_HEIGHT-200 or topPos[1] < 0  :
        yspeed = -yspeed
    canvas.after(10, moveBom)
canvas.after(10, moveBom)





window.mainloop()