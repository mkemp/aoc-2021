from math import sqrt

with open('input') as f:
    values = f.read().strip().partition(': ')[-1].partition(', ')

t_x_min = 277
t_x_max = 318
t_y_min = -92
t_y_max = -53


def sign(number):
    try:
        return int(number / abs(number))
    except ZeroDivisionError:
        return 0


def in_target(x, y):
    return t_x_min <= x <= t_x_max and t_y_min <= y <= t_y_max


def viable(x, y, d_x, d_y):
    return x <= t_x_max and t_y_min <= y and not (d_x == 0 and x < t_x_min)


def step(x, y, d_x, d_y):
    return x + d_x, y + d_y, (0 if d_x == 0 else (abs(d_x) - 1) * sign(d_x)), d_y - 1


def brute_force():
    final_y_max, distinct_values = 0, 0
    for p_x in range(int(sqrt(t_x_min)), t_x_max + 1):
        for p_y in range(t_y_min, abs(t_y_min) + 1):
            x, y = 0, 0
            d_x, d_y = p_x, p_y
            y_max = 0
            while viable(x, y, d_x, d_y):
                x, y, d_x, d_y = step(x, y, d_x, d_y)
                y_max = max(y_max, y)
                if in_target(x, y):
                    distinct_values += 1
                    final_y_max = max(final_y_max, y_max)
                    break
    return final_y_max, distinct_values


# Part 1
y_max, distinct_values = brute_force()
print(y_max)
# 4186

# Part 2
print(distinct_values)
# 2669
