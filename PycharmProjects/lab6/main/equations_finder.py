def find_equation(p1, p2):
    if p1 == p2:
        raise ValueError("Points cannot be equal.")
    a = (p2[1] - p1[1]) / (p2[0] - p1[0])
    b = p1[1] - a * p1[0]
    return f'y={a}x+{b}'
