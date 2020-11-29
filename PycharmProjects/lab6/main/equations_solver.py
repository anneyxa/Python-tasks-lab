def count_equation(a, b, c):
    try:
        if a == 0:
            return count_linear_equation(b, c)
        else:
            return count_quadratic_equation(a, b, c)
    except ValueError as e:
        print(e)


def count_quadratic_equation(a, b, c):
    delta = b * b - 4 * a * c
    sqrt_delta = abs(delta) ** (1 / 2)
    if delta > 0:
        x1 = ((-b + sqrt_delta)/(2 * a))
        x2 = ((-b - sqrt_delta)/(2 * a))
        return x1, x2
    elif delta == 0:
        x0 = (-b / (2 * a))
        return x0
    else:
        raise ValueError("Equation has no solutions")


def count_linear_equation(a, b):
    if a != 0:
        x = -b / a
        return x
    elif b == 0:
        raise ValueError("Equation has infinite number of solutions")
    else:
        raise ValueError("Contradictory equation")
