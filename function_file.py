def to_seconds(countdown):
    countdown = countdown.split()
    seconds = 0
    for clock in countdown:
        try:
            if 'h' in clock:
                seconds += int(clock[:len(clock) - 1]) * 3600
            elif 'm' in clock:
                seconds += int(clock[:len(clock) - 1]) * 60
            elif 's' in clock:
                seconds += int(clock[:len(clock) - 1])
            elif len(clock) == 1:
                seconds += int(clock)
            else:
                seconds += int(clock[:len(clock)])
        except:
            print("The format entered is not correct.")
    return str(seconds)

def countdown(seconds):
    import time
    while seconds:
        mins, secs = divmod(seconds, 60)
        hours, mins = divmod(mins ,60)
        timer = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
        print("Killing Spotify in " + timer, end='\r')
        time.sleep(1)
        seconds -= 1

def del_output():
    import subprocess
    try:
        subprocess.call('rm output.txt',shell=True)
    except:
        pass
