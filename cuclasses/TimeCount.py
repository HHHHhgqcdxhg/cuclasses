import time
from functools import wraps

def timeCount(enable:bool=True, method:dict(help="""method to count time;可选择的计时所用的获取时间的函数.默认time.perf_counter,或者也可以选用time.time,python3.7可以按需选用time.perf_counter_ns""")=time.perf_counter):
    """
    装饰器,被装饰的函数将在执行后打印执行时间
    :param enable: 设为False则不计时,直接执行函数
    :param method: 可选择的计时所用的获取时间的函数.默认time.perf_counter,或者也可以选填time.time,python3.7可以按需选用time.perf_counter_ns
    :return: None
    """

    def decorate(func):
        if not enable:
            return lambda *args: func(*args)

        @wraps(func)
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

    print(timeCount.__annotations__)
