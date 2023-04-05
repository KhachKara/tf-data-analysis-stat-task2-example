def solution(p: float, x: np.array) -> tuple:
    alpha1 = (1 - p) / 2
    alpha2 = (1 + p) / 2
    n = x.size
    a1, a2 = pow(alpha1, 1 / n), pow(alpha2, 1 / n)

    x_max = x.max()
    return (x_max - 0.095) / a2 + 0.095, \
           (x_max - 0.095) / a1 + 0.095
