
def solution_station_7(equation: str) -> float:
    a = 3
    b = -1
    c = 4
    d = 7
    e = 0.5

    equation = equation.replace("a", str(a))
    equation = equation.replace("b", str(b))
    equation = equation.replace("c", str(c))
    equation = equation.replace("d", str(d))
    equation = equation.replace("e", str(e))

    return float(eval(equation))

