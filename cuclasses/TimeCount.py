import time


def timeCount(enable=True, method=time.perf_counter):
    def decorate(func):
        if not enable:
            return lambda *args: func(*args)

        def retfunc(*args):
            t0 = method()
            res = func(*args)
            t1 = method() - t0
            print(f"func {func.__name__:<12} excuted in : {t1}")
            return res

        return retfunc

    return decorate


if __name__ == '__main__':
    @timeCount()
    def cccccccccc():
        print({"a": "c"})


    cccccccccc()
