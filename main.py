#!/usr/bin/python3
import subprocess
import my_timer

subprocess.call('ps aux | grep spotify >> output.txt', shell=True)
inFile = "output.txt"
def get_time():
    wait_time = input("In how long do you want to kill Spotify(format ?h ?m ?s):")
    wait_time = wait_time.rstrip()
    return wait_time

redlight = True
seconds = '0'

while redlight:
    wait_time = get_time()
    seconds = my_timer.to_seconds(wait_time)
    if seconds != '0':
        redlight = False

with open(inFile) as i:
    lines = i.readlines()
    obj = lines[0].split()
    spotify_id = obj[1]
    my_timer.del_output()
    if len(lines) < 3:
        print("Spotify is not currently running.")
    else:
        my_timer.countdown(int(seconds))
        try:
            subprocess.call('kill %s' %spotify_id, shell=True)
        except:
            print("Spotify is not currently running.")
