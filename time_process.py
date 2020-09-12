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

