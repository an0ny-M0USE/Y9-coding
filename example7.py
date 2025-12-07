import time

def loading():
    for i in range(3):  # Will repeat the animation this many times
        # Clear entire line and show "Loading game"
        print("\rLoading game     ", end="", flush=True)
        print("\rLoading game", end="", flush=True)
        time.sleep(0.2)
        
        # Add one dot at a time
        for i in range(1, 4):  # Will do 1, 2, 3 dots
            print("\rLoading game" + "." * i + "   ", end="", flush=True)
            time.sleep(0.2)
loading()