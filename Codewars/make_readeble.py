def make_readable(seconds):
    if seconds <= 359999 and seconds >= 0:
        hours = seconds // (60*60)
        seconds %= (60*60)
        minutes = seconds // 60
        seconds %= 60
        return "%02i:%02i:%02i" % (hours, minutes, seconds) 