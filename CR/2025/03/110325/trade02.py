def trade(price, signal):
    n, t, result = 0, 0, []
    for p, s in zip(price, signal):
        if s == 1:
            n, t = n+1, t+p
            yield 0
        elif s == 0:
            yield 0
        elif s == -1:
            avg = t/n
            n, t = n-1, t-avg
            yield p - avg
        else:
            assert s in (1, 0, -1), f"Signal {s} error"

price = [100, 99, 98, 99, 101, 102]
signal = [1, -1, 0, 0, 0, 0]

results = list(trade(price, signal))
print(results)