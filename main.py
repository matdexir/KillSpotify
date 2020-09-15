import subprocess
import sys

subprocess.call('ps aux | grep spotify >> output.txt', shell=True)
inFile = "output.txt"
def get_time():
    wait_time = input("In how long do you want to kill Spotify(format ?h ?m ?s):")
    wait_time = wait_time.rstrip()
    return wait_time

import function_file

redlight = True
seconds = '0'

while redlight:
    wait_time = get_time()
    seconds = function_file.to_seconds(wait_time)
    if seconds != '0':
        redlight = False

with open(inFile) as i:
    lines = i.readlines()
    obj = lines[0].split()
    spotify_id = obj[1]
    function_file.del_output()
    if len(lines) < 3:
        print("Spotify is not currently running.")
    else:
        function_file.countdown(int(seconds))
        try:
            subprocess.call('kill %s' %spotify_id, shell=True)
        except:
            print("Spotify is not currently running.")
