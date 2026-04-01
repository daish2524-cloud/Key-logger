import keyboard
import os
import time

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
filename = os.path.join(desktop, "my_global_notes.txt")

print("Running... Press ESC to stop.")

buffer = ""

def save_to_file():
    global buffer
    if buffer:
        with open(filename, "a") as f:
            f.write(buffer)
        buffer = ""

def on_key(event):
    global buffer
    name = event.name

    if name == "esc":
        save_to_file()
        print("\nStopped safely ✅")
        os._exit(0)
    elif name == "space":
        buffer += " "
    elif name == "enter":
        buffer += "\n"
    elif name == "backspace":
        buffer = buffer[:-1]
    elif len(name) == 1:
        buffer += name

keyboard.on_press(on_key)

while True:
    try:
        time.sleep(2)
        save_to_file()
    except Exception as e:
        print("Error:", e)