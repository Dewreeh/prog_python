def is_fit(a, b, c, m, k):
    max_s_of_box_shapes = max(a*b, a*c, b*c)
    s_door = m*k
    return max_s_of_box_shapes <= m*k
print(is_fit(2, 1, 3, 2, 3))