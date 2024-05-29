def integrate(f, a, b, *, n_iter=1000):
    h = (b - a) / n_iter
    s = 0.5 * (f(a) + f(b))
    x = a + h
    while (x <= b - h):
        s += f(x)
        x += h
    return h * s