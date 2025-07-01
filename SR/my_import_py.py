from about_time import about_time


def some_func():
    import time
    time.sleep(85e-3)
    return True


def main():
    with about_time() as t1:  # <-- use it like a context manager!

        t2 = about_time(some_func)  # <-- use it with any callable!!

        t3 = about_time(x * 2 for x in range(56789))  # <-- use it with any iterable or generator!!!
        data = [x for x in t3]  # then just iterate!

    print(f'total: {t1.duration_human}')
    print(f'  some_func: {t2.duration_human} -> result: {t2.result}')
    print(f'  generator: {t3.duration_human} -> {t3.count_human} elements, throughput: {t3.throughput_human}')

main()