import tkinter as tk
import random

# Constants
CANVAS_W = 400
CANVAS_H = 400
TARGET_SIZE = 20
TIME_LIMIT_MS = 13 * 1000  # 13 seconds in milliseconds

# Initialize Score
score = 0
target_timer_id = None

def move_player(event):
    key = event.keysym.lower()
    x, y = 0, 0
    if key == 'w': y = -10
    elif key == 's': y = 10
    elif key == 'a': x = -10
    elif key == 'd': x = 10
    
    canvas.move(player, x, y)
    check_collision()

def spawn_target():
    """Place the target at a random location and (re)start the timeout."""
    global target_timer_id
    # Cancel any existing timer
    if target_timer_id is not None:
        try:
            root.after_cancel(target_timer_id)
        except Exception:
            pass
        target_timer_id = None

    # Choose random position inside canvas bounds
    x1 = random.randint(0, CANVAS_W - TARGET_SIZE)
    y1 = random.randint(0, CANVAS_H - TARGET_SIZE)
    x2 = x1 + TARGET_SIZE
    y2 = y1 + TARGET_SIZE
    canvas.coords(target, x1, y1, x2, y2)

    # Start timeout for this target
    target_timer_id = root.after(TIME_LIMIT_MS, on_target_timeout)

def on_target_timeout():
    """Called when player fails to get the target in time."""
    global score, target_timer_id
    target_timer_id = None
    score -= 5
    score_label.config(text=f"Score: {score}")
    spawn_target()

def check_collision():
    global score, target_timer_id
    # Get player coordinates
    p_coords = canvas.coords(player)
    # Check for overlapping objects
    overlapping = canvas.find_overlapping(*p_coords)

    # If player overlaps with the target
    if target in overlapping:
        # Collected before timeout: cancel timer and award points
        if target_timer_id is not None:
            try:
                root.after_cancel(target_timer_id)
            except Exception:
                pass
            target_timer_id = None

        score += 10
        score_label.config(text=f"Score: {score}")
        spawn_target()


# Setup Tkinter
root = tk.Tk()
canvas = tk.Canvas(root, width=CANVAS_W, height=CANVAS_H)
canvas.pack()

# Create shapes
player = canvas.create_rectangle(190, 190, 210, 210, fill="blue")
target = canvas.create_rectangle(0, 0, TARGET_SIZE, TARGET_SIZE, fill="red")

# Score Label
score_label = tk.Label(root, text=f"Score: {score}")
score_label.pack()

# Bind keys
root.bind("<KeyPress>", move_player)

# Spawn the first target and start its timer
spawn_target()

root.mainloop()
