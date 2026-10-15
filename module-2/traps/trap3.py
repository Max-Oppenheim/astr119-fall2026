# trap3.py -- predict what happens, then run it.
count = 0


def bump():
    global count
    count = count + 1


bump()
bump()
print(count)
