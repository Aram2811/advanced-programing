def a(b, c):
    tuple = ()
    for i in b.keys():
        if b[i] == c:
            d = tuple + (i,)
    print(d)


a({'Theodore': 19, 'Roxanne': 22, 'Mathew': 19, 'Betty': 20, }, 19)
