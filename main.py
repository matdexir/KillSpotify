import subprocess
import sys

subprocess.call('ps aux | grep spotify >> output.txt',shell=True)
inFile = "output.txt"
wait_time = input("In how long do you want to kill Spotify(format ?h ?m ?s):")
wait_time = wait_time.rstrip()
with open(inFile) as i:
    lines = i.readlines()
    obj = lines[0].split()
    subprocess.call('echo "Killing Spotify..."',shell=True)
    subprocess.call('sleep %s'%wait_time,shell=True)
    try:
        subprocess.call('kill %s'%wait_time %spotify_id,shell=True)
    except:
        print("Spotify is not currently running.")
    try:
        subprocess.call('rm output.txt',shell=True)
    except:
        pass
