import tkinter as tk

# Initialize Score
score = 0

def move_player(event):
    global score
    key = event.keysym.lower()
    x, y = 0, 0
    if key == 'w': y = -10
    elif key == 's': y = 10
    elif key == 'a': x = -10
    elif key == 'd': x = 10
    
    canvas.move(player, x, y)
    check_collision()

def check_collision():
    global score
    # Get player coordinates
    p_coords = canvas.coords(player)
    # Check for overlapping objects
    overlapping = canvas.find_overlapping(*p_coords)
    
    # If player overlaps with the target (item id 2)
    if target in overlapping:
        score += 10
        score_label.config(text=f"Score: {score}")
        # Move target to new random location (optional)
        canvas.move(target, 50, 50) 

# Setup Tkinter
root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Create shapes
player = canvas.create_rectangle(190, 190, 210, 210, fill="blue")
target = canvas.create_rectangle(300, 300, 320, 320, fill="red")

# Score Label
score_label = tk.Label(root, text=f"Score: {score}")
score_label.pack()

# Bind keys
root.bind("<KeyPress>", move_player)

root.mainloop()
