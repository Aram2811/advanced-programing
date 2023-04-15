def a(b):
    c = max(b.values())
    d = min(b.values())
    for i in b.keys():
        if b[i] == c:
            Max = i
        if b[i] == d:
            Min = i
    return Max, Min
print(a({'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}))