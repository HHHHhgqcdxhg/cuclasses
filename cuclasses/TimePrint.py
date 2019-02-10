from datetime import datetime

rawPrint = print


def _timePrint(*args, **kwargs):
    try:
        strf = kwargs["strf"]
    except:
        strf = "[%Y-%m-%d %H:%M:%S]"
    else:
        del kwargs["strf"]
    timeStr = datetime.now().strftime(strf)
    rawPrint(timeStr, *args, **kwargs)


class timePrint:
    """带时间戳的print
with timePrint() as print:
    print(0)
    # >>> [2019-02-10 16:23:35] 0

    print(1, strf="[%Y-%m-%d %H:%M:%S]1")
    # >>> [2019-02-10 16:23:35]1 1

with timePrint("[%Y-%m-%d %H:%M:%S]2") as print:
    print(2)
    # >>> [2019-02-10 16:23:35]2 2

    print(3, strf="[%Y-%m-%d %H:%M:%S]3")
    # >>> [2019-02-10 16:23:35]3 3

print(4)
# >>> 4
"""

    def __init__(self, strf="[%Y-%m-%d %H:%M:%S]"):
        self.__strf = strf

    def __enter__(self):
        self.__mode = 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__mode = 0

    def __call__(self, *args, **kwargs):
        if self.__mode == 1:
            if not "strf" in kwargs.keys():
                kwargs["strf"] = self.__strf
            _timePrint(*args, **kwargs)
        else:
            rawPrint(*args, **kwargs)


if __name__ == '__main__':
    with timePrint() as print:
        print(0)
        # >>> [2019-02-10 16:23:35] 0

        print(1, strf="[%Y-%m-%d %H:%M:%S]1")
        # >>> [2019-02-10 16:23:35]1 1

    with timePrint("[%Y-%m-%d %H:%M:%S]2") as print:
        print(2)
        # >>> [2019-02-10 16:23:35]2 2

        print(3, strf="[%Y-%m-%d %H:%M:%S]3")
        # >>> [2019-02-10 16:23:35]3 3

    print(4)
    # >>> 4

    print(timePrint.__doc__)
