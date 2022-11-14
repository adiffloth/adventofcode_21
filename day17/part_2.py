x_max = 251
x_min = 192
y_max = -59
y_min = -89

def hits_target(vx, vy):
    x = y = 0
    while (y >= y_min) and (x <= x_max):  # Hasn't overshot the target

        if (x_min <= x <= x_max) and (y_min <= y <= y_max):  # In the target area
            return True

        if (vx == 0) and (x < x_min):  # Early quitting, no chance
            return False

        x += vx  # Update position and velocities for the next step
        y += vy
        if vx > 0:
            vx -= 1
        vy -= 1
    return False  # Fall through means we've overshot

count = 0
for vx in range(1, x_max + 2):
    for vy in range(y_min - 1, 400):
        count += hits_target(vx, vy)
print(count)  # 2986
