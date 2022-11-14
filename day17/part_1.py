# x_max = 251
# x_min = 192
# y_max = -59
# y_min = -89

x_max = 30
x_min = 20
y_max = -5
y_min = -10

def trajectory(vx, vy):
    x = y = 0
    while y > y_min:
        if (x_min <= x <= x_max) and (y_min <= y <= y_max):
            return True
        x += vx
        y += vy
        if vx > 0:
            vx -= 1
        elif vx < 0:
            vx += 1
        vy -= 1
        # print(x, y)
    return False

assert trajectory(7, 2)
assert trajectory(6, 3)
assert trajectory(9, 0)
assert not trajectory(17, -4)
