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
    """带时间戳的print"""

    def __init__(self, strf="[%Y-%m-%d %H:%M:%S]"):
        self.__strf = strf

    def __enter__(self):
        self.__mode = 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__mode = 0

    def __call__(self, *args, **kwargs):
        if self.__mode == 1:
            kwargs["strf"] = self.__strf
            _timePrint(*args, **kwargs)
        else:
            rawPrint(*args, **kwargs)


if __name__ == '__main__':
    with timePrint() as print:
        print(10)
    print(11)
