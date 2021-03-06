import os, time
import ctypes
MessageBox = ctypes.windll.user32.MessageBoxW

#path_to_watch = r"D:\Neurolab\ialdev\Ischemia YG\learning"
def watch_folder(path_to_watch):
    before = dict ([(f, None) for f in os.listdir (path_to_watch)])
    while 1:
        time.sleep (10)
        after = dict ([(f, None) for f in os.listdir (path_to_watch)])
        added = [f for f in after if not f in before]
        removed = [f for f in before if not f in after]
        if added: print("Added: ", ", ".join (added))
        if removed: print("Removed: ", ", ".join (removed))
        before = after

def watch_and_say(path_to_watch, delay):
    before = dict ([(f, None) for f in os.listdir (path_to_watch)])
    while 1:
        time.sleep (delay)
        after = dict ([(f, None) for f in os.listdir (path_to_watch)])
        added = [f for f in after if not f in before]
        removed = [f for f in before if not f in after]
        if added: 
            print("Added: ", ", ".join (added))
            MessageBox(None, 'Added file: ' + ", ".join (added), 'Folder watcher', 0)
        if removed: print("Removed: ", ", ".join (removed))
        before = after