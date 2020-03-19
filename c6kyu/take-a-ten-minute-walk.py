"""
Description:

The city provides its citizens with a Walk Generating App on their phones -
everytime you press the button it sends you an array of one-letter strings
representing directions to walk (eg. ['n', 's', 'w', 'e']). You always walk
only a single block in a direction and you know it takes you one minute to
traverse one city block, so create a function that will return true if the walk
the app gives you will take you exactly ten minutes (you don't want to be early
or late!) and will, of course, return you to your starting point. Return false
otherwise.
"""


def is_valid_walk(walk):
    time = 10
    pos = [0, 0]
    for i in walk:
        if time < 0:
            break
        if i == 'n':
            pos[0] += 1
        elif i == 's':
            pos[0] -= 1
        elif i == 'w':
            pos[1] += 1
        else:
            pos[1] -= 1
        time -= 1
    if time == 0 and pos == [0, 0]:
        return True
    else:
        return False


if __name__ == "__main__":
    print(is_valid_walk(['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']))
