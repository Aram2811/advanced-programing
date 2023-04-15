def a(b):
    c = list()
    for d, p in b.items():
        c.append((d, p))
    return c


print(a({'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4}))
