"""
Description:
Write a function, which takes a non-negative integer (seconds) as input and
returns the time in a human-readable format (HH:MM:SS)

    HH = hours, padded to 2 digits, range: 00 - 99
    MM = minutes, padded to 2 digits, range: 00 - 59
    SS = seconds, padded to 2 digits, range: 00 - 59

The maximum time never exceeds 359999 (99:59:59)
"""
def make_readable(seconds):
    # print(seconds)
    hours = seconds // 3600
    seconds -= hours * 3600
    if len(str(hours)) < 2:
        hours = f"0{hours}"
    minutes = seconds // 60
    seconds -= minutes * 60
    if len(str(minutes)) < 2:
        minutes = f"0{minutes}"
    if len(str(seconds)) < 2:
        seconds = f"0{seconds}"
    return f"{hours}:{minutes}:{seconds}"


if __name__ == "__main__":

    assert make_readable(0) == "00:00:00"
    assert make_readable(5) == "00:00:05"
    assert make_readable(60) == "00:01:00"
    assert make_readable(86399) == "23:59:59"
    assert make_readable(359999) == "99:59:59"