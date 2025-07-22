from pynput import mouse

# Function to handle mouse movement
def on_move(x, y):
    print(f"Mouse moved to ({x}, {y})")

# Function to handle mouse click
def on_click(x, y, button, pressed):
    if pressed:
        print(f"Mouse clicked at ({x}, {y}) with {button}")
    else:
        print(f"Mouse released at ({x}, {y})")

# Function to handle mouse scroll
def on_scroll(x, y, dx, dy):
    print(f"Scrolled at ({x}, {y}) with delta ({dx}, {dy})")

# Start listening for mouse events
with mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    print("Listening for mouse events... Press Ctrl + C to stop.")
    listener.join()