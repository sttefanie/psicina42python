def my_var():
    a = 42
    b = "42"
    c = "quarenta-dois"
    d = 42.0
    e =  True
    f = [1, 2, 3, 4]
    g = {'x': 1, 'y': 2}
    h = (1, 2, 2)
    i = set()

    for var in (a, b, c, d, e, f, g, h, i):
        print("{} has a type {}".format(var, type(var)))

if __name__ == '__main__':
    my_var()