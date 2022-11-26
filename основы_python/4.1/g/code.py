def can_eat(knight, chess):
    x_1, y_1 = knight
    for x_2, y_2 in ((2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)):
        if (x_1 + x_2, y_1 + y_2) == chess:
            return True
    return False
