def make_pizza(size, *topings):
    for top in topings:
        print(f"{size}--{top}")

make_pizza(12, "peperroni ")
make_pizza(16, "mushrooms","extra cheese","grand pepers")