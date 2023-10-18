import tkinter as tk
import time
window = tk.Tk()
window.title("Game Animation")
canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()
x_pos = 50
y_pos = 50
def update_game():
    global x_pos, y_pos
    
    # Update the position of the game objects
    x_pos += 1
    y_pos += 1
    
    # Clear the canvas
    canvas.delete("all")
    
    # Draw the game objects
    canvas.create_oval(x_pos, y_pos, x_pos + 20, y_pos + 20, fill="red")
    
    # Call the update_game function after a delay
    window.after(10, update_game)
update_game()
window.mainloop()